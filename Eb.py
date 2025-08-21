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
    padding:15px;
    border-radius:12px;
    margin:10px 0;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    font-size:18px;
}
.mood-happy {background-color:#FFFACD;}       /* 즐거움 */
.mood-sad {background-color:#ADD8E6;}         /* 슬픔 */
.mood-angry {background-color:#F08080;}       /* 화남 */
.mood-calm {background-color:#E0FFFF;}        /* 편안함 */
.mood-love {background-color:#FFC0CB;}        /* 사랑 */
.mood-cool {background-color:#B0E0E6;}        /* 자신감 */
.mood-anxious {background-color:#F5DEB3;}     /* 불안 */
.mood-focus {background-color:#D8BFD8;}       /* 집중 */
.mood-extremesad {background-color:#9370DB;}  /* 극도로 슬픔 */
.mood-peace {background-color:#98FB98;}       /* 평온 */
</style>
""", unsafe_allow_html=True)

# -------------------- 제목 --------------------
st.markdown("<div class='title'>🎵 오늘의 기분에 맞는 음악 추천기 🎵</div>", unsafe_allow_html=True)
st.write("현재 기분을 선택하면, 당신에게 딱 맞는 음악을 추천해드려요!")

# -------------------- 기분 선택 --------------------
mood = st.radio(
    "오늘 기분은 어떤가요?",
    [
        "😊 즐거움", "😢 슬픔", "😡 화남/스트레스", "😴 편안함", 
        "😍 사랑", "😎 자신감", "😰 불안", "🤔 집중", 
        "😭 극도로 슬픔", "😇 평온/만족"
    ]
)

# -------------------- 기분별 추천곡 --------------------
music = {
    "😊 즐거움": [{"title": "Happy - Pharrell Williams", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"}],
    "😢 슬픔": [{"title": "Someone Like You - Adele", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"}],
    "😡 화남/스트레스": [{"title": "Eye of the Tiger - Survivor", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"}],
    "😴 편안함": [{"title": "Clair de Lune - Debussy", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"}],
    "😍 사랑": [{"title": "Perfect - Ed Sheeran", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"}],
    "😎 자신감": [{"title": "Can't Hold Us - Macklemore", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"}],
    "😰 불안": [{"title": "Weightless - Marconi Union", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"}],
    "🤔 집중": [{"title": "Study Music Alpha Waves", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"}],
    "😭 극도로 슬픔": [{"title": "Fix You - Coldplay", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"}],
    "😇 평온/만족": [{"title": "River Flows in You - Yiruma", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"}],
}

# -------------------- 기분 클래스 매칭 --------------------
mood_class = {
    "😊 즐거움": "mood-happy",
    "😢 슬픔": "mood-sad",
    "😡 화남/스트레스": "mood-angry",
    "😴 편안함": "mood-calm",
    "😍 사랑": "mood-love",
    "😎 자신감": "mood-cool",
    "😰 불안": "mood-anxious",
    "🤔 집중": "mood-focus",
    "😭 극도로 슬픔": "mood-extremesad",
    "😇 평온/만족": "mood-peace"
}[mood]

# -------------------- 추천곡 출력 --------------------
st.subheader(f"🎧 추천 음악 ({mood})")
for song in music[mood]:
    st.markdown(f"<div class='card {mood_class}'>{song['title']}</div>", unsafe_allow_html=True)
    st.audio(song['url'], format="audio/mp3")
