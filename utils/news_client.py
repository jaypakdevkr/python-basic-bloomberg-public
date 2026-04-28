from datetime import datetime
from typing import Any


def fetch_company_news(
    *,
    company_name: str,
    symbol: str = "",
    max_items: int = 5,
    days: int = 7,
) -> list[dict[str, Any]]:
    keyword = company_name.strip() or symbol.strip() or "종목"

    articles: list[dict[str, Any]] = []
    for index in range(max_items):
        articles.append(
            {
                "title": f"{keyword} 관련 뉴스 자리 {index + 1}",
                "link": "https://example.com/news-placeholder",
                "source_name": "예시 출처",
                "source_url": "https://example.com",
                "published_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "description": f"10-6장에서 RSS 기반 뉴스 수집으로 교체할 자리입니다. 기간: 최근 {days}일",
            }
        )

    return articles
