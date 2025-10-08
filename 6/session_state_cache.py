import streamlit as st
import time


st.set_page_config(page_title="@cache_data")
st.title("Expensive Calculation Demo")

# user inputs
route = st.selectbox("CTA route to cut", ["Red Line", "Blue Line", "Green Line"])
cut_pct = st.slider("What fraction of service to cut?", 0.0, 50.0, 10.0, step=5.0)

if "counter" not in st.session_state:
    st.session_state.counter = 0

@st.cache_data()
def compute_passengers(route, cut_pct):
    with st.spinner("Crunching numbers..."):
        time.sleep(3)  # stand-in for a slow computation
    st.session_state.counter += 1
    return (100 - cut_pct) * 1.2345  # fake result
expected_passengers = compute_passengers(route, cut_pct)

st.metric("Expected number of passengers per trip", expected_passengers)

st.write(f"This page has run calculations {st.session_state.counter} times.")

