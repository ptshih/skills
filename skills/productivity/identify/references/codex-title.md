# Codex conversation title

Prefer an exposed native rename tool. Otherwise inspect `codex app-server --help`
and generate the installed JSON schemas into a temporary directory with
`codex app-server generate-json-schema --out <temporary-directory>`. Check
`ClientRequest.json`, `v1/InitializeParams.json`, `v2/ThreadReadParams.json`, and
`v2/ThreadSetNameParams.json` before constructing requests.

Use the current `CODEX_THREAD_ID` or an equally authoritative current-session ID.
If neither is available, report the missing target instead of guessing from titles.
Use `codex app-server proxy` when an existing control daemon is available; otherwise
use a temporary `codex app-server --stdio` process. A missing daemon socket does
not require installing, enabling, or restarting a daemon.

The protocol verified on 2026-10-31 uses newline-delimited JSON over stdin/stdout:

1. Request `initialize` with a `clientInfo` object containing a client `name` and
   `version`. This identifies the API client, not the user's agent role.
2. After success, send the `initialized` notification.
3. Request `thread/read` with `threadId` and `includeTurns: false`. Confirm the
   returned thread ID matches the current session and inspect `thread.name` only.
4. If needed, request `thread/name/set` with that `threadId` and the desired `name`.
5. Request `thread/read` again and compare `thread.name` with the desired title.

Use distinct request IDs, match responses by ID, handle protocol errors, and bound
waits. Avoid printing conversation content or unrelated notifications. Close only
the temporary client/process created for this operation. If an update response is
lost, read back before retrying. Do not start/resume a thread or turn, change auth,
or edit transcript files, indexes, or databases. Respect explicit denials.

This changes the conversation title. It does not establish a separate Codex agent
routing alias. Herdr agent registration is a different field.

Reference: [Codex app-server](https://developers.openai.com/codex/app-server/).
