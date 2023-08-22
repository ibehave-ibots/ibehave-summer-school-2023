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
import matplotlib.pylab as plt
import numpy as np

df = pd.read_csv('data/round1.csv')

st.title('Age Distribution Study')
st.subheader('Data overview')
hist,edges=np.histogram(df['Age'])
plt.plot(edges[:-1],hist)
plt.xlabel('Age')
st.text('Description of the age structure in experiment XY')
st.write('## Subheader')



