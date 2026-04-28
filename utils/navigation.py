import streamlit as st


def render_sidebar_navigation(active_page: str | None = None) -> None:
    with st.sidebar:
        st.subheader("메뉴")
        st.page_link(
            "pages/1_종목_분석실.py",
            label="종목 분석실",
            disabled=active_page == "analysis",
        )
        st.page_link(
            "pages/2_주문_보유현황.py",
            label="주문/보유현황",
            disabled=active_page == "operations",
        )
        st.divider()
