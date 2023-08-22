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
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Round 1 Data Dashboard')
st.subheader('project description information') 
st.text('data analysis for neural spiking data')
st.text('Epileptic Seizure Onset Detection')
st.text('locomotor modulation of Drosophila sensory processing')
st.text('Automated behavioral platform')
st.write('## Subheader')
df = pd.read_csv('data/round1.csv') 
a = df.shape
st.text('Our dataset has the shape: ')
st.text(a)
mn_age = df.Age.mean()
print((df.Age.mean()))
st.text('Mean age: ')
st.text(mn_age)
#st.text('Mean age of the subjects in our dataset is: ',mean(df.Age))
print(df.head(2))
print(df.columns)
print(len)
val_cnt = df['Sex'].value_counts()
print()
st.text('number of females and males: ')
st.text(val_cnt)
print(val_cnt)
plt.plot('Sex','Count',data=val_cnt.reset_index())
#age= max(df['Age'].max())
