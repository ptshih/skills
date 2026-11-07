# Overlord watcher: poll every 60 s and print a line only when something needs a look.
# Usage: python3 -I watch.py <repo path>. Run under a Monitor; each line is one event.
import json, os, subprocess, sys, time

REPO = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
WS, ME = os.environ.get("HERDR_WORKSPACE_ID"), os.environ.get("HERDR_PANE_ID", "")
LONG = 20 * 60  # flag an agent that has been working this long without a state change


def run(*args):
    return subprocess.run(args, capture_output=True, text=True, timeout=30).stdout


def agents():
    data = json.loads(run("herdr", "agent", "list"))["result"]["agents"]
    return {a["pane_id"]: (a.get("terminal_title_stripped") or a["pane_id"], a.get("agent_status", "?"))
            for a in data if a.get("workspace_id") == WS and a["pane_id"] != ME}


def git_state():
    git = lambda *a: run("git", "-C", REPO, *a)
    trees = {}
    for line in git("worktree", "list").splitlines():
        parts = line.split()
        trees[parts[0]] = parts[2] if len(parts) > 2 else parts[1]
    folder = os.path.join(REPO, ".worktrees")
    dirs = {os.path.join(folder, d) for d in os.listdir(folder)} if os.path.isdir(folder) else set()
    return {
        "main": git("rev-parse", "--short", "main").strip(),
        "branch": git("branch", "--show-current").strip(),
        "tracked": sorted(l for l in git("status", "--porcelain").splitlines() if not l.startswith("??")),
        "trees": trees,
        "orphans": sorted(dirs - trees.keys()),
    }


def git_changes(old, new):
    if old["main"] != new["main"]:
        yield f"main moved {old['main']} -> {new['main']}"
    if old["branch"] != new["branch"]:
        yield f"shared checkout switched {old['branch'] or 'detached'} -> {new['branch'] or 'detached'}"
    if old["tracked"] != new["tracked"]:
        yield f"shared checkout tracked changes: {', '.join(new['tracked']) or 'none'}"
    for path in new["trees"].keys() - old["trees"].keys():
        yield f"worktree added {path} {new['trees'][path]}"
    for path in old["trees"].keys() - new["trees"].keys():
        yield f"worktree removed {path}"
    if old["orphans"] != new["orphans"]:
        yield f"orphan worktree folders: {', '.join(os.path.basename(o) for o in new['orphans']) or 'none'}"


prev_agents, prev_git, working_since = None, None, {}
while True:
    try:
        cur, now = agents(), time.time()
        if prev_agents is None:
            print(f"watching {len(cur)} agents: " + ", ".join(f"{n}={s}" for n, s in cur.values()))
        else:
            for p in cur.keys() - prev_agents.keys():
                print(f"NEW {cur[p][0]} ({p}): {cur[p][1]}")
            for p in prev_agents.keys() - cur.keys():
                print(f"GONE {prev_agents[p][0]} ({p})")
            for p in cur.keys() & prev_agents.keys():
                if cur[p][1] != prev_agents[p][1]:
                    print(f"{cur[p][0]} ({p}): {prev_agents[p][1]} -> {cur[p][1]}")
        for p, (name, status) in cur.items():
            if status != "working":
                working_since.pop(p, None)
                continue
            start, flagged = working_since.setdefault(p, (now, 0))
            if (now - start) // LONG > flagged:
                working_since[p] = (start, flagged + 1)
                print(f"{name} ({p}) has been working {int((now - start) // 60)} min without a state change")
        prev_agents = cur
        state = git_state()
        if prev_git is None:
            print(f"git: main {state['main']}, checkout {state['branch']}, {len(state['trees'])} worktrees, "
                  f"orphans: {', '.join(os.path.basename(o) for o in state['orphans']) or 'none'}")
        else:
            for line in git_changes(prev_git, state):
                print("git: " + line)
        prev_git = state
    except Exception as e:
        print(f"watcher error: {e}")
    sys.stdout.flush()
    time.sleep(60)
