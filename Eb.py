import streamlit as st

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="기분 음악 추천기", page_icon="🎵", layout="centered")

# -------------------- CSS 스타일 --------------------
st.markdown("""
    <style>
    .title {
        font-size:32px;
        font-weight:bold;
        color:#4B9CD3;
        text-align:center;
        margin-bottom:20px;
    }
    .card {
        background-color:#f0f8ff;
        padding:15px;
        border-radius:12px;
        margin:10px 0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        font-size:18px;
    }
    .mood-happy {background-color:#FFFACD;}
    .mood-sad {background-color:#ADD8E6;}
    .mood-angry {background-color:#F08080;}
    .mood-calm {background-color:#E0FFFF;}
    </style>
""", unsafe_allow_html=True)

# -------------------- 제목 --------------------
st.markdown("<div class='title'>🎵 오늘의 기분에 맞는 음악 추천기 🎵</div>", unsafe_allow_html=True)
st.write("현재 기분을 선택하면, 당신에게 딱 맞는 음악을 추천해드려요!")

# -------------------- 기분 선택 --------------------
mood = st.radio(
    "오늘 기분은 어떤가요?",
    ["😊 즐거움", "😢 슬픔", "😡 스트레스", "😴 편안함"]
)

# -------------------- 기분별 추천곡 데이터 --------------------
music = {
    "😊 즐거움": [
        {"title": "Happy - Pharrell Williams", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
        {"title": "Can't Stop The Feeling - Justin Timberlake", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"}
    ],
    "😢 슬픔": [
        {"title": "Someone Like You - Adele", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
        {"title": "All of Me - John Legend", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"}
    ],
    "😡 스트레스": [
        {"title": "Eye of the Tiger - Survivor", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"},
        {"title": "Stronger - Kanye West", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"}
    ],
    "😴 편안함": [
        {"title": "Clair de Lune - Debussy", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"},
        {"title": "Weightless - Marconi Union", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"}
    ]
}

# -------------------- 배경색 매칭 --------------------
mood_class = {
    "😊 즐거움": "mood-happy",
    "😢 슬픔": "mood-sad",
    "😡 스트레스": "mood-angry",
    "😴 편안함": "mood-calm"
}[mood]

# -------------------- 추천곡 출력 --------------------
st.subheader(f"🎧 추천 음악 ({mood})")
for song in music[mood]:
    st.markdown(f"<div class='card {mood_class}'>{song['title']}</div>", unsafe_allow_html=True)
    st.audio(song['url'], format="audio/mp3")
