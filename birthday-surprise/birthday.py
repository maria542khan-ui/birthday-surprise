import time
import streamlit as st

st.set_page_config(page_title="Happy Birthday My Love 💖", page_icon="💍", layout="centered")

st.markdown("""
<style>
body, .stApp {
    background: radial-gradient(circle at top, #360b2e, #0d020d);
    color: #ffe6f2;
    overflow-x: hidden;
}
@keyframes floatGirl {
    0%, 100% { transform: translateY(0px) rotate(-4deg); }
    50% { transform: translateY(-15px) rotate(4deg); }
}
@keyframes twinkle {
    0%, 100% { opacity: 0.25; transform: scale(0.85); }
    50% { opacity: 1; transform: scale(1.25); }
}
.girl-box {
    text-align: center;
    font-size: 85px;
    animation: floatGirl 2.2s ease-in-out infinite;
    margin-top: 10px;
}
.stars {
    text-align: center;
    font-size: 24px;
    letter-spacing: 12px;
    animation: twinkle 1.4s infinite alternate;
    color: #ffb3d9;
}
.msg-box {
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #ff66b2;
    text-shadow: 0 0 14px #ff1a8c;
    margin: 18px 0 8px 0;
}
.sub-note {
    text-align: center;
    font-size: 18px;
    font-style: italic;
    color: #ffd6eb;
    margin-bottom: 24px;
}
.tease-text {
    text-align: center;
    font-size: 16px;
    color: #ff99cc;
    margin-bottom: 10px;
}
.letter-card {
    background: rgba(255, 102, 178, 0.12);
    border: 2px solid #ff66b2;
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 0 25px rgba(255, 26, 140, 0.35);
    text-align: center;
    font-size: 18px;
    line-height: 1.7;
    color: #fff0f6;
}
</style>
""", unsafe_allow_html=True)

if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if "page" not in st.session_state:
    st.session_state.page = "card"
if "typed" not in st.session_state:
    st.session_state.typed = False

if st.session_state.page == "card":
    st.markdown('<div class="stars">✨ 💍 💖 ✨ 🌟 💖 💍 ✨</div>', unsafe_allow_html=True)
    st.markdown('<div class="girl-box">👧🏻🎀😘<br><span style="font-size:38px;">👗💕✨</span></div>', unsafe_allow_html=True)

    message = "Happy Birthday to my future fiancé! I love you endlessly! 💖"
    placeholder = st.empty()
    if not st.session_state.typed:
        current = ""
        for ch in message:
            current += ch
            placeholder.markdown(f'<div class="msg-box">{current}</div>', unsafe_allow_html=True)
            time.sleep(0.06)
        st.session_state.typed = True
    else:
        placeholder.markdown(f'<div class="msg-box">{message}</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="sub-note">"Every day with you feels like a dream, and I can’t wait for our forever together."</div>',
        unsafe_allow_html=True
    )

    teases = [
        "Catch the button for your surprise! 😉",
        "Too slow! Try over here! 😜💕",
        "Almost got it! One more try! 😘",
        "Okay, you caught me! Open your surprise 👇"
    ]
    st.markdown(f'<div class="tease-text">{teases[st.session_state.clicks]}</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    if st.session_state.clicks == 0:
        with cols[0]:
            if st.button("Next ➡️"):
                st.session_state.clicks += 1
                st.rerun()
    elif st.session_state.clicks == 1:
        with cols[2]:
            if st.button("Next ➡️"):
                st.session_state.clicks += 1
                st.rerun()
    elif st.session_state.clicks == 2:
        with cols[1]:
            if st.button("Next ➡️"):
                st.session_state.clicks += 1
                st.rerun()
    else:
        with cols[1]:
            if st.button("💍 Open Your Surprise 💍"):
                st.session_state.page = "letter"
                st.balloons()
                st.rerun()

elif st.session_state.page == "letter":
    st.markdown('<div class="stars">✨ 🎂 💖 Happy Birthday My Husband 💖 🎂 ✨</div>', unsafe_allow_html=True)
    st.markdown('<div class="msg-box">A Special Note Just For You 💌</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="letter-card">
        <b>To the love of my life,</b><br><br>
        Happy Birthday! 🎉 On your special day, I just want to remind you how deeply I love you and how grateful I am to have you in my life.<br><br>
        ✨ You are my favorite person to talk to<br>
        💖 You make me feel safe, happy, and loved every single day<br>
        💍 I can’t wait for all the birthdays we will celebrate together in our future<br><br>
        May all your dreams come true this year. I love you forever and always! 😘❤️
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅️ Replay From the Start"):
        st.session_state.clicks = 0
        st.session_state.typed = False
        st.session_state.page = "card"
        st.rerun()
