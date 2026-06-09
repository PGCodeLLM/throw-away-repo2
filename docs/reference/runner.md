# `runner` reference

Helpers that execute user-supplied input. This module exists as a fixture for
security scanners and is **intentionally unsafe**.

> ## ⚠️ Security warning
>
> The functions in this module pass input to the shell and to `eval`. They are
> documented here only so the reference matches the code. **Do not use this
> module in production and never pass it untrusted input.**

```python
from src import runner
```

## `run(user_input)`

Echoes `user_input` by interpolating it into a shell command via `os.system`.

```python
runner.run("hello")  # prints: hello
```

- **Side effect:** spawns a shell.
- **Unsafe:** `user_input` is interpolated directly into the command string, so
  shell metacharacters are interpreted (command injection). Treat all input as
  trusted-only.

## `load(data)`

Evaluates `data` as a Python expression via `eval` and returns the result.

```python
runner.load("1 + 1")  # -> 2
```

- **Unsafe:** `eval` executes arbitrary code contained in `data`. Never call
  this with input you do not fully control.
