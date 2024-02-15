import streamlit



streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Roket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)


#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

streamlit.header('Fruityvice Fruit Advance!')

import requests

#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")
#streamlit.text(fruityvice_response.json())

#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized):
   

#fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
#New selection to display fruityvice api response


def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "this_fruit_choice")
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())  
 return fruityvice_normalized
 #create the repeatable code block called a function
 streamlit.header('Fruityvice Fruit Advice')   
try:
#fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')

   fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
   
#streamlit.write('The user entered', fruit_choice)
if not fruit_choice:
  streamlit.error("Please select fruit to get information")
else:

back_from_function= get_fruityvice_data(fruit_choice)  
streamlit.dataframe(back_from_function)
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()
#streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like add?', 'Jackfruit')
my_cur.execute("insert into fruit_load_list values('fruit_choice')")
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("insert into fruit load list values('from streamlit')")
