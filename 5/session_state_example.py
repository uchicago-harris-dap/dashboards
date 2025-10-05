import streamlit as st
import time

st.title("Expensive Calculation Demo")

# user inputs
route = st.selectbox("Route", ["Red Line", "Blue Line", "Green Line"])
cut_pct = st.slider("Cut percentage", 0.0, 50.0, 10.0, step=5.0)

# session_state key
key = f"util_{route}_{cut_pct}"

# run the heavy job only if we haven't already stored it
if key not in st.session_state:
    with st.spinner("Crunching numbers..."):
        time.sleep(3)  # stand‑in for a slow computation
        st.session_state[key] = (100 - cut_pct) * 1.2345  # fake result

st.metric("Projected utilization", f"{st.session_state[key]:.2f}")
st.write("Session state keys:", list(st.session_state.keys()))
