# throw-away-repo2

A small Python sample project used as a fixture for end-to-end tooling. It
exposes two layers:

- **`calculator`** — pure arithmetic helper functions.
- **`runner`** — executes user-supplied input (intentionally unsafe; see the
  security warning below).

`app.py` wires the two together as a runnable entry point.

## Requirements

- Python 3.8 or newer (standard library only — no third-party dependencies).

## Project layout

| Path                | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| `src/app.py`        | Entry point that demonstrates the two modules.         |
| `src/calculator.py` | Pure arithmetic helpers (`add`, `subtract`, `divide`). |
| `src/runner.py`     | Command/expression execution helpers (unsafe).         |
| `docs/`             | Architecture overview and module reference.            |

## Quick start

Run the demo entry point from the repository root so that the `src` package
resolves correctly:

```bash
python -m src.app
```

This adds `2 + 3` via `calculator.add` and then echoes a greeting through
`runner.run`.

## Documentation

- [Architecture overview](docs/architecture.md) — how the layers fit together.
- [`calculator` reference](docs/reference/calculator.md) — arithmetic helpers.
- [`runner` reference](docs/reference/runner.md) — execution helpers (unsafe).

## ⚠️ Security note

The `runner` module runs shell commands and evaluates expressions from its
input by design — it exists as a fixture for security scanners. **Do not use it
in production or pass it untrusted input.** See the
[`runner` reference](docs/reference/runner.md) for details.
