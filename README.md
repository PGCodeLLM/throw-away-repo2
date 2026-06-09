# throw-away-repo2

A small Python service with two layers (see `docs/architecture.md`):

- `calculator` — pure arithmetic helpers
- `runner` — executes commands and is wired together in `app.py`

## Running

`src/app.py` uses package-relative imports (`from src import ...`), so run it
as a module from the repository root, not as a script:

```bash
python3 -m src.app
```

Running `python3 src/app.py` directly fails with `ModuleNotFoundError: No module named 'src'`.
