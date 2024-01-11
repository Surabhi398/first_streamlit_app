import streamlit

streamlit.title('My parents new Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🍝Omega 3 And Blueberry Omlet')
streamlit.text('🥞Banana Pancakes')
streamlit.text('🧉Kale, Spinach & Rocket Smoothie')
streamlit.text('🥪Egg Sandwich')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
