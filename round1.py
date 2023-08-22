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
st.title('Group8_r1_ibots')
st.subheader('Hi Guys') 
st.text('I don´t like food')
st.write('But I like math')
df = pd.read_csv('data/round1.csv') 

st.write(df)
z=df.iloc[:,2]
plt(len(z),z)