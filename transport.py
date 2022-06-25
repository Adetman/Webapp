#Import Streamlite

import pandas as pd
import streamlit as st

#Import Image
from PIL import Image

img = Image.open('logo.jpg')

st.image(img, width=200)

#Page Title
st.title('Welcome to Top Transport Company')

#Import Date and Time
import datetime

the_time = datetime.datetime.now().strftime('%y-%m-%d %H:%M')

st.write('Today is ' + str(the_time))

departure = {}
arrival = {}

user = st.sidebar.text_input('What is your name')

#Movement type
movement = ['Book a seat', 'Hire a bus', 'Check my booking Satus']
location = pd.read_csv("Nigeria.csv")
location.sort_values(by='Capital')

option = st.sidebar.radio('What do you want from us today ' + '?', movement)

if option == 'Book a seat':
    travel = ['One way', 'Round trip']
    trip = st.selectbox('Please select your trip', travel)
    if trip == 'One way':
        date = st.date_input('Departure Date')
        departure = st.selectbox('Your departure terminal is', location['Capital'])
        arrival = st.selectbox('Your arrival terminal is', location['Capital'])
        if departure == arrival:
            st.error('Your departure point cannot be same with your arrival point')
        if(st.button('Submit')):
            st.success('Thank you for Choosing Top Transport Company, Dear ' + str(user.upper()))
    
    else:
        #First movement
        departure_date = st.date_input('Departure Date')
        departure1 = st.selectbox('Your departure terminal is', location['Capital'])
        arrival1 = st.selectbox('Your arrival terminal is', location['Capital'])
        if departure1 == arrival1:
            st.error('Your departure point cannot be same with your arrival point')
        else:
            st.info('Your next departure terminal is ' + str(arrival1))
        return_date = st.date_input('Return Date')
        
        if(st.button('Submit')):
            st.success('Thank you for Choosing Top Transport Company, Dear ' + str(user.upper()))

elif option == 'Hire a bus':
    date = st.date_input('Departure Date')
    st.number_input('How many days hire do you need?')
    destination = st.selectbox('Please enter your destination?', location['Capital'])
    st.info('You have chosen, ' + str(destination))
    st.text_area('Please provide further details and contacts')
    if(st.button('Submit')):
        st.success('Thank you for Choosing Top Transport Company, Dear ' + str(user.upper()))

else:
    st.text_input('Please enter your name to check the status of your booking')
    if(st.button('Submit')):
        st.success("Your booking is confirmed.  \nThank you for Choosing Top Transport Company, Dear " + str(user.upper()))
    
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
