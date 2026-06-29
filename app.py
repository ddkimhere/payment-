import streamlit as st

# 페이지 설정
st.set_page_config(page_title="학원 관리 시스템", layout="wide")

# CSS: 화면 전체를 활용하여 버튼을 강제로 가로 중앙 배치
st.markdown("""
    <style>
    /* 전체 화면 중앙 정렬 */
    .block-container {
        display: flex;
        flex-direction: column;
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
        margin: 5px 0 !important;
    }
    h1 {
        text-align: center;
        margin-bottom: 50px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 초기화
if 'role' not in st.session_state: st.session_state.role = None

# 첫 화면
if st.session_state.role is None:
    st.title("🏫 학원 관리 시스템")
    
    # 버튼을 중앙 정렬시키기 위한 핵심 로직
    # 빈 열(col)을 활용하여 버튼 그룹을 중앙에 배치
    _, center_col, _ = st.columns([1, 2, 1])
    
    with center_col:
        if st.button("👤 운영자 모드"):
            st.session_state.role = "admin_login"
            st.rerun()
        if st.button("👩‍🏫 선생님 모드"):
            st.session_state.role = "teacher"
            st.rerun()
