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
    
    # 버튼 및 글씨체 크게 조정 (CSS)
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            width: 100%;
            height: 150px;
            font-size: 40px !important;
            font-weight: 800;
            border-radius: 20px;
            background-color: #f0f2f6;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            border: 3px solid #ff4b4b;
        }
        </style>
    """, unsafe_allow_html=True)

    # 운영자 버튼
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
    # 로그아웃 버튼을 우측 상단이나 사이드바에 배치 가능
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
        st.title("👤 운영자 전용 관리 페이지")
        
        # 1. 요약 대시보드
        total_tuition = st.session_state.data['기본교육비'].sum()
        total_books = st.session_state.data['교재비'].sum()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("총 교육비", f"{total_tuition:,}원")
        col2.metric("총 교재비", f"{total_books:,}원")
        col3.metric("전체 매출", f"{(total_tuition + total_books):,}원")

        st.markdown("---")

        # 2. 학생 데이터 편집 (추가/삭제 포함)
        st.subheader("학생 정산 데이터 관리")
        edited_df = st.data_editor(
            st.session_state.data, 
            num_rows="dynamic", 
            use_container_width=True
        )
        
        # 3. 저장 및 엑셀 다운로드 기능
        col_btn1, col_btn2 = st.columns([1, 4])
        if col_btn1.button("💾 데이터 저장"):
            st.session_state.data = edited_df
            st.success("데이터가 안전하게 저장되었습니다.")
            
        # 엑셀 다운로드 (CSV 변환)
        csv = edited_df.to_csv(index=False).encode('utf-8-sig')
        col_btn2.download_button(
            label="📥 엑셀로 저장하기",
            data=csv,
            file_name='학원정산내역.csv',
            mime='text/csv',
        )
