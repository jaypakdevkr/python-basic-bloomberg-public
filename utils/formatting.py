from typing import Any


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return default


def format_won(value: Any) -> str:
    return f"{int(round(_to_float(value))):,}원"


def format_number(value: Any) -> str:
    return f"{int(round(_to_float(value))):,}"


def format_percent(value: Any, digits: int = 2) -> str:
    number = _to_float(value)
    return f"{number:.{digits}f}%"
