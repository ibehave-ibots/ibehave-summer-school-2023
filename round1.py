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

f_hist,f_edges=np.histogram(df['Age'])

fig, ax = plt.subplots(2,1)
ax[0].title('All participants')
ax[0].hist(df['Age'],color='k')
ax[1].title('Sex sepereation')
ax[1].hist(df[df.Sex=='F']['Age'])
ax[0].set_xlabel('Age')


st.write(fig)
st.text('Description of the age structure in experiment XY')
st.write('## Subheader')



