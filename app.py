import streamlit as st
import pandas as pd

# 데이터 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([
        {"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False},
        {"학생명": "이영희", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False},
        {"학생명": "박민호", "기본교육비": 300000, "교재명": "", "교재비": 0, "납부확인": False},
    ])

if 'role' not in st.session_state:
    st.session_state.role = None
if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# 첫 화면
if st.session_state.role is None:
    st.title("🏫 학원 관리 시스템")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 큰 버튼 만들기 (CSS 사용)
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            width: 100%;
            height: 100px;
            font-size: 24px;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # 운영자 버튼 (암호 확인 로직)
    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 선생님 버튼
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()

# 운영자 암호 입력 화면
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

# 역할별 화면
else:
    if st.button("🔙 로그아웃"):
        st.session_state.role = None
        st.session_state.admin_authenticated = False
        st.rerun()
    
    if st.session_state.role == "teacher":
        st.title("👩‍🏫 선생님 전용 화면")
        edited_df = st.data_editor(st.session_state.data, disabled=["학생명", "기본교육비", "납부확인"])
        if st.button("저장"):
            st.session_state.data.update(edited_df)
            st.success("저장 완료!")

    elif st.session_state.role == "admin" and st.session_state.admin_authenticated:
        st.title("👤 운영자 전용 화면")
        st.dataframe(st.session_state.data, use_container_width=True)
        st.metric("총 매출", f"{(st.session_state.data['기본교육비'] + st.session_state.data['교재비']).sum():,}원")
