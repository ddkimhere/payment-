import streamlit as st
import pandas as pd
import datetime

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="학원 관리 시스템",
    page_icon="🏫",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>

/* 전체 화면 */
html, body, [data-testid="stAppViewContainer"]{
    background:#f5f7fb;
}

/* 가운데 정렬 */
.main .block-container{
    max-width:700px;
    margin:auto;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    min-height:100vh;
}

/* 카드 */
.card{
    background:white;
    padding:50px;
    border-radius:25px;
    box-shadow:0 15px 40px rgba(0,0,0,.12);
    width:100%;
    max-width:500px;
    text-align:center;
}

/* 제목 */
.title{
    font-size:42px;
    font-weight:800;
    margin-bottom:40px;
    color:#1f2937;
}

/* 버튼 */
div.stButton{
    display:flex;
    justify-content:center;
}

div.stButton > button{
    width:340px;
    height:90px;

    font-size:23px;
    font-weight:700;

    border:none;
    border-radius:18px;

    color:white;

    background:linear-gradient(135deg,#6366f1,#4f46e5);

    transition:all .25s;

    margin:12px auto;
}

div.stButton > button:hover{
    transform:translateY(-4px);
    box-shadow:0 10px 20px rgba(79,70,229,.35);
}

/* 입력창 */
div[data-baseweb="input"]{
    border-radius:12px;
}

/* Streamlit 메뉴 숨김 */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 세션
# -------------------------------------------------
if "role" not in st.session_state:
    st.session_state.role = None

if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False


# =================================================
# 첫 화면
# =================================================
if st.session_state.role is None:

    st.markdown("""
    <div class="card">
        <div class="title">🏫<br>학원 관리 시스템</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("👤 운영자 모드"):
        st.session_state.role = "admin_login"
        st.rerun()

    if st.button("👩‍🏫 선생님 모드"):
        st.session_state.role = "teacher"
        st.rerun()


# =================================================
# 운영자 로그인
# =================================================
elif st.session_state.role == "admin_login":

    st.markdown("""
    <div class="card">
        <div class="title">🔐 운영자 인증</div>
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input(
        "암호를 입력하세요",
        type="password"
    )

    if password == "slzhfcjswo":
        st.session_state.admin_authenticated = True
        st.session_state.role = "admin"
        st.rerun()

    st.write("")

    if st.button("⬅️ 돌아가기"):
        st.session_state.role = None
        st.rerun()


# =================================================
# 선생님
# =================================================
elif st.session_state.role == "teacher":

    st.markdown("""
    <div class="card">
        <div class="title">👩‍🏫 선생님 모드</div>
    </div>
    """, unsafe_allow_html=True)

    st.success("선생님 전용 기능을 여기에 추가하세요.")

    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.rerun()


# =================================================
# 운영자
# =================================================
elif (
    st.session_state.role == "admin"
    and st.session_state.admin_authenticated
):

    st.markdown("""
    <div class="card">
        <div class="title">👤 운영자 모드</div>
    </div>
    """, unsafe_allow_html=True)

    st.success("운영자 전용 기능을 여기에 추가하세요.")

    if st.button("⬅️ 로그아웃"):
        st.session_state.role = None
        st.session_state.admin_authenticated = False
        st.rerun()
