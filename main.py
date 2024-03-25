import streamlit as st
import pandas

st.title("The Best Company")
description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Nam at lectus urna duis convallis 
convallis. Ultrices dui sapien eget mi proin sed libero enim.
"""
st.write(description)

st.header("Our Team")
col1, col2, col3 = st.columns(3)

data = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in data[0:4].iterrows():
        st.header(row["first name"], row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index, row in data[4:8].iterrows():
        st.header(row["first name"], row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])


with col3:
    for index, row in data[8:12].iterrows():
        st.header(row["first name"], row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])