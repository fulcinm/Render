import streamlit as st
import pandas as pd
import plotly.express as px



df = pd.read_csv('cars.csv')

st.header('Market of used Cars')
st.write("""
##### Filter the data below to see the ads by model""")

df['model_year'] = pd.to_numeric(df['model_year'], errors = 'coerce')
df = df.dropna(subset=['model_year'])
df['model_year'] = df['model_year'].astype(int)

df['cylinders'] = pd.to_numeric(df['cylinders'], errors = 'coerce')
df = df.dropna(subset=['cylinders'])
df['cylinders'] = df['cylinders'].astype(int)

df['odometer'] = pd.to_numeric(df['odometer'], errors = 'coerce')
df = df.dropna(subset=['odometer'])
df['odometer'] = df['odometer'].astype(int)

df = df.dropna(subset=['paint_color'])

models = df['model'].unique()

name_models = st.selectbox('Select model:', models)


year_min, year_max = (df['model_year'].min(),df['model_year'].max())
year_range = st.slider("Choose years:",value=(year_min, year_max), min_value=year_min, max_value=year_max)

actual_range = list(range(year_range[0], year_range[1]+1))

filtered_df = df[(df['model']==name_models) & (df.model_year.isin(actual_range))]

st.table(filtered_df.head(100))


st.header('Price Comparison')
st.write("""
##### How distribution of price varies depending on transmission, cylinders, type, and condition""")

list_for_hist=['transmission','cylinders','type','condition']
choice_for_hist=st.selectbox('split for price distribution', list_for_hist)

fig = px.histogram(df, x='price', color=choice_for_hist)

fig.update_layout(
title='<b> Split of price by {} </b>'.format(choice_for_hist))
st.plotly_chart(fig)

df['age']=2023-df['model_year']
def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'

df['age_category'] = df['age'].apply(age_category)


st.write("""
##### How distribution of price varies depending on odometer and number of days listed""")
list_for_scatter=['odometer','days_listed']
choice_for_scatter=st.selectbox('split for price distribution', list_for_scatter)

fig2 = px.scatter(df, x='price', y = choice_for_scatter, color = 'age_category')
st.plotly_chart(fig2)

    

