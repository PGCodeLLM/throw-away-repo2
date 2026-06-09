# Implementation Notes

## Project layout
- Python repo. Source in `src/` (`calculator.py`, `app.py`, `runner.py`). No test framework, no manifest (no package.json / pyproject.toml / requirements).
- `src/calculator.py` holds pure arithmetic helpers. Style: module docstring, plain `def fn(a, b):`, no type hints. Existing `add`/`subtract`/`divide` have NO docstrings.
- Verify code changes by running `python3 -c "..."` and `python3 -m py_compile`, since there is no test runner.

## Conventions
- Wiki spec page = source of truth. Implement only the described delta; keep other functions unchanged.

## Out-of-scope observations (do NOT fix unless wiki says so)
- `subtract()` adds instead of subtracts (marked BUG).
- `divide()` has no zero check (marked BUG).
- `runner.py` has command injection (`os.system`) and `eval` of untrusted data (marked SECURITY).
These are intentional fixtures; leave them alone unless a wiki edit targets them.

## Runs
- 2026-06-09: "Multiply Feature" page (created) → added `multiply(a, b)` with one-line docstring to `src/calculator.py`. SHA 000...0 (created event default).
- 2026-06-09 (re-run): SHA 000...0 was already in processed-edits, BUT `multiply` was NOT present in `src/calculator.py` on `main` (prior PR never merged). Did NOT blindly noop on the dedup — verified code vs wiki, found the delta missing, re-implemented and opened a fresh PR. Lesson: the all-zeros created-event SHA is a degenerate dedup key (constant across all created events), so processed-edits cannot prove the code matches the spec. Always verify the source reflects the wiki before skipping.
