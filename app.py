import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼을 아래위로 배치하고 글씨를 50px로 키움
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
        margin: 10px auto; /* 아래위 간격 10px */
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([{"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}])
if 'role' not in st.session_state: st.session_state.role = None
if 'admin_authenticated' not in st.session_state: st.session_state.admin_authenticated = False

# 첫 화면: 아래위 배치
if st.session_state.role is None:
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px; font-size: 50px;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)
    
    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
    
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()

# (로그인 및 기능 화면은 이전과 동일하게 유지됩니다)
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
    # 로그인 후 화면 (기본 연동 기능 유지)
    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.rerun()
    
    if st.session_state.role == "teacher":
        st.subheader("👩‍🏫 교재비 입력 모드")
        edited_df = st.data_editor(st.session_state.data, disabled=["학생명", "기본교육비", "납부확인"], use_container_width=True)
        if st.button("저장"):
            st.session_state.data = edited_df
            st.success("저장 완료!")

    elif st.session_state.role == "admin":
        st.subheader("👤 운영자 총괄 관리")
        st.data_editor(st.session_state.data, num_rows="dynamic", use_container_width=True)
