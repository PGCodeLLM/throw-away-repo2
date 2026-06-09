# Architecture

This project is intentionally small. It is organized into two functional
layers plus a thin entry point.

## Layers

- **`calculator` (pure functions)** — Stateless arithmetic helpers with no
  side effects. Safe to call anywhere. See the
  [`calculator` reference](reference/calculator.md).
- **`runner` (executes input)** — Helpers that shell out and evaluate
  expressions. These have side effects and are **unsafe by design**. See the
  [`runner` reference](reference/runner.md).

## Entry point

`src/app.py` ties the layers together: it calls `calculator.add` and then
`runner.run`. Invoke it with:

```bash
python -m src.app
```

## Data flow

```text
app.main()
  ├─ calculator.add(2, 3)   → returns 5 (pure)
  └─ runner.run("hello")    → echoes via the shell (side effect)
```

See `src/` for the implementation of each module.
