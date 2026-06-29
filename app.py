import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼 크기를 300px * 100px로 조정하고 중앙 배치
st.markdown("""
    <style>
    div.stButton > button {
        width: 300px !important;
        height: 100px !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        border-radius: 15px !important;
        background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
        color: white !important;
        box-shadow: 0 5px 10px rgba(0,0,0,0.2);
        margin: 5px auto !important;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# 세션 초기화
if 'role' not in st.session_state: st.session_state.role = None
if 'admin_authenticated' not in st.session_state: st.session_state.admin_authenticated = False

# [1] 첫 화면
if st.session_state.role is None:
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)
    
    # 버튼 배치를 위해 중앙 열 할당
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        if st.button("👤 운영자 모드"):
            st.session_state.role = "admin_login"
            st.rerun()
        if st.button("👩‍🏫 선생님 모드"):
            st.session_state.role = "teacher"
            st.rerun()

# [2] 운영자 로그인 (새 암호 적용)
elif st.session_state.role == "admin_login":
    st.title("🔐 운영자 인증")
    # 변경된 암호 적용
    if st.text_input("암호를 입력하세요", type="password") == "slzhfcjswo":
        st.session_state.admin_authenticated = True
        st.session_state.role = "admin"
        st.rerun()
    if st.button("돌아가기"):
        st.session_state.role = None
        st.rerun()

# [3] 선생님 모드
elif st.session_state.role == "teacher":
    st.title("👩‍🏫 선생님 전용 화면")
    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.rerun()
    # (선생님 기능 구현 자리)

# [4] 운영자 모드
elif st.session_state.role == "admin" and st.session_state.admin_authenticated:
    st.title("👤 운영자 전용 화면")
    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.session_state.admin_authenticated = False
        st.rerun()
    # (운영자 기능 구현 자리)
