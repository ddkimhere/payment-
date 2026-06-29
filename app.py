import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼을 화면 중앙에 위아래로 배치하고 글씨를 50px로 설정
st.markdown("""
    <style>
    /* 버튼들을 감싸는 영역을 화면 중앙으로 정렬 */
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    /* 버튼 스타일 */
    div.stButton > button {
        width: 600px !important;
        height: 200px !important;
        font-size: 50px !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
        color: white !important;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3);
        margin: 10px 0 !important; /* 버튼 위아래 간격 */
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([{"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}])
if 'role' not in st.session_state: st.session_state.role = None
if 'admin_authenticated' not in st.session_state: st.session_state.admin_authenticated = False

# [첫 화면]: 중앙 위아래 배치
if st.session_state.role is None:
    # 제목도 중앙 정렬
    st.markdown("<h1 style='text-align: center; margin-bottom: 30px; font-size: 50px;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)
    
    # 버튼 배치를 위해 빈 공간 생성
    st.write("") 
    
    # 운영자 버튼
    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
    
    # 선생님 버튼
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()

# [로그인 및 기능 화면은 이전과 동일하게 유지]
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
    # 기능 화면 생략 (기존 로직 사용)
    st.subheader("관리 화면으로 진입했습니다.")
    if st.button("⬅️ 처음으로"):
        st.session_state.role = None
        st.rerun()
