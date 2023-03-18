import streamlit as st


from authentication import user_authenticated
import streamlit as st

import os





def index():
    st.title("Customer's Behaviour with Kratos")
    st.write(
        """Here I am going to represent my findings with the Telematics historical data.
    It would helpful in finding the customer's behaviour Insight and will helpful in planing accordingly"""
    )
    st.markdown(
        """
        ### 💾 Index:
        **Page**|**Description**
        -----|-----
        |Charging Insight| Insights about when customer chargeIn and chargeOut|
        |Distance per Day| Average Distance Travelled per day|
        """
    )
    st.text("")
    st.markdown(
        """
            ### 💪 Challenge:
            ##### Here I am creating a report to summarizing my research including:
            - Avg charging time taken by customers for full charge in Pune, Mumbai, Nashik and Aurangabad (separate for each city)
            - Are customers charging full (i.e. say from 5% to 100%) or only incremental charging every time (i.e. say from 25% to 80%)
            - What time of the day the charging takes place (are people charging the most during day or nighttime?)
            - Avg daily k.m. run of customers in Pune, Mumbai, Nashik and Aurangabad (separate for each city)
            - Highest k.m. run so far in single charge in Pune, Mumbai, Nashik and Aurangabad (separate for each city)
            """
    )

def main():
    

    with st.form(key="welcome", clear_on_submit=True):
        with st.sidebar:
            st.markdown("# Welcome to Authentication")
            user = st.text_input("Username", value="")
            password = st.text_input("Password", value="", type="password")
            submitted = st.form_submit_button("LogIn")

    if submitted:
        result = user_authenticated(username=user, password=password)
        if result:
            st.sidebar.success("Logged in successfully!")
    index()
            
