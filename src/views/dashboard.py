import streamlit as st
import pandas as pd
import numpy as np
from authentication import session_handler
import plotly.express as px

import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation

# import plotly.express as px  # interactive charts
import streamlit as st
from PIL import Image
# st.set_page_config(layout="wide", page_title="Charging Behaviour", page_icon="🔋")



@session_handler
def main():
        
        st.title("Customers Insight Regarding the charging")
        st.write(
                """
                Here We will find out User start charging from what per to what percent
                """
        )
        

        # read csv from a URL
        @st.cache_data
        def get_data() -> pd.DataFrame:
                return pd.read_csv(r"C:\Users\mohit\Desktop\demo\basic-auth-streamlit\src\views\data.csv")


        df = get_data()
        df.loc[(df["Customer City"].isnull() == True), "Customer City"] = "Pune"
        df["start1"] = pd.to_datetime(df["start"]).dt.date


        st.title("Customers Behaviour Dashboard")
        # city_filter = st.selectbox("Select the City", pd.unique(df["Customer City"]))
        options = st.multiselect(
                "Select the City", pd.unique(df["Customer City"]), pd.unique(df["Customer City"])
        )


        col1, col2 = st.columns(2)

        # In the first column, add the Start Date input
        with col1:
                start_date = st.date_input(
                "Start Date", value=pd.to_datetime("2021-01-01", format="%Y-%m-%d")
                )

        # In the second column, add the End Date input
        with col2:
                end_date = st.date_input(
                "End Date", value=pd.to_datetime("today", format="%Y-%m-%d")
                )

        # st.write('You selected:', options)

        df = df[df["Customer City"].isin(options)]
        df = df[(df["start1"] >= start_date) & (df["start1"] <= end_date)]
        if len(df)> 0:
                x = pd.pivot_table(
                df,
                values="s",
                index=["ChargeIn"],
                columns=["ChargeOut"],
                aggfunc=np.sum,
                margins=True,
                )
                x = ((x / x.iloc[-1, -1]) * 100).round(2)
                x[x.isnull() == True] = 0
                x = x.astype(str) + " %"
                x.index.names = ["ChargeIn/ChargeOut"]
                # styled_df = x.style.background_gradient( cmap='Greens')


                df["start"] = pd.to_datetime(df["start"]) + pd.Timedelta(hours=5, minutes=30)

                df["Hour"] = df["start"].astype("str").str[11:13].astype("int")
                bins = [0, 6, 12, 18, 23]
                label = ["0-6", "6-12", "12-18", "18-24"]
                df["ChargingTime"] = pd.cut(df["Hour"], bins, labels=label)
                # sns.countplot(df['ChargingTime'])

                gr = px.histogram(
                df,
                x="ChargingTime",
                barmode="group",
                category_orders=dict(ChargingTime=["0-6", "6-12", "12-18", "18-24"]),
                text_auto=True,
                )
                st.markdown("### Cutomers Start Charging Time")
                
                st.plotly_chart(gr, use_container_width=True)


                st.markdown("### Cutomers Start Charging Time Table")


                st.dataframe(x, height=450, use_container_width=True)
        else:
                st.markdown("# No Data")

