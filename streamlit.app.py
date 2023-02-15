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

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())

# get the json values and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as table
streamlit.dataframe(fruityvice_normalized)
# do not do anything beyond this line
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION(), CURRENT_ROLE(), CURRENT_DATABASE(), CURRENT_SCHEMA()")
my_cur.execute("select * from FRUIT_LOAD_LIST")

#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

#add_my_fruit = "insert into pc_rivery_db.public.fruit_load_list values ('" + fruit_choice + "')"
#my_cur.execute(add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from Streamlit')")
