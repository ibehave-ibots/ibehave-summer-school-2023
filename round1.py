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
import numpy as np

st.title('Middle school :green[class trip]:apple:')
st.subheader('our goal') 
st.text('Being noisy')
st.write('OMG, what are we gonna do?')
df = pd.read_csv('data/round1.csv') 
st.write('lets generate some data as a number of code eah person can write')
st.dataframe(df)
st.divider()
l = len(df)
rand_vec = np.random.randint(5, size=l)
age = np.mean(df['Age'])
st.metric('average age',age,3)

st.line_chart(df['Age'])
Age_df = pd.DataFrame()
Age_df['M'] = df.query("Sex=='M'")["Age"]
st.text(Age_df)
