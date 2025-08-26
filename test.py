"""
Streamlit Mood-based Music Recommender - 심플 한국 노래 추천기

▶ 기능
- 사용자가 기분을 선택하면 그에 맞는 한국 노래 한 곡만 바로 추천
- 심플하고 깔끔한 UI
"""

import random
import streamlit as st

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(page_title="기분 음악 추천기", page_icon="🎵", layout="centered")

# -------------------------------
# 데이터: 기분별 한국 노래 (가수 + 노래 제목)
# -------------------------------
MOOD_MUSIC = {
    "😀 행복": [
        ("아이유", "좋은 날"),
        ("BTS", "Dynamite"),
        ("레드벨벳", "빨간 맛"),
        ("트와이스", "Cheer Up"),
        ("방탄소년단", "Permission to Dance"),
        ("RIIZE", "Fly Up"),
    ],
    "😢 슬픔": [
        ("태연", "사계"),
        ("폴킴", "모든 날, 모든 순간"),
        ("백예린", "그건 아마 우리의 잘못은 아닐 거야"),
        ("아이유", "사랑이 잘"),
        ("벤", "열애중"),
    ],
    "😡 분노": [
        ("방탄소년단", "MIC Drop"),
        ("지코", "Any Song"),
        ("다이나믹 듀오", "BAAAM"),
        ("DAY6", "Shoot Me"),
    ],
    "😌 차분": [
        ("아이유", "밤편지"),
        ("아이유", "Love poem"),
        ("헤이즈", "비도 오고 그래서"),
        ("적재", "별 보러 가자"),
        ("폴킴", "모든 날 모든 순간"),
        ("이하이", "한숨"),
    ],
    "🤩 신남": [
        ("싸이", "That That (feat. SUGA)"),
        ("세븐틴", "아주 NICE"),
        ("NCT 127", "영웅(Kick It)"),
        ("ITZY", "WANNABE"),
    ],
    "😴 피곤": [
        ("백예린", "밤하늘의 별을"),
        ("악동뮤지션", "오랜 날 오랜 밤"),
        ("아이유", "이 지금"),
        ("케이시", "그때가 좋았어"),
    ],
    "🎯 집중": [
        ("아이유", "무릎"),
        ("검정치마", "EVERYTHING"),
        ("새소년", "단풍"),
        ("DAY6", "그렇더라고요"),
    ],
}

# -------------------------------
# UI
# -------------------------------
st.title("🎵 기분별 노래 추천")
st.caption("기분에 맞는 노래 한 곡을 바로 추천해드립니다.")

# 기분 선택
mood = st.selectbox("지금 기분을 선택하세요", list(MOOD_MUSIC.keys()))

if mood:
    songs = MOOD_MUSIC[mood]

    # 선택 즉시 추천
    artist, title = random.choice(songs)

    # 심플 카드 스타일
    st.markdown(
        f"""
        <div style="
            border: 1px solid #ccc;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            text-align: center;
            box-shadow: 1px 1px 8px rgba(0,0,0,0.08);
        ">
            <h2 style="margin:0; font-weight:600;">{title}</h2>
            <p style="margin:5px 0 0; font-size:18px; color:#555;">{artist}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------
# 팁
# -------------------------------
st.divider()
st.markdown(
    """
**Tips**
- 🎶 원하는 노래와 가수를 `MOOD_MUSIC` 딕셔너리에 더 추가할 수 있어요.
- 🎯 기분 선택만으로 바로 한 곡을 랜덤 추천받을 수 있습니다.
"""
)
