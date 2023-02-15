import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


#import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
     #import requests
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    #streamlit.text(fruityvice_response.json())

    # get the json values and normalize it
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  #fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    #streamlit.write("The user entered ", fruit_choice)
    streamlit.write("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    # output as table
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

#import snowflake.connector
#streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")

#Snowflake related functions
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("select * from FRUIT_LOAD_LIST")          
          return  'Thanks for adding '+new_fruit
     
#add a button to load the fruit
if streamlit.button("Get Fruit Load List"):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = get_fruit_load_list()
     streamlit.dataframe(back_from_function)

# allow the end user to add fruit to the list
def insert_row_snowflake(new_fruit)
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from Streamlit')")
          return  my_cur.fetchall()

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button("Add a fruit to the list"):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_from_function)
     
  
