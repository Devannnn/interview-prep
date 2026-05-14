Check the current README interview questions for structure, table of contents accuracy, and difficulty ordering.

Workflow:

1. Read the current README file.
2. Identify all interview question headings and their answer blocks.
3. Check that the table of contents matches the actual question headings:
   - every question appears exactly once
   - numbering is sequential
   - link text matches the heading text
   - anchors match the generated Markdown heading anchors
4. Check that the question sections themselves are numbered sequentially.
5. Check whether the questions are ordered from easier to harder.
6. Use this difficulty progression unless the README clearly implies another order:
   - basic concepts and definitions
   - local repository state and inspection commands
   - remotes and collaboration workflows
   - temporary work management
   - undoing changes and history rewriting concepts
   - merge conflicts, merge/rebase, and advanced history topics
7. Report any issues found, grouped by:
   - table of contents issues
   - numbering issues
   - difficulty ordering issues
8. If changes are needed, propose the corrected order before editing.
9. If I ask you to fix it, update the README while preserving the existing answer text.
10. After editing, reread the README and verify that the table of contents, numbering, and order are correct.

When reviewing difficulty:

- Prefer a practical interview-learning order over strict Git internals order.
- Keep closely related questions together when possible.
- Do not rewrite answers unless I explicitly ask.
- If multiple valid orders exist, explain the tradeoff briefly and choose the clearest progression for a beginner-to-intermediate interview prep README.
