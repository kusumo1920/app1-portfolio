import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    user_message = f"Subject: New Message from Kesit's Personal Website\n\n" \
                   f"From: {user_email}\n" \
                   f"{user_message}"
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(user_message)
        st.info("Your message was sent successfully!")
