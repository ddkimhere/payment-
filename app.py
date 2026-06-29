import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼 크기와 폰트만 설정
st.markdown("""
    <style>
    div.stButton > button {
        width: 600px !important;
        height: 200px !important;
        font-size: 50px !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
        color: white !important;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3);
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'role' not in st.session_state: st.session_state.role = None

# [1] 첫 화면: 중앙 정렬 핵심 로직
if st.session_state.role is None:
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px; font-size: 50px;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)
    
    # 3개의 열을 만들어 가운데(middle)에만 버튼 배치
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2: # 가운데 열에 버튼 배치
        if st.button("👤 운영자 모드"):
            st.session_state.role = "admin_login"
            st.rerun()
        
        if st.button("👩‍🏫 선생님 모드"):
            st.session_state.role = "teacher"
            st.rerun()

# (이하 로그인 및 기능 화면 로직은 동일)
elif st.session_state.role == "admin_login":
    # ... 기존 로그인 로직 ...
    pass
