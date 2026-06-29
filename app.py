import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 화면 70% 제한 및 버튼 디자인
st.markdown("""
    <style>
    .main .block-container {
        max-width: 70% !important;
        margin: 0 auto !important;
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
        margin: 10px auto !important;
        display: block;
    }
    h1 { text-align: center; margin-bottom: 50px !important; }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([{"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}])
if 'role' not in st.session_state: st.session_state.role = None
if 'admin_authenticated' not in st.session_state: st.session_state.admin_authenticated = False

# [1] 첫 화면
if st.session_state.role is None:
    st.title("🏫 학원 관리 시스템")
    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()

# [2] 운영자 로그인
elif st.session_state.role == "admin_login":
    st.title("🔐 운영자 인증")
    if st.text_input("암호를 입력하세요", type="password") == "slzhfcjswo":
        st.session_state.admin_authenticated = True
        st.session_state.role = "admin"
        st.rerun()
    if st.button("돌아가기"):
        st.session_state.role = None
        st.rerun()

# [3] 선생님 모드
elif st.session_state.role == "teacher":
    st.header("👩‍🏫 선생님 전용 화면")
    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.rerun()
    edited_df = st.data_editor(st.session_state.data, disabled=["학생명", "기본교육비", "납부확인"], use_container_width=True)
    if st.button("저장"):
        st.session_state.data = edited_df
        st.success("저장 완료!")

# [4] 운영자 모드
elif st.session_state.role == "admin" and st.session_state.admin_authenticated:
    st.header("👤 운영자 전용 관리")
    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.session_state.admin_authenticated = False
        st.rerun()
    
    col_a, col_b = st.columns(2)
    current_year = col_a.selectbox("연도", [2026, 2027])
    current_month = col_b.selectbox("월", list(range(1, 13)), index=datetime.datetime.now().month - 1)
    
    if st.button("➕ 학생 등록"):
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([{"학생명": "신규", "기본교육비": 0, "교재명": "", "교재비": 0, "납부확인": False}])])
        st.rerun()
        
    st.data_editor(st.session_state.data, num_rows="dynamic", use_container_width=True)
