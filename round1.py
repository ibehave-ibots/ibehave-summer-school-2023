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
st.write('## Subheader')
df = pd.read_csv('data/round1.csv')
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots()
    df.plot.hist(column = "Age", ax = ax)
    st.pyplot(fig)
with col2:
    sexTable = df['Sex'].value_counts()
    st.write(sexTable)
# pie chart for sex
# Histogram for age in general
# Histogram for age split by sex
