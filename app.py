import streamlit as st
import pandas as pd

# 데이터 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([
        {"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False},
        {"학생명": "이영희", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False},
        {"학생명": "박민호", "기본교육비": 300000, "교재명": "", "교재비": 0, "납부확인": False},
    ])

# 1. 로그인/역할 선택 상태 설정
if 'role' not in st.session_state:
    st.session_state.role = None

# 첫 화면 (역할 선택)
if st.session_state.role is None:
    st.title("🏫 학원 관리 시스템")
    st.subheader("사용자를 선택해주세요.")
    
    col1, col2 = st.columns(2)
    if col1.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()
    if col2.button("👤 운영자 모드"):
        st.session_state.role = "admin"
        st.rerun()

# 역할별 화면 구성
else:
    st.sidebar.button("🔙 처음으로", on_click=lambda: st.session_state.update({"role": None}))
    
    if st.session_state.role == "teacher":
        st.title("👩‍🏫 선생님 전용 화면")
        # 교재비 입력 기능만 제공
        search_name = st.text_input("🔍 학생 검색")
        df = st.session_state.data
        if search_name: df = df[df['학생명'].str.contains(search_name)]
        
        edited_df = st.data_editor(df, disabled=["학생명", "기본교육비", "납부확인"])
        if st.button("저장"):
            st.session_state.data.update(edited_df)
            st.success("저장 완료!")

    elif st.session_state.role == "admin":
        st.title("👤 운영자 전용 화면")
        # 전체 데이터 수정 및 삭제 기능
        st.dataframe(st.session_state.data)
        st.metric("총 매출", f"{(st.session_state.data['기본교육비'] + st.session_state.data['교재비']).sum():,}원")
