# Lead, Brainstorm, and Designer

Use this pattern when the user selects three persistent collaborators with temporary
implementation and review workers. It does not create a team or authorize work by
itself. Preserve the user's chosen model and reasoning effort for each role; if a
choice is unavailable, report that instead of substituting another model.

## Roles and user conversations

| Role | Owns | Typical user request |
| --- | --- | --- |
| Lead | Delivery, architecture, priorities, worker assignments, integration, verification | Build this; fix this; what is the status? |
| Brainstorm | Product exploration, alternatives, challenging assumptions | Is this useful; what are the tradeoffs? |
| Designer | Visual direction, interaction design, prototypes, design acceptance | Show options; improve this flow. |

These are the user's three direct collaborators. The user can stay in whichever
conversation they started; agents handle the handoff without asking the user to
repeat decisions. Project-wide status and competing priorities belong with Lead.

Distinguish exploration, decisions, and authorized execution. “Just exploring”
keeps the work conceptual. “Let's choose this” settles a decision. “Build it”
authorizes implementation within the discussed scope. Interpret ordinary language
in context; these examples are not required commands. Implementation approval
never implies publishing approval beyond the user's existing instructions.

## Synchronization

- The agent receiving a consequential user direction records its meaning, scope,
  source, and time in its current decision notes, then sends affected agents one
  concise inbox notice with the decision and the note's path. Label ideas,
  recommendations, settled decisions, and authorized work distinctly.
- Lead maintains a small shared current plan: accepted decisions, owners and paths,
  dependencies, active work, and pending user questions. Link role-owned notes and
  reports rather than copying their full contents. Keep this in the project's
  private coordination area, not public product content.
- Brainstorm and Designer may consult each other directly within the authorized
  work. Copy Lead on consequential outcomes; Lead need not relay every exchange.
- Before starting dependent work, read the current plan and relevant role notes.
  Inbox delivery may be delayed. A queued notice is not proof it has been read;
  an older notice must not undo a newer decision or completed acceptable work.
- If directions genuinely conflict, pause only the affected work and have one
  agent bring the unresolved choice to the user. Continue independent work.
- Sync at decisions, handoffs, blockers, and completion. Use reports for routine
  completion and inboxes for assignments, decisions, questions, and corrections.
  Do not require acknowledgment loops or continuous status chatter. Verify receipt
  when execution depends on it; never type assignments into a running terminal.

## Implementation and review

Lead owns production-code assignments and temporary worker lifecycle. Designer
supplies the design brief and checks the implementation. Brainstorm explores and
challenges proposals without creating a parallel implementation track. Preserve
explicit user exceptions and work already authorized directly to a role.

Use one writer per path and isolated worktrees for parallel implementation. Small
fixes can stay with Lead; substantial features go to a builder when delegation is
authorized. Lead examines consequential findings and critical code paths directly;
a reviewer or a high reasoning setting does not replace that judgment. Match
review scope to risk and assess reviewer quality from actual findings.

Builders and reviewers are temporary. Launch them only within current authorization,
with one complete brief, exact model/effort, ownership, checks, and a report destination.
Retain a worker through related fix/recheck rounds. Once its assignment is finished,
collect its report and preserve its changes, then terminate that worker session.
Session cleanup does not authorize deleting its branch, worktree, or artifacts.
Lead handles worker communication so the user does not need to manage those sessions.
