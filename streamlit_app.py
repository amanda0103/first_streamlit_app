import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('BREAKFAST MENU')
streamlit.text(' 🥣Omega 3 and blueberry oatmeal')
streamlit.text('🥗Kale,Spinach and Rocket Smoothie')
streamlit.text('🐔Hard-boiled free-ranged eggs')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)



