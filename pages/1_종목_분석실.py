import streamlit as st

from utils.formatting import format_won
from utils.navigation import render_sidebar_navigation
from utils.storage import init_session_state

st.set_page_config(
    page_title="Bloomberg | 종목 분석실",
    layout="wide",
    initial_sidebar_state="expanded",
)
init_session_state()
render_sidebar_navigation(active_page="analysis")

st.title("종목 분석실")

with st.sidebar:
    st.subheader("주문 패널")

    account_mode = st.selectbox(
        "계좌 모드",
        options=["demo", "real"],
        key="order_ticket_account_mode",
        format_func=lambda value: "모의투자" if value == "demo" else "실전투자",
    )
    order_symbol = st.text_input("종목코드", key="order_ticket_symbol")
    side = st.selectbox(
        "주문 구분",
        options=["buy", "sell"],
        key="order_ticket_side",
        format_func=lambda value: "매수" if value == "buy" else "매도",
    )
    order_type = st.selectbox(
        "주문 유형",
        options=["market", "limit"],
        key="order_ticket_type",
        format_func=lambda value: "시장가" if value == "market" else "지정가",
    )
    qty = st.number_input("수량", min_value=1, step=1, key="order_ticket_qty")

    if order_type == "market":
        refresh_columns = st.columns([3, 1], vertical_alignment="bottom")
        with refresh_columns[1]:
            st.button(
                "↻",
                key="refresh_market_price",
                help="현재 시장가 새로고침",
                width="stretch",
                disabled=True,
            )

        with refresh_columns[0]:
            st.text_input(
                "가격",
                value=format_won(st.session_state.order_ticket_market_price),
                disabled=True,
            )

        st.caption(f"기준 시각: {st.session_state.order_ticket_market_as_of}")
        price = st.session_state.order_ticket_market_price
    else:
        st.caption(
            f"현재가 기준 빠른 선택: {format_won(st.session_state.order_ticket_market_price)}"
        )
        adjust_columns = st.columns(4)
        adjust_columns[0].button("-1,000원", width="stretch", disabled=True)
        adjust_columns[1].button("-500원", width="stretch", disabled=True)
        adjust_columns[2].button("+500원", width="stretch", disabled=True)
        adjust_columns[3].button("+1,000원", width="stretch", disabled=True)
        price = st.number_input(
            "가격",
            min_value=0,
            step=500,
            key="order_ticket_price",
            help="10-7장에서 주문 패널 입력 로직, 현재가 기준 빠른 선택, 주문 미리보기를 완성하고, 10-8장에서 주문 요청과 결과 확인 연결.",
        )

    preview_clicked = st.button("주문 미리보기", width="stretch")
    if preview_clicked:
        st.info(
            f"스켈레톤 단계에서는 {order_symbol or st.session_state.selected_symbol} "
            f"{qty}주, 가격 {format_won(price)} 초안만 보입니다. "
            "10-7장에서 주문 패널 입력 로직과 주문 미리보기를 완성하고, 10-8장에서 실제 주문 요청과 결과 확인 연결."
        )

    st.info(
        "10-7장에서 주문 패널 입력 로직과 주문 미리보기 구현. "
        "10-8장에서 주문 요청과 결과 확인 연결."
    )

st.write(
    "이 페이지는 10-3장부터 10-8장까지 가장 많이 다루게 될 핵심 화면입니다. "
    "지금은 자리만 잡아 두고, 이후 입력 폼, 차트와 지표, AI Copilot, 뉴스 브리핑, 주문 패널, 주문 결과 확인 구현."
)

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("분석 입력")
    st.info("10-3장에서 종목코드, 시작일, 종료일 입력 폼 구현")

    st.subheader("차트와 지표")
    st.info("10-4장에서 현재가, 기간 시세, 지표 카드, 차트 구현")

with right_col:
    st.subheader("AI Copilot")
    st.info("10-5장에서 추세 해설과 질문 응답 구현")

    st.subheader("뉴스 브리핑")
    st.info("10-6장에서 RSS 뉴스 브리핑 구현")
