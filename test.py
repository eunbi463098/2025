"""
Streamlit Mood-based Music Recommender - Korean Songs Version (Embed 가능한 영상)

▶ 기능
- 사용자가 기분을 선택하면 그에 맞는 한국 노래(임베드 가능한 유튜브 링크)를 추천합니다.
- 기분: 행복 😀, 슬픔 😢, 분노 😡, 차분 😌, 신남 🤩, 피곤 😴, 집중 🎯
"""

import random
import streamlit as st

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(page_title="기분 음악 추천기", page_icon="🎵", layout="centered")

# -------------------------------
# 데이터: 기분별 한국 노래 유튜브 임베드 링크
# -------------------------------
MOOD_MUSIC = {
    "😀 행복": [
        "https://www.youtube.com/watch?v=BzYnNdJhZQw",  # 아이유 - 좋은 날
        "https://www.youtube.com/watch?v=gdZLi9oWNZg",  # BTS - Dynamite
    ],
    "😢 슬픔": [
        "https://www.youtube.com/watch?v=7XnH-p4T7xQ",  # 태연 - 사계
        "https://www.youtube.com/watch?v=d9IxdwEFk1c",  # 폴킴 - 모든 날, 모든 순간
    ],
    "😡 분노": [
        "https://www.youtube.com/watch?v=WMweEpGlu_U",  # 방탄소년단 - MIC Drop
        "https://www.youtube.com/watch?v=J-wFp43XOrA",  # 세븐틴 - 아주 NICE
    ],
    "😌 차분": [
        "https://www.youtube.com/watch?v=BzYnNdJhZQw",  # 아이유 - 밤편지
        "https://www.youtube.com/watch?v=7HN0Lz2exdE",  # 악동뮤지션 - 오랜 날 오랜 밤
    ],
    "🤩 신남": [
        "https://www.youtube.com/watch?v=J_CFBjAyPWE",  # 싸이 - That That (feat. SUGA)
        "https://www.youtube.com/watch?v=fJrCjz7FQjA",  # 세븐틴 - 아주 NICE
    ],
    "😴 피곤": [
        "https://www.youtube.com/watch?v=fHI8X4OXluQ",  # 백예린 - 밤하늘의 별을
        "https://www.youtube.com/watch?v=7HN0Lz2exdE",  # 악동뮤지션 - 오랜 날 오랜 밤
    ],
    "🎯 집중": [
        "https://www.youtube.com/watch?v=jeqdYqsrsA0",  # 아이유 - 무릎
        "https://www.youtube.com/watch?v=7NqXyoY-5Bw",  # 검정치마 - EVERYTHING
    ],
}

# -------------------------------
# UI
# -------------------------------
st.title("🎵 기분별 한국 노래 추천기")
st.caption("당신의 기분에 맞는 한국 노래를 추천해 드려요!")

mood = st.selectbox("지금 기분을 선택하세요", list(MOOD_MUSIC.keys()))

if mood:
    st.subheader(f"당신의 기분: {mood}")
    urls = MOOD_MUSIC[mood]
    choice = random.choice(urls)
    st.video(choice)

    st.markdown("---")
    st.markdown("**다른 추천 곡**")
    for u in urls:
        if u != choice:
            st.write(u)

# -------------------------------
# 팁
# -------------------------------
st.divider()
st.markdown(
    """
**Tips**
- 🎶 `MOOD_MUSIC` 딕셔너리에 원하는 한국 노래 유튜브 링크를 더 추가할 수 있어요.
- 🔀 매번 다른 노래를 듣고 싶으면 `random.choice` 대신 `random.shuffle`을 써서 여러 곡을 보여줄 수 있어요.
- 🧩 더 발전시키려면 Spotify API, YouTube Data API를 연동할 수도 있습니다.
"""
)
