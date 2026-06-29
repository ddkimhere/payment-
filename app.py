import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 정렬을 위해 전체 박스를 중앙 고정합니다.
st.markdown("""
    <style>
    /* 화면 중앙 정렬을 위한 최상위 컨테이너 설정 */
    .stApp {
        display: flex;
        justify-content: center;
    }
    .main .block-container {
        max-width: 70% !important;
        margin: 0 auto !important;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    /* 버튼 정렬 */
    div.stButton {
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        width: 300px !important;
        height: 100px !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        border-radius: 15px !important;
        background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
        color: white !important;
        box-shadow: 0 5px 10px rgba(0,0,0,0.2);
        margin: 5px 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# [데이터 초기화 및 로직은 기존과 동일]
if 'role' not in st.session_state: st.session_state.role = None
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([{"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}])

# 제목도 중앙 정렬
st.markdown("<h1 style='text-align: center;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)

# 메인 화면
if st.session_state.role is None:
    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()
else:
    # 기능 구현부
    if st.button("⬅️ 처음으로"):
        st.session_state.role = None
        st.rerun()
