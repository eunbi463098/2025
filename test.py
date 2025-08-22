"""
Streamlit Mood-based Music Recommender - 화려한 한국 노래 추천기

▶ 기능
- 사용자가 기분을 선택하면 그에 맞는 한국 노래 한 곡만 추천
- 화려한 UI: 카드 스타일, 색상, 버튼, 이모지 적용
"""

import random
import streamlit as st

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(page_title="기분 음악 추천기", page_icon="🎵", layout="centered")

# -------------------------------
# 데이터: 기분별 한국 노래 (가수 + 노래 제목 + 색상 + 이모지)
# -------------------------------
MOOD_MUSIC = {
    "😀 행복": {
        "songs": [
            ("아이유", "좋은 날"),
            ("BTS", "Dynamite"),
            ("레드벨벳", "빨간 맛"),
            ("트와이스", "Cheer Up"),
            ("방탄소년단", "Permission to Dance"),
        ],
        "color": "#FFF176",
        "emoji": "😀"
    },
    "😢 슬픔": {
        "songs": [
            ("태연", "사계"),
            ("폴킴", "모든 날, 모든 순간"),
            ("백예린", "그건 아마 우리의 잘못은 아닐 거야"),
            ("아이유", "사랑이 잘"),
            ("벤", "열애중"),
        ],
        "color": "#64B5F6",
        "emoji": "😢"
    },
    "😡 분노": {
        "songs": [
            ("방탄소년단", "MIC Drop"),
            ("지코", "Any Song"),
            ("다이나믹 듀오", "BAAAM"),
        ],
        "color": "#E57373",
        "emoji": "😡"
    },
    "😌 차분": {
        "songs": [
            ("아이유", "밤편지"),
            ("악동뮤지션", "오랜 날 오랜 밤"),
            ("헤이즈", "비도 오고 그래서"),
            ("적재", "별 보러 가자"),
        ],
        "color": "#81C784",
        "emoji": "😌"
    },
    "🤩 신남": {
        "songs": [
            ("싸이", "That That (feat. SUGA)"),
            ("세븐틴", "아주 NICE"),
            ("NCT 127", "Kick It"),
            ("ITZY", "WANNABE"),
        ],
        "color": "#FFD54F",
        "emoji": "🤩"
    },
    "😴 피곤": {
        "songs": [
            ("백예린", "밤하늘의 별을"),
            ("악동뮤지션", "오랜 날 오랜 밤"),
            ("아이유", "이 지금"),
            ("케이시", "그때가 좋았어"),
        ],
        "color": "#B39DDB",
        "emoji": "😴"
    },
    "🎯 집중": {
        "songs": [
            ("아이유", "무릎"),
            ("검정치마", "EVERYTHING"),
            ("새소년", "단풍"),
        ],
        "color": "#4FC3F7",
        "emoji": "🎯"
    },
}

# -------------------------------
# UI
# -------------------------------
st.title("🎵 화려한 기분별 한국 노래 추천기")
st.caption("기분에 맞는 한국 노래 한 곡을 카드 스타일로 추천합니다.")

mood = st.selectbox("지금 기분을 선택하세요", list(MOOD_MUSIC.keys()))

if mood:
    mood_info = MOOD_MUSIC[mood]
    songs = mood_info["songs"]
    color = mood_info["color"]
    emoji = mood_info["emoji"]

    if st.button("🎶 노래 추천 받기"):
        choice = random.choice(songs)
        artist, title = choice
        st.markdown(f"<div style='background-color:{color}; padding:20px; border-radius:15px; text-align:center'>\n<h2>{emoji} {title} — {artist} {emoji}</h2>\n</div>", unsafe_allow_html=True)

# -------------------------------
# 팁
# -------------------------------
st.divider()
st.markdown(
    """
**Tips**
- 🎶 `MOOD_MUSIC` 딕셔너리에 원하는 노래와 가수를 더 추가할 수 있어요.
- 🔀 ‘노래 추천 받기’ 버튼을 눌러 매번 새로운 곡을 무작위로 추천받을 수 있습니다.
"""
)
