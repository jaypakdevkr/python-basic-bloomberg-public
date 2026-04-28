from typing import Any, Iterable

import pandas as pd

OHLCV_COLUMNS = ["date", "open", "high", "low", "close", "volume"]


def normalize_ohlcv(records: Iterable[dict[str, Any]]) -> pd.DataFrame:
    frame = pd.DataFrame(list(records))
    if frame.empty:
        return pd.DataFrame(columns=OHLCV_COLUMNS)

    for column in OHLCV_COLUMNS:
        if column not in frame.columns:
            frame[column] = 0

    frame["date"] = pd.to_datetime(frame["date"])
    for column in ["open", "high", "low", "close", "volume"]:
        frame[column] = pd.to_numeric(frame[column], errors="coerce").fillna(0)

    return frame[OHLCV_COLUMNS].sort_values("date").reset_index(drop=True)


def compute_indicators(price_df: pd.DataFrame) -> pd.DataFrame:
    if price_df.empty:
        return price_df.copy()

    df = price_df.copy()
    df["ma5"] = df["close"].rolling(window=5, min_periods=1).mean()
    df["ma20"] = df["close"].rolling(window=20, min_periods=1).mean()
    df["period_return_pct"] = ((df["close"] / df["close"].iloc[0]) - 1) * 100
    df["volatility_pct"] = df["close"].pct_change().fillna(0).rolling(window=20, min_periods=2).std().fillna(0) * 100
    df["momentum_score"] = 50.0
    return df


def build_analysis_summary(
    symbol: str,
    company_name: str,
    price_df: pd.DataFrame,
    current_quote: dict[str, Any],
) -> dict[str, Any]:
    if price_df.empty:
        return {
            "symbol": symbol,
            "company_name": company_name,
            "latest_close": 0,
            "period_return_pct": 0.0,
            "trend": {},
            "momentum": {},
            "risk": {},
        }

    latest_row = price_df.iloc[-1]
    return {
        "symbol": symbol,
        "company_name": company_name,
        "latest_close": float(current_quote.get("current_price", latest_row["close"])),
        "period_return_pct": float(latest_row.get("period_return_pct", 0.0)),
        "trend": {
            "ma5": float(latest_row.get("ma5", 0.0)),
            "ma20": float(latest_row.get("ma20", 0.0)),
            "signal": "TODO",
        },
        "momentum": {
            "momentum_score": float(latest_row.get("momentum_score", 0.0)),
        },
        "risk": {
            "volatility_pct": float(latest_row.get("volatility_pct", 0.0)),
        },
    }


def build_analysis_context(
    summary: dict[str, Any],
    order_draft: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "page": "analysis",
        "symbol": summary.get("symbol", ""),
        "company_name": summary.get("company_name", ""),
        "trend": summary.get("trend", {}),
        "momentum": summary.get("momentum", {}),
        "risk": summary.get("risk", {}),
        "current_order_draft": order_draft,
    }


def build_order_gap_summary(
    current_price: float,
    side: str,
    order_type: str,
    qty: int,
    price: float,
) -> dict[str, Any]:
    reference_price = current_price if order_type == "market" else price
    gap_price = reference_price - current_price
    gap_pct = (gap_price / current_price * 100) if current_price else 0.0

    warning = "정상 범위"
    if abs(gap_pct) >= 5:
        warning = "현재가와 괴리가 큽니다"
    elif abs(gap_pct) >= 2:
        warning = "주문 가격을 다시 확인하세요"

    return {
        "side": side,
        "order_type": order_type,
        "qty": int(qty),
        "price": round(reference_price, 2),
        "current_price": round(current_price, 2),
        "gap_price": round(gap_price, 2),
        "gap_pct_vs_current": round(gap_pct, 2),
        "warning": warning,
    }
