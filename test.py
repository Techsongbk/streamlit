import streamlit as st
import pandas as pd
import plotly.express as px

avocado = pd.read_csv("avocado.csv")

st.write('# Avocado Prices dashboard')  #st.title('Avocado Prices dashboard')
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')
st.header('Summary statistics')

st.header('Line chart by geographies')
avocado_stats = avocado.groupby('type')['AveragePrice'].mean()
st.dataframe(avocado_stats)

st.header('Line chart by geographies')

with st.form('line_chart'):
    selected_geography = st.selectbox(label='Region', options=avocado['region'].unique())
    submitted = st.form_submit_button('Submit')
    if submitted:
        filtered_avocado = avocado[avocado['region'] == selected_geography]
        line_fig = px.line(filtered_avocado,
                           x='date', y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        st.plotly_chart(line_fig)


with st.sidebar:
    st.subheader('About')
    st.markdown('This dashboard is made by Just into Data, using **Streamlit**')
st.sidebar.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=50)