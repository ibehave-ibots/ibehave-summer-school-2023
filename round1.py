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

st.title('Team2 iBots workshop')
st.subheader('coolest kids') 
st.text('`i am having fun`')
st.write('## Subheader')
df = pd.read_csv('data/round1.csv') 
st.write(df)
st.text(f"The average age of subjects is {df['Age'].mean()}")
st.text(f"The ratio of each sex of subject is {df[(df['Sex']=='M')].sum()&df[(df['Sex']=='F')].sum()}")

fig, ax = plt.subplot()
ax.hist(df[(df['Sex']=='M')], color = '#EF767A')
ax.hist(df[(df['Sex']=='F')], color = '#456990')