import streamlit as st
import pandas
from send_email import send_email

topics = pandas.read_csv('topics.csv')
topics_loaded = []
for index, item in topics.iterrows():
    topics_loaded.append(item["topic"])

with st.form('contact'):
    email = st.text_input("Your Email Address")
    select_topic = st.selectbox("What topic do you want to discuss?", topics_loaded)
    message_raw = st.text_area("Text")
    submit = st.form_submit_button("Submit")
    if submit:
        message = f"Subject: New Email from {email} on Company Page.\nTopic - {select_topic}\n\nMessage: {message_raw}"
        send_email(message)
        st.info("Your email was sent successfully.")