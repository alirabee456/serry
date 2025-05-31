import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
data=pd.read_excel('pandas28.xlsx')
branches=['all']+data['Branch'].unique().tolist()
st.sidebar.header('Filters')
s=st.sidebar.selectbox(label='select a branch',options=branches)
payments=['all']+data['Payment'].unique().tolist()
p=st.sidebar.selectbox(label='select a payment',options=payments)
st.sidebar.image('profit.gif')
if s!='all':
    data=data[data['Branch']==s]
if p!='all':
    data=data[data['Payment']==p]

tab1,tab2,tab3=st.tabs(['sales','Quantity','kpis'])
with tab1:
    total_quantity=data['Quantity'].sum()
    orders=data['Invoice ID'].count()
    total_sales=np.round(data['Total'].sum()/1000,2)
    avg_rating=np.round(data['Rating'].mean(),1)
    total_tax=np.round(data['Tax 5%'].sum()/1000,2)
    col1,col2,col3,col4,clo5=st.columns([1,1,1,1,1])
    col1.metric(label='total quantity', value=total_quantity)
    col2.metric(label='orders', value=orders)
    col3.metric(label='total sales', value=f"{total_sales} K")
    col4.metric(label='average rating', value=avg_rating)
    clo5.metric(label='total tax', value=f"{total_tax}K")

with tab2:
    d2 = data['Gender'].value_counts().reset_index()
    fig1=px.pie(d2,names='Gender',values='count')
    st.plotly_chart(fig1)