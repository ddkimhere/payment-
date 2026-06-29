import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼들을 중앙에 10px 간격으로 고정 배치
st.markdown("""
    <style>
    /* 중앙 정렬을 위한 컨테이너 */
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px !important;
        margin-top: 50px;
    }
    /* 버튼 스타일 */
    div.stButton > button {
        width: 320px !important;
        height: 200px !important;
        font-size: 36px !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
        color: white !important;
        box-shadow: 0 10px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([{"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False}])
if 'role' not in st.session_state: st.session_state.role = None
if 'admin_authenticated' not in st.session_state: st.session_state.admin_authenticated = False

# [1] 첫 화면
if st.session_state.role is None:
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px; font-size: 50px;'>🏫 학원 관리 시스템</h1>", unsafe_allow_html=True)
    
    # CSS 클래스를 적용한 컨테이너 시작
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    # Streamlit은 버튼 배치가 조금 까다로워서, 아래와 같이 나란히 배치합니다.
    col1, col2 = st.columns([0.16, 0.16]) # 버튼 크기만큼만 열을 할당하여 가운데로 모음
    with col1:
        if st.button("👤 운영자 모드"):
            st.session_state.role = "admin_login"
            st.rerun()
    with col2:
        if st.button("👩‍🏫 선생님 모드"):
            st.session_state.role = "teacher"
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# [2] 기능 화면 (이전과 동일)
elif st.session_state.role == "admin_login":
    st.title("🔐 운영자 인증")
    if st.text_input("암호를 입력하세요", type="password") == "0107":
        st.session_state.admin_authenticated = True
        st.session_state.role = "admin"
        st.rerun()
else:
    # (이하 로그인 후 화면 생략 - 기존 코드와 동일하게 유지하세요)
    st.write("로그인 성공!")
