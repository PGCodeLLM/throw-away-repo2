# `calculator` reference

Basic arithmetic helpers. All functions are pure: they take numeric arguments
and return a result without side effects.

```python
from src import calculator
```

## `add(a, b)`

Returns the sum of `a` and `b`.

```python
calculator.add(2, 3)  # -> 5
```

## `subtract(a, b)`

**Intended contract:** returns the difference `a - b`.

```python
calculator.subtract(5, 3)  # intended -> 2
```

> **Known issue:** the current implementation returns `a + b` instead of
> `a - b`. See [Known issues](#known-issues) below.

## `divide(a, b)`

**Intended contract:** returns the quotient `a / b`.

```python
calculator.divide(6, 3)  # -> 2.0
```

> **Known issue:** there is no guard against division by zero. Calling
> `divide(x, 0)` raises `ZeroDivisionError`. See
> [Known issues](#known-issues) below.

## Known issues

These are documented as observations so the reference reflects actual behavior.
They are not addressed in this documentation change.

| Function    | Expected behavior | Actual behavior                       |
| ----------- | ----------------- | ------------------------------------- |
| `subtract`  | returns `a - b`   | returns `a + b`                       |
| `divide`    | returns `a / b`   | returns `a / b`; no zero-division guard |
