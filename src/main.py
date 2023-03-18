import streamlit as st
from PIL import Image
im = Image.open(r"C:\Users\mohit\Desktop\demo\basic-auth-streamlit\src\views\image.ico")
st.set_page_config(
                page_title="Tork Analytics",
                page_icon=im,
            )
from views import dashboard, welcome


RADIO_BUTTON_FACTORY = {
    "🚩 Welcome": {'func': welcome.main, 'activate': True},
    "🔋Charging Event ": {'func': dashboard.main, 'activate': True}
}


def run_app():
    active_sections = {key: value for key, value in RADIO_BUTTON_FACTORY.items() if value['activate']}
    st.sidebar.header(":open_book: Menu")
    option = st.sidebar.radio("", list(active_sections.keys()))
    func = active_sections[option]["func"]
    func()


if __name__ == "__main__":
    run_app()