import streamlit as st
import plotly.express as px
# import matplotlib.pyplot as plt
import pandas as pd
import os
import logging
# import seaborn as sns
import streamlit as st
from django.core.wsgi import get_wsgi_application
# from sklearn.cluster import KMeans
import streamlit as st
import logging
import functools
import typing as t

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

from django.contrib.auth import authenticate


def add_auth_to_session():
    try:
        st.session_state["authenticated"] = True
    except Exception as e:
        logging.error(e)





def user_authenticated(username, password):
    """Returns `True` if the user had a correct password."""


    """Checks whether a password entered by the user is correct."""
    user = authenticate(
        username = username, password =password
    )

    if user is not None:
        st.session_state["password_correct"] = True
        
    else:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"] == True:
        add_auth_to_session()
        return True
    else:
        return False
    

def session_handler(func: t.Callable) -> t.Callable:
    generic_text = (
        "🚫 __You must have to authenticate yourself "
        "to view the content of the dashbaord. "
        "Please visit the welcome section and authenticate yourself.__"
    )
    @functools.wraps(func)
    def wrapper():
        if 'authenticated' in st.session_state and st.session_state['authenticated']:
            func()
        else:
            st.markdown(generic_text)
    return wrapper
