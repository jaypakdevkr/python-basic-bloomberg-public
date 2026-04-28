import streamlit as st

from utils.navigation import render_sidebar_navigation
from utils.storage import init_session_state

init_session_state()
render_sidebar_navigation(active_page="operations")

st.title("주문/보유현황")
st.write(
    "이 페이지는 주문 뒤 상태를 다시 확인하는 운영 화면입니다. "
    "10-8장에서 주문 내역, 미체결 주문, 보유 종목, 예수금 정보를 붙이게 됩니다."
)

col1, col2 = st.columns(2)
with col1:
    st.subheader("주문 상태")
    st.info("10-8장에서 최근 주문과 미체결 주문 조회 결과 구현")

with col2:
    st.subheader("보유 현황")
    st.info("10-8장에서 보유 종목, 예수금, 평가금액 조회 구현")
