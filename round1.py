reference = '''
st.write(df)
st.metric('Age', 10)
st.dataframe(df)
st.data_editor(df)
 
df['column_A'].min()  
df['column_A'].max() 
df['column_A'].mean() 
df['column_A'].std() 
df['column_A'].value_counts() 
df['column_A'].unique()
'''

import streamlit as st                  # https://docs.streamlit.io/library/api-reference
import pandas as pd                     # https://pandas.pydata.org/docs/reference/index.html
import matplotlib.pyplot as plt

st.title('Superduuper Team 1')
st.subheader('Unbelivable Data') 
st.text('The wordls best data')
st.write('Age and Sex wise distribution of feature X')
df = pd.read_csv('data/round1.csv')
col1, col2 = st.columns(2)
st.write(df)
with col1:
    fig, ax = plt.subplots()
    df.plot.hist(column = "Age", ax = ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    df[df["Sex"]=="M"].plot.hist(column = "Age", ax = ax, color = "blue")
    plt.title("Age Male")
    st.pyplot(fig)
    st.write("Distribution of age for male")

with col2:
    sexTable = df['Sex'].value_counts()

    fig, ax = plt.subplots()
    
    sexTable.plot.pie(ax = ax, autopct='%.2f')
    plt.title("Feature X: Sex Distribution")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    df[df["Sex"]=="F"].plot.hist(column = "Age", ax = ax, color = "orange")
    plt.title("Age Female")
    st.pyplot(fig)
# pie chart for sex
# Histogram for age in general
# Histogram for age split by sex
