# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:39:58 2022

@author: student
"""

import pandas as pd
import streamlit as st
import numpy as np
st.title("Welcome to Data Visualization!")


if st.button('Hello'):
    st.write('Generate insights from data, Communicate insights, Work with data visualization tools')


st.header("Hospitals in Lebanon")

import plotly.express as px
df= pd.read_csv("C:/Users/student/Desktop/Hospitals and Beds in Lebanon - 18 April 2021.csv")
fig= px.histogram(df, x="Location", y="Number of Beds")
st.plotly_chart(fig)

df= pd.read_csv("C:/Users/student/Desktop/Hospitals and Beds in Lebanon - 18 April 2021.csv")
fig1 = px.bar(df, x="Hospital", y="Number of Beds",
  animation_frame="Date of Establishment")
st.plotly_chart(fig1)

df= pd.read_csv("C:/Users/student/Desktop/Hospitals and Beds in Lebanon - 18 April 2021.csv")
fig2 = px.bar(df, x="Location", y="Number of Beds", color="Hospital")
st.plotly_chart(fig2)

st.header("Covid-19 cases")
df= pd.read_csv("C:\\Users\\student\\Desktop\\covid-vaccination-vs-death_ratio.csv")
fig3= px.scatter(df, x="people_vaccinated", y="New_deaths", animation_frame="date", animation_group="country", color="country", hover_name="country", size="population", size_max= 30, log_x= True)
st.plotly_chart(fig3)

df= pd.read_csv("C:\\Users\\student\\Desktop\\covid-vaccination-vs-death_ratio.csv")
fig4= px.bar(df, x="country", y="total_vaccinations", color="country",
  animation_frame="date", animation_group="country", range_y=[0,100000000])
st.plotly_chart(fig4)


agree = st.checkbox('I liked the visualization')

if agree:
    st.write('Thank you!')
