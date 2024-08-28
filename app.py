import streamlit as st
from datetime import datetime

# 기본 설정
st.set_page_config(page_title="일정 트래킹 서비스", page_icon="📅", layout="centered")

# 페이지 제목
st.title("📅 일정 트래킹 서비스")

# 날짜 선택
selected_date = st.date_input("날짜를 선택하세요", datetime.now())

# 날짜에 해당하는 일정 저장용 변수
if 'schedule' not in st.session_state:
    st.session_state['schedule'] = {}

# 사용자가 입력한 일정
if selected_date not in st.session_state['schedule']:
    st.session_state['schedule'][selected_date] = []

# 일정 추가 섹션
st.subheader(f"{selected_date.strftime('%Y-%m-%d')}의 일정 추가")
new_task = st.text_input("새로운 일정 입력")
if st.button("일정 추가"):
    if new_task:
        st.session_state['schedule'][selected_date].append(new_task)
        st.success("일정이 추가되었습니다!")
    else:
        st.error("일정을 입력하세요.")

# 일정 목록 보기
st.subheader(f"{selected_date.strftime('%Y-%m-%d')}의 일정 목록")
if st.session_state['schedule'][selected_date]:
    for i, task in enumerate(st.session_state['schedule'][selected_date], start=1):
        st.write(f"{i}. {task}")
else:
    st.write("추가된 일정이 없습니다.")

# 일정 삭제 기능 (옵션)
if st.session_state['schedule'][selected_date]:
    delete_task = st.selectbox("삭제할 일정을 선택하세요", st.session_state['schedule'][selected_date])
    if st.button("일정 삭제"):
        st.session_state['schedule'][selected_date].remove(delete_task)
        st.success("일정이 삭제되었습니다.")
