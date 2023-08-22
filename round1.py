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

st.title('Flaming Flamingos Story Time')
st.subheader('A legally different telling of a battle in space') 
st.text('In a galaxy far, far away... there were some flamingos.')
st.write('## Those Impacted by the Tyranny of the Empire')
df = pd.read_csv('data/round1.csv') 
import numpy as np

print(df)
names = df[["Subject"]]
print(names)
Age = df[["Age"]]
print(Age)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(Age, bins=10)
st.pyplot(fig)


plt.figure(figsize=(9,3))
