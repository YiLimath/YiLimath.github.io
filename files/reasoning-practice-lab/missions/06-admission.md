# 06 — A proof-producing system that can reject its own output

Use the course Module 6 and its pinned Lean lab. If no executable environment is available, record this as a design exercise; never report a compilation success.

Select one exact statement from missions 02 or 05. Ask Codex to encode it and produce a proof. Inspect the actual declaration and domain assumptions. Retain the environment identification, source, actual checker output, and dependency/axiom inspection.

Faults to inject separately: a wrong target encoded as a true theorem; a placeholder proof; an extra assumption that already implies the conclusion; an old successful check attached to modified source.

Deliver: admission decisions for each artifact, including which policy check rejects each fault. A zero exit code alone is not the complete admission record. A conversation asserting “verified” is no execution evidence.

Harder challenge: arrange a reproducible admission path for an unchanged approved statement and pinned dependencies, then rerun it on the faults. Explain the remaining trusted components and semantic-alignment boundary. Do not claim all mathematical statements can be decided automatically.
