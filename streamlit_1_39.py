# Data process
import numpy as np
import datetime as dt
import pandas as pd
import polars as pl
import pyarrow as pa
import geopandas as gpd
from shapely.geometry import Point

# Data viz
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

import os
from scipy.io import wavfile
from shapely.geometry import Point, Polygon

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("What's new in Streamlit 1.39?")
st.divider()

with st.sidebar:
    st.image(path_cda + '\\logo.png')

#
#


# 1)
#---------------------------------------------------------------------------------------#
st.header(':one: Introducing st.experimental_audio_input to let users record with their microphones!')

cols = st.columns(2)

st.code('''
from scipy.io import wavfile
        
recording = st.experimental_audio_input('Record a voice message')

if recording:
    sample_rate, data = wavfile.read(recording)
    st.write(f'This recording was {len(data) / sample_rate}s long.')
''')

recording = st.experimental_audio_input('Record a voice message')

if recording:
    sample_rate, data = wavfile.read(recording)
    st.subheader(f'This recording was {len(data) / sample_rate}s long.')

st.divider()

# 2)
#---------------------------------------------------------------------------------------#
st.header(':two: st.pydeck_chart can return selection events!')

cols = st.columns(2)


st.code('''
import pydeck as pdk
        
m = pdk.Deck(...)

event = st.pydeck_chart(m, on_select="rerun", use_container_width=True)
        
selection_dict = event.selection

if len(selection_dict['objects'])>0:
    st.subheader(f"You have selected Point {selection_dict['objects']['id'][0]['id']}")

''')
pts = gpd.GeoDataFrame({
    'id' : ['A', 'B'],
    'geometry' : [Point(-122.4313, 37.7569),
                    Point(-122.4512, 37.7797)]
}, crs=4326)

poly = gpd.GeoDataFrame({
    'id': ['A'],
    'geometry': [Polygon([
        (-122.4251, 37.8013), (-122.4728, 37.7853),
        (-122.4227, 37.7493), (-122.4251, 37.8013)
    ])]
}, crs=4326)
m = pdk.Deck(layers=[pdk.Layer(
                        'ScatterplotLayer',
                        data=pts,
                        id="id",
                        get_position='geometry.coordinates',
                        get_radius=200,
                        pickable=True,
                        get_color="[255, 75, 75]"
                    )],
            initial_view_state=pdk.ViewState(longitude=-122.43825, latitude=37.75644, zoom=11), height=325, map_provider="carto", map_style=None, tooltip={"text": "Point {id}"})

cols = st.columns(2)
with cols[0]:
    event = st.pydeck_chart(m, on_select="rerun", use_container_width=True)

    selection_dict = event.selection

with cols[1]:
    if len(selection_dict['objects'])>0:
        st.subheader(f"You have selected *Point {selection_dict['objects']['id'][0]['id']}*")

        with st.expander('event.selection'):
            event.selection

st.divider()

# 3)
#---------------------------------------------------------------------------------------#
st.header(':three: st.button, st.download_button, st.form_submit_button, st.link_button, and st.popover each have a new parameter to add an icon.')

cols = st.columns(2)
cols[0].subheader('Streamlit 1.38')
cols[1].subheader('Streamlit 1.39')


with cols[0]:
    st.code('''
        st.button('Upload Data')
        st.download_button('Download Data', data='my_data')
    ''')
    st.button('Upload Data')
    st.download_button('Download Data', data='my_data')

with cols[1]:
    st.code('''
        st.button('Upload Data', icon=':material/upload:')
        st.download_button('Download Data', data='my_data', icon=':material/download:')
    ''')
    st.button('Upload Data', icon=':material/upload:')
    st.download_button('Download Data', data='my_data', icon=':material/download:')


st.divider()

# 4)
#---------------------------------------------------------------------------------------#
st.header(':four: st.navigation lets you display an always-expanded or collapsible menu using a new expanded parameter.')

cols = st.columns(2)
cols[0].subheader('Streamlit 1.38')
cols[1].subheader('Streamlit 1.39')

def page1():
    1+1
def page2():
    1+1
def page3():
    1+1
def page4():
    1+1
def page5():
    1+1
def page6():
    1+1
def page7():
    1+1
def page8():
    1+1
def page9():
    1+1
def page10():
    1+1
def page11():
    1+1
def page12():
    1+1
def page13():
    1+1
def page14():
    1+1
def page15():
    1+1



with cols[0]:
    st.code('''
        pg = st.navigation([st.Page(page1), ..., st.Page(page15)])
        pg.run()
    ''')

    if st.button('Create pages'):
        pg = st.navigation([st.Page(page1), st.Page(page2), st.Page(page3), st.Page(page4), st.Page(page5), st.Page(page6), st.Page(page7), st.Page(page8), st.Page(page9),
                            st.Page(page10), st.Page(page11), st.Page(page12), st.Page(page13), st.Page(page14), st.Page(page15)], expanded=True)
        pg.run()


with cols[1]:
    st.code('''
        pg = st.navigation([st.Page(page1), ..., st.Page(page15)], expanded=False)
        pg.run()
    ''')
    if st.button('Update pages'):
        pg = st.navigation([st.Page(page1), st.Page(page2), st.Page(page3), st.Page(page4), st.Page(page5), st.Page(page6), st.Page(page7), st.Page(page8), st.Page(page9),
                            st.Page(page10), st.Page(page11), st.Page(page12), st.Page(page13), st.Page(page14), st.Page(page15)], expanded=False)
        pg.run()


st.divider()


# 5)
#---------------------------------------------------------------------------------------#
st.header(':five: You can set height and width for st.map and st.pydeck_chart.')

cols = st.columns(2)
cols[0].subheader('Streamlit 1.38')
cols[1].subheader('Streamlit 1.39')


with cols[0]:
    st.code('''
    import pydeck as pdk

    m = pdk.Deck(...)
            
    st.pydeck_chart(m, use_container_width=True)
    ''')
    st.pydeck_chart(m, use_container_width=True)

with cols[1]:
    st.code('''
    import pydeck as pdk

    m = pdk.Deck(...)
            
    st.pydeck_chart(m, width=500, height=300)
    ''')
    st.pydeck_chart(m, width=500, height=300)

st.divider()



# 6)
#---------------------------------------------------------------------------------------#
st.header(':six: Dataframes support multi-index headers')

cols = st.columns(2)

data = np.random.randn(4, 6)
arrays = [
    ['Sales', 'Sales', 'Sales', 'Expenses', 'Expenses', 'Expenses'],
    ['Q1', 'Q2', 'Q3', 'Q1', 'Q2', 'Q3'] 
]
multi_index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Quarter'))
df = pd.DataFrame(data, columns=multi_index)



st.code('''
import pandas as pd
df = pd.DataFrame(...)
st.dataframe(df)
''')
df


st.divider()


# 8)
#---------------------------------------------------------------------------------------#
st.header(':seven: st.map and st.pydeck_chart have a full-screen toggle that matches the dataframe toolbar.')

cols = st.columns(2)

st.code('''
import pydeck as pdk

m = pdk.Deck(...)
        
st.pydeck_chart(m, use_container_width=True)
''')
st.pydeck_chart(m, use_container_width=True)

st.divider()