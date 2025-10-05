import streamlit as st
import pandas as pd
import altair as alt
 
 #st.write sends to the app
st.write("""
# My first app
Hello *world!*
""")

#regular python
url = (
    "https://raw.githubusercontent.com/vega/vega-datasets/main/data/seattle-weather.csv"
)

weather = pd.read_csv(url, parse_dates=["date"])

chart_to_show = (
    alt.Chart(weather)
    .mark_line()
    .encode(
        x="date:T",
        y=alt.Y("temp_max:Q", title="Max temperature (°C)"),
        tooltip=["date:T", "temp_max:Q"],
    )
)

#st.altair_chart(chart_to_show)
