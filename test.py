
"""
Streamlit YouTube Recommender — Basic Starter

▶ 기능
- 키워드를 선택하면 관련 유튜브 영상을 추천합니다.
- (선택) YouTube Data API v3를 연결하면 실시간 검색 결과를 사용합니다.
- API 키가 없으면 미리 준비된 샘플 데이터로 동작합니다.

▶ 준비
1) `pip install streamlit requests`
2) (선택) 구글 클라우드 콘솔에서 YouTube Data API v3 키 발급 후 .env 또는 환경변수로 설정
   - Windows: set YOUTUBE_API_KEY=YOUR_KEY
   - macOS/Linux: export YOUTUBE_API_KEY=YOUR_KEY
3) 실행: `streamlit run app.py`
"""

import os
import random
import textwrap
from typing import List, Dict

import requests
import streamlit as st

# -------------------------------
# 기본 설정
# -------------------------------
st.set_page_config(page_title="YouTube 추천기", page_icon="🎬", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []  # [(keyword, video_url)]

# -------------------------------
# 키워드 & 샘플 데이터 (API 없을 때 사용)
# -------------------------------
DEFAULT_KEYWORDS = [
    "공부 음악", "운동 루틴", "요리 레시피", "코딩 튜토리얼", "스트레스 해소", "명상", "스트림릿", "MBTI", "마케팅", "여행 브이로그",
]

SAMPLE_VIDEOS: Dict[str, List[str]] = {
    "공부 음악": [
        "https://www.youtube.com/watch?v=jfKfPfyJRdk",
        "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "https://www.youtube.com/watch?v=DWcJFNfaw9c",
    ],
    "운동 루틴": [
        "https://www.youtube.com/watch?v=UItWltVZZmE",
        "https://www.youtube.com/watch?v=2MoGxae-zyo",
    ],
    "요리 레시피": [
        "https://www.youtube.com/watch?v=8l2MZk3K6i8",
        "https://www.youtube.com/watch?v=ZLZqV6Zp2BU",
    ],
    "코딩 튜토리얼": [
        "https://www.youtube.com/watch?v=JwSS70SZdyM",
        "https://www.youtube.com/watch?v=VqgUkExPvLY",
        "https://www.youtube.com/watch?v=t4mwF-6fakw",
    ],
    "스트레스 해소": [
        "https://www.youtube.com/watch?v=aW8BDgLpZkI",
        "https://www.youtube.com/watch?v=8lpj47jZHgA",
    ],
    "명상": [
        "https://www.youtube.com/watch?v=inpok4MKVLM",
        "https://www.youtube.com/watch?v=ZToicYcHIOU",
    ],
    "스트림릿": [
        "https://www.youtube.com/watch?v=Yk-unX4KnV4",
        "https://www.youtube.com/watch?v=VqgUkExPvLY",
    ],
    "MBTI": [
        "https://www.youtube.com/watch?v=jCsdxw3P3DU",
        "https://www.youtube.com/watch?v=8r8FQK-2WSI",
    ],
    "마케팅": [
        "https://www.youtube.com/watch?v=2Z1Q5-7qDkA",
        "https://www.youtube.com/watch?v=3WbB5r9n1sg",
    ],
    "여행 브이로그": [
        "https://www.youtube.com/watch?v=5xF3j4nX3kg",
        "https://www.youtube.com/watch?v=Hk4tZ2D2s6E",
    ],
}

# -------------------------------
# 유틸
# -------------------------------

def extract_video_id(url: str) -> str:
    """유튜브 URL에서 videoId를 추출합니다."""
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return url

@st.cache_data(show_spinner=False)
def search_youtube(query: str, max_results: int = 6) -> List[str]:
    """YouTube Data API v3를 사용해 검색. API 키가 없으면 샘플 데이터로 대체."""
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        # 샘플 데이터로 fallback
        pool = SAMPLE_VIDEOS.get(query, [])
        if not pool:  # 없으면 유사 키워드에서 섞어주기
            for k, urls in SAMPLE_VIDEOS.items():
                if query in k or k in query:
                    pool += urls
        return random.sample(pool, k=min(len(pool), max_results)) if pool else []

    # 실제 API 호출
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": api_key,
        "regionCode": "KR",
        "relevanceLanguage": "ko",
        "safeSearch": "moderate",
    }
    try:
        r = requests.get("https://www.googleapis.com/youtube/v3/search", params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        ids = [item["id"]["videoId"] for item in data.get("items", [])]
        return [f"https://www.youtube.com/watch?v={vid}" for vid in ids]
    except Exception as e:
        st.warning(f"API 검색 중 오류가 발생하여 샘플 데이터로 대체합니다. (사유: {e})")
        pool = SAMPLE_VIDEOS.get(query, [])
        return random.sample(pool, k=min(len(pool), max_results)) if pool else []


# -------------------------------
# 사이드바
# -------------------------------
with st.sidebar:
    st.header("🔎 검색 옵션")
    st.markdown("API 키를 설정하면 더 다양한 실시간 결과를 볼 수 있어요.")
    keywords = st.multiselect("키워드 선택", DEFAULT_KEYWORDS, default=[DEFAULT_KEYWORDS[0]])
    max_results = st.slider("추천 개수", 1, 12, 6)
    shuffle = st.toggle("결과 섞기", value=True)
    show_titles = st.toggle("영상 제목 표시", value=True)

    st.divider()
    st.subheader("➕ 키워드 직접 추가")
    new_kw = st.text_input("원하는 키워드를 입력하세요", placeholder="예: lo-fi, 수학 공부, python")
    add_btn = st.button("추가")
    if add_btn and new_kw:
        if new_kw not in DEFAULT_KEYWORDS:
            DEFAULT_KEYWORDS.append(new_kw)
        if new_kw not in keywords:
            keywords.append(new_kw)
        st.success(f"'{new_kw}' 키워드를 추가했어요!")

# -------------------------------
# 본문 UI
# -------------------------------
st.title("🎬 키워드 기반 유튜브 추천기")
st.caption("키워드를 고르면 관련 영상을 추천해 드려요. API 없이도 샘플 데이터로 바로 실행 가능!")

if not keywords:
    st.info("왼쪽 사이드바에서 키워드를 하나 이상 선택하거나 추가하세요.")
    st.stop()

results: List[str] = []
for kw in keywords:
    urls = search_youtube(kw, max_results=max_results)
    if shuffle:
        random.shuffle(urls)
    results.extend([(kw, u) for u in urls])

# 중복 제거 (동일 URL)
seen = set()
unique_results = []
for kw, url in results:
    if url not in seen:
        seen.add(url)
        unique_results.append((kw, url))

# 히스토리 업데이트
for item in unique_results:
    if item not in st.session_state.history:
        st.session_state.history.append(item)

# -------------------------------
# 결과 표시
# -------------------------------
cols_per_row = 3
cols = st.columns(cols_per_row)

if unique_results:
    st.subheader("추천 영상")
    for i, (kw, url) in enumerate(unique_results):
        col = cols[i % cols_per_row]
        with col:
            vid = extract_video_id(url)
            if show_titles:
                st.markdown(f"**#{i+1}. {kw}**")
            st.video(f"https://www.youtube.com/watch?v={vid}")
else:
    st.warning("검색 결과가 없어요. 다른 키워드를 시도해 보세요.")

# -------------------------------
# 히스토리 & 유틸
# -------------------------------
with st.expander("⏱️ 최근 추천 히스토리"):
    if st.session_state.history:
        for idx, (kw, url) in enumerate(reversed(st.session_state.history[-30:]), 1):
            st.markdown(f"{idx}. **{kw}** — {url}")
        if st.button("히스토리 초기화"):
            st.session_state.history = []
            st.experimental_rerun()
    else:
        st.caption("아직 히스토리가 없습니다.")

st.divider()
st.markdown(
    textwrap.dedent(
        """
        **Tips**
        - 🔐 실시간 검색을 원하면 환경변수 `YOUTUBE_API_KEY`를 설정하세요.
        - 🧩 기본 키워드/샘플 목록은 코드의 `DEFAULT_KEYWORDS`, `SAMPLE_VIDEOS`에서 수정할 수 있어요.
        - 🧹 API 에러 시 자동으로 샘플 데이터로 대체됩니다.
        - 💡 그리드/정렬/필터 등 UI를 더 강화하고 싶다면 `st.data_editor`, `st.tabs`를 활용해 보세요.
        """
    )
)

