import streamlit as st
import plotly.express as px
import pandas as pd

def display_map(location_data):
	fig = px.scatter_mapbox(location_data, lat='latitude', lon='longitude', size='mark_size', hover_name='location')
	fig.update_layout(mapbox_style='open-street-map')
	return fig


st.title("My Location")

# Create the pandas DataFrame for map locations
data = {'location': ['Faculty of Engineering Kamphaeng Saen', 'Baan Klang Muang Urbanion Kaset Navamin 2', 'Amonphan Shop'],
        'latitude': [14.02082, 13.85457, 13.28210],
        'longitude': [99.97117, 100.60643, 101.43712],
        'mark_size': [5, 5, 5]}
        #'mark_color': ['rgb(255, 0, 0)', 'rgb(0, 0, 255)', 'rgb(0, 255, 0)']}
df = pd.DataFrame(data)
st.write(df)

px_map = display_map(df)
st.plotly_chart(px_map, use_container_width=True)


#from ipywidgets import embed
#snippet = embed.embed_snippet(views=map)
#html = embed.html_template.format(title="", snippet=snippet)

#import streamlit.components.v1 as components
#components.html(html, height=500,width=500)