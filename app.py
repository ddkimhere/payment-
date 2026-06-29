import streamlit as st
import pandas as pd

# 데이터 설정
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame([
        {"학생명": "김철수", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False},
        {"학생명": "이영희", "기본교육비": 250000, "교재명": "", "교재비": 0, "납부확인": False},
        {"학생명": "박민호", "기본교육비": 300000, "교재명": "", "교재비": 0, "납부확인": False},
    ])

st.set_page_config(page_title="학원 정산 시스템", layout="wide")

st.title("🏫 학원 교육비 & 교재비 정산 시스템")

# 검색
search_name = st.text_input("🔍 학생 이름을 입력하세요", "")

# 데이터 필터링
df = st.session_state.data
if search_name:
    filtered_df = df[df['학생명'].str.contains(search_name)]
else:
    filtered_df = df

st.subheader("📋 정산 리스트")

# 데이터 편집기
edited_df = st.data_editor(
    filtered_df,
    column_config={
        "납부확인": st.column_config.CheckboxColumn("✅ 납부완료"),
        "교재비": st.column_config.NumberColumn("💰 교재비 (원)", format="%d"),
    },
    disabled=["학생명", "기본교육비"],
    num_rows="dynamic",
    use_container_width=True
)

# 합계 계산
total_tuition = edited_df['기본교육비'].sum()
total_books = edited_df['교재비'].sum()
st.info(f"💡 검색된 학생 합계: 교육비 {total_tuition:,}원 + 교재비 {total_books:,}원 = 총 {(total_tuition + total_books):,}원")

# 저장 버튼
if st.button("💾 변경사항 저장하기"):
    st.session_state.data.update(edited_df)
    st.success("데이터가 성공적으로 저장되었습니다!")