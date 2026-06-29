import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼 중앙 정렬 및 글씨 크기/굵기 강화
st.markdown("""
    <style>
    .stButton > button {
        width: 300px !important;
        height: 180px !important;
        font-size: 32px !important;
        font-weight: 900 !important;
        border-radius: 25px !important;
        background: linear-gradient(135deg, #4f46e5, #818cf8) !important;
        color: white !important;
        margin: 0 auto;
    }
    .main-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([{"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}])
if 'role' not in st.session_state: st.session_state.role = None
if 'admin_authenticated' not in st.session_state: st.session_state.admin_authenticated = False

# [1] 첫 화면: 중앙 정렬된 버튼
if st.session_state.role is None:
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)
    
    # 버튼을 감싸는 레이아웃 (중앙 정렬)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("👤 운영자 모드"):
            st.session_state.role = "admin_login"
            st.rerun()
    with col2:
        if st.button("👩‍🏫 선생님 모드"):
            st.session_state.role = "teacher"
            st.rerun()

# [2] 로그인 로직 및 기능 화면 (위와 동일)
elif st.session_state.role == "admin_login":
    st.title("🔐 운영자 인증")
    if st.text_input("암호를 입력하세요", type="password") == "0107":
        st.session_state.admin_authenticated = True
        st.session_state.role = "admin"
        st.rerun()
    if st.button("돌아가기"):
        st.session_state.role = None
        st.rerun()
else:
    col_a, col_b = st.columns(2)
    current_year = col_a.selectbox("연도", [2026, 2027])
    current_month = col_b.selectbox("월", list(range(1, 13)), index=datetime.datetime.now().month - 1)
    st.markdown("---")

    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.session_state.admin_authenticated = False
        st.rerun()

    if st.session_state.role == "teacher":
        st.subheader(f"👩‍🏫 {current_month}월 교재비 입력")
        edited_df = st.data_editor(st.session_state.data, disabled=["학생명", "기본교육비", "납부확인"], use_container_width=True)
        if st.button("저장"):
            st.session_state.data = edited_df
            st.success("저장 완료!")

    elif st.session_state.role == "admin":
        st.subheader(f"👤 {current_year}년 {current_month}월 총괄 관리")
        if st.button("➕ 학생 등록"):
            st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([{"학생명": "신규", "기본교육비": 0, "교재명": "", "교재비": 0, "납부확인": False}])])
            st.rerun()
        st.data_editor(st.session_state.data, num_rows="dynamic", use_container_width=True)
