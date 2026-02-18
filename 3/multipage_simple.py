import streamlit as st

# This message is always displayed
st.write("Welcome message")

# define functions for what each page displays
def my_first_page():
    st.write("my first page")
def my_second_page():
    st.write("my second page")

# define dictionary for what is in the selection box
page_names_to_funcs = {
    "First Page": my_first_page,
    "Second Page": my_second_page
}

# define the selection box  (default is "First Page")
demo_name = st.sidebar.selectbox(
    "Choose a page", 
    page_names_to_funcs.keys()
)

# only run a function if the user has selected that page
if demo_name == "First Page":
    my_first_page()
elif demo_name == "Second Page":
    my_second_page()
