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
from pathlib import Path

st.title('This is a placeholder title')
st.subheader('By Natalia, Trace, and Ali') 
st.text('The magnificent team is learning how to commit')
st.write('## Subheader')
df = pd.read_csv('data/round1.csv')
df= df.sort_values(by=['Age'])
st.text("Here's the data:")
df.apply(lambda row: st.text(f'Subject: {row["Subject"]}, Age: {row["Age"]}, Sex: {row["Sex"]}'), axis=1)
