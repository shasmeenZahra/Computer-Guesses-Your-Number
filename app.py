import streamlit as st

st.title("🤖 Computer Guesses Your Number!")
st.write("Think of a number between 1 and 100, and I will try to guess it!")

if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.attempts = 0
    st.session_state.message = "Is this your number?"

st.subheader(f"Is your number {st.session_state.guess}?")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔼 Too Low"):
        st.session_state.low = st.session_state.guess + 1
        st.session_state.attempts += 1

with col2:
    if st.button("✅ Correct!"):
        st.success(f"🎉 Yay! I guessed your number in {st.session_state.attempts} attempts.")
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts = 0
        st.stop()

with col3:
    if st.button("🔽 Too High"):
        st.session_state.high = st.session_state.guess - 1
        st.session_state.attempts += 1

if st.session_state.low <= st.session_state.high:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
else:
    st.error("Oops! Something went wrong. Please restart the game.")

