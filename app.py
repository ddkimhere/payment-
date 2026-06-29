import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 버튼 중앙 정렬 및 제목까지 완벽하게 정렬
st.markdown("""
    <style>
    /* 제목 중앙 정렬 */
    .title-centered {
        text-align: center;
        margin-bottom: 50px;
    }
    /* 버튼들을 중앙으로 정렬하는 컨테이너 */
    .button-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }
    /* 버튼 크기 및 폰트 설정 */
    div.stButton > button {
        width: 600px !important;
        height: 200px !important;
        font-size: 50px !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
        color: white !important;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'role' not in st.session_state: st.session_state.role = None

# 첫 화면
if st.session_state.role is None:
    # 중앙 정렬된 제목
    st.markdown('<div class="title-centered"><h1>🏫 학원 관리 시스템</h1></div>', unsafe_allow_html=True)
    
    # 버튼 배치를 위한 중앙 컨테이너
    st.markdown('<div class="button-wrapper">', unsafe_allow_html=True)
    
    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()
        
    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# (이후 기능 구현은 기존과 동일)
