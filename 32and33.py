import streamlit as st
import plotly.express as pe
from backend import get_data

#add title,textinput slider,selectbox and subheader

st.header("weather app")
st.title("weather forecast for the next days")
place=st.text_input(label="place:",placeholder="add place")
days=st.slider("forecast days",min_value=1,max_value=5,help="select the number of the days in forecast")
option=st.selectbox("select the view",
                    ("Temperature","sky"))
st.subheader(f"{option} for the next{days} days in {place} ")

#get  the temp and sky and date
if place:
    try:
        filter_d=get_data(place,days)

        if option=="Temperature":
            temp=[dict["main"]["temp"]/10 for dict in filter_d]
            dates=[dict["dt_txt"]for dict in filter_d]
            line=pe.line(x=dates,y=temp,labels={'x':"date","y":"temp(c)"})
            st.plotly_chart(line)

        if option=="sky":
            images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            sky=[dict["weather"][0]["main"] for dict in filter_d]
            image_path=[images[condition] for condition in sky]
            print(sky)
            st.image(image_path,width=100)

    except KeyError:
        st.write("this place does not exits enter valid place")