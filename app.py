import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# 데이터 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([
        {"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}
    ])

if 'role' not in st.session_state:
    st.session_state.role = None
if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 1. 공통 상단: 연도/월 선택
st.title("🏫 학원 관리 시스템")
col1, col2 = st.columns(2)
current_year = col1.selectbox("연도 선택", [2026, 2027], index=0)
current_month = col2.selectbox("월 선택", list(range(1, 13)), index=datetime.datetime.now().month - 1)
st.markdown("---")

# 2. 첫 화면 (로그인 전)
if st.session_state.role is None:
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            width: 100%;
            height: 150px;
            font-size: 40px !important;
            font-weight: 800;
            border-radius: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()

# 3. 운영자 로그인 화면
elif st.session_state.role == "admin_login":
    st.title("🔐 운영자 인증")
    password = st.text_input("암호를 입력하세요", type="password")
    if st.button("확인"):
        if password == "0107":
            st.session_state.admin_authenticated = True
            st.session_state.role = "admin"
            st.rerun()
        else:
            st.error("암호가 틀렸습니다.")
    if st.button("뒤로가기"):
        st.session_state.role = None
        st.rerun()

# 4. 각 역할별 기능
else:
    if st.button("🔙 로그아웃"):
        st.session_state.role = None
        st.session_state.admin_authenticated = False
        st.rerun()

    if st.session_state.role == "teacher":
        st.header("👩‍🏫 선생님 전용 화면")
        edited_df = st.data_editor(st.session_state.data, disabled=["학생명", "기본교육비", "납부확인"])
        if st.button("저장"):
            st.session_state.data.update(edited_df)
            st.success("저장 완료!")

    elif st.session_state.role == "admin" and st.session_state.admin_authenticated:
        st.header(f"📅 {current_year}년 {current_month}월 정산 관리")
        
        if st.button("➕ 학생 신규 등록"):
            new_row = {"학생명": "신규학생", "기본교육비": 0, "교재명": "", "교재비": 0, "납부확인": False}
            st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
            st.rerun()

        edited_df = st.data_editor(st.session_state.data, num_rows="dynamic", use_container_width=True)
        
        if st.button("💾 이 달의 기록 저장하기"):
            st.session_state.data = edited_df
            st.success(f"{current_year}년 {current_month}월 데이터가 저장되었습니다.")
