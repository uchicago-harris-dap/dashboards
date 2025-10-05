import streamlit as st
import time

st.title("Expensive Calculation Demo")

# user inputs
route = st.selectbox("CTA route to cut", ["Red Line", "Blue Line", "Green Line"])
cut_pct = st.slider("What fraction of service to cut?", 0.0, 50.0, 10.0, step=5.0)

# session_state key
key = f"n_pass_{route}_{cut_pct}"

# run the heavy job only if we haven't already stored it
if key not in st.session_state:
    with st.spinner("Crunching numbers..."):
        time.sleep(3)  # stand‑in for a slow computation
        st.session_state[key] = (100 - cut_pct) * 1.2345  # fake result

st.metric("Expected number of passengers per trip", f"{st.session_state[key]:.2f}")
st.write("Session state keys (programmer tool, would not normally be shown to users):", list(st.session_state.keys()))
