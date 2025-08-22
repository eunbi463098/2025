"""
Streamlit Mood-based Music Recommender — Basic Starter

▶ 기능
- 사용자가 기분을 선택하면 그에 맞는 음악(유튜브 링크)을 추천합니다.
- 기분: 행복 😀, 슬픔 😢, 분노 😡, 차분 😌, 신남 🤩, 피곤 😴, 집중 🎯

▶ 준비
1) `pip install streamlit`
2) 실행: `streamlit run app.py`
"""

import random
import streamlit as st

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(page_title="기분 음악 추천기", page_icon="🎵", layout="centered")

# -------------------------------
# 데이터: 기분별 유튜브 음악 링크
# -------------------------------
MOOD_MUSIC = {
    "😀 행복": [
        "https://www.youtube.com/watch?v=9bZkp7q19f0",  # 강남스타일
        "https://www.youtube.com/watch?v=KQetemT1sWc",  # Pharrell Williams - Happy
    ],
    "😢 슬픔": [
        "https://www.youtube.com/watch?v=RB-RcX5DS5A",  # Adele - Someone Like You
        "https://www.youtube.com/watch?v=YQHsXMglC9A",  # Adele - Hello
    ],
    "😡 분노": [
        "https://www.youtube.com/watch?v=eVTXPUF4Oz4",  # Linkin Park - In the End
        "https://www.youtube.com/watch?v=2vjPBrBU-TM",  # Sia - Chandelier
    ],
    "😌 차분": [
        "https://www.youtube.com/watch?v=2OEL4P1Rz04",  # Relaxing piano
        "https://www.youtube.com/watch?v=1ZYbU82GVz4",  # Meditation music
    ],
    "🤩 신남": [
        "https://www.youtube.com/watch?v=JGwWNGJdvx8",  # Ed Sheeran - Shape of You
        "https://www.youtube.com/watch?v=3tmd-ClpJxA",  # Maroon 5 - Sugar
    ],
    "😴 피곤": [
        "https://www.youtube.com/watch?v=s2aAqXGlZrs",  # Sleep music
        "https://www.youtube.com/watch?v=1ZYbU82GVz4",  # Soft piano
    ],
    "🎯 집중": [
        "https://www.youtube.com/watch?v=jfKfPfyJRdk",  # Lofi hip hop
        "https://www.youtube.com/watch?v=5qap5aO4i9A",  # Lofi girl
    ],
}

# -------------------------------
# UI
# -------------------------------
st.title("🎵 기분별 음악 추천기")
st.caption("당신의 기분에 맞는 음악을 추천해 드려요!")

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
st.markdown("""
**Tips**
- 🎶 `MOOD_MUSIC` 딕셔너리에 원하는 음악 유튜브 링크를 더 추가할 수 있어요.
- 🔀 매번 다른 음악을 듣고 싶으면 `random.choice` 대신 `random.shuffle`을 써서 여러 곡을 보여줄 수 있어요.
- 🧩 더 발전시키려면 Spotify API, YouTube Data API를 연동할 수도 있습니다.
""")
