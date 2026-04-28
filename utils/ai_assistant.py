import os
from typing import Any

DEFAULT_OPENAI_MODEL = "gpt-5.4-mini"


def get_ai_runtime_status() -> dict[str, Any]:
    return {
        "provider": "openai-placeholder" if os.getenv("OPENAI_API_KEY") else "local-placeholder",
        "model": os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL),
        "api_key_configured": bool(os.getenv("OPENAI_API_KEY")),
    }


def ask_analysis_copilot(context: dict[str, Any], question: str) -> dict[str, Any]:
    symbol = context.get("symbol", "-")
    company_name = context.get("company_name", symbol)
    return {
        "answer": (
            f"지금은 스켈레톤 단계입니다. "
            f"{company_name}({symbol}) 화면을 읽어 AI가 설명하도록 10-5장에서 확장합니다."
        ),
        "key_points": [
            f"질문: {question}",
            "analysis_context를 기반으로 OpenAI 응답 구현",
        ],
        "risk_flags": ["현재는 예시 문장만 반환합니다."],
        "unknowns": ["실제 AI 호출은 아직 연결되지 않았습니다."],
        "source": "skeleton",
    }


def summarize_ops_context(context: dict[str, Any]) -> dict[str, Any]:
    return {
        "answer": "10-8장에서 주문 상태와 보유현황을 읽어 AI 요약을 붙일 예정입니다.",
        "key_points": ["잔고와 주문 데이터를 요약하는 흐름 구현"],
        "risk_flags": ["현재는 스켈레톤 응답입니다."],
        "unknowns": [],
        "source": "skeleton",
    }


def summarize_news_briefing(company_name: str, articles: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "summary": f"{company_name} 관련 뉴스 브리핑은 10-6장에서 구현",
        "opportunities": ["뉴스에서 긍정 신호 요약 구현"],
        "warnings": ["뉴스에서 경고 신호 요약 구현"],
        "needs_confirmation": [f"기사 수: {len(articles)}"],
        "source": "skeleton",
    }
