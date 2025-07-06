import sys
import pysqlite3
sys.modules["sqlite3"] = pysqlite3

import streamlit as st
from crewai import Crew, Process, Task
from agents import coordinator_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from crew import TravelCoordinatorCrew

load_dotenv()

# Streamlit 앱 제목
st.title("🚀 여행 일정 계획 챗봇")

# 사용자 입력을 받는 영역
# user_input = st.text_area(
#     "여행 계획을 입력해 주세요:",
#     "2025년 7월 25일부터 27일까지 인천을 출발해서 오사카로 여행을 다녀오려고 합니다. "
#     "항공편, 숙소, 현지 맛집, 가볼만한 곳까지 포함해서 여행 일정을 상세히 만들어주세요. "
#     "예산은 총 80만 원 이내로 잡고 있어요. "
#     "혼자 가는 여행이라 너무 비싸지 않으면서 가성비 좋은 곳들로 부탁드려요."
# )

user_input = st.text_area(
    "여행 계획을 입력해 주세요:",
            "2025년 7월 25일부터 27일까지 인천을 출발해서 삿포로로 여행을 다녀오려고 합니다. "
            "25세인 딸과 같이 갑니다. 가급적이면 대중교통을 이용하고 싶어요. 관광을하면서 이동 시간을 미리 계산해서 다니고 싶습니다."
            "항공편, 숙소, 현지 맛집, 가볼만한 곳까지 포함해서 여행 일정을 상세히 만들어주세요. "
            "예산은 일인 당 80만 원 이내로 잡고 있어요. "
            "삿포로는 처음가는 여행이라 삿포로의 분위기를 느끼면서 가성비 좋은 곳들로 부탁드려요."
)

# 여행 일정 생성 버튼
if st.button("여행 일정 생성하기"):
    with st.spinner("일정을 생성 중입니다..."):

        inputs = {
            'content': user_input
        }

        result = TravelCoordinatorCrew().crew().kickoff(inputs=inputs)


    st.success("여행 일정 생성 완료!")

    # 생성된 일정 결과 출력
    st.markdown("### 📝 생성된 여행 일정:")
    st.markdown(result)
    print(result)
    
    