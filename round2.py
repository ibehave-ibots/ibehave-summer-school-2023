code_reference = '''
# create and show plot
sns.catplot(data=df, x='column_A', y='column_B', kind="bar")
st.write(plt)

# seaborn 
sns.catplot(
    data=df,
    x='column_A',
    y='column_B',
    kind="bar",   # can also be "box", "violin", "point", "line", "boxen", "strip", "swarm" 
    hue = 'column_C', # optional
    row = 'column_D', # optional
    col = 'column_E', # optional
) 

col1, col2 = st.columns(2)
with col1:
    st.write('col1')
with col2:
    st.dataframe(df) 

tab1, tab2 = st.tabs(tabs=['tab1_name', 'tab2_name'])
with tab1:
    st.write('tab1')
with tab2:
    st.data_editor(df)              
'''

import seaborn as sns                   # https://seaborn.pydata.org/generated/seaborn.catplot.html
import streamlit as st                  # https://docs.streamlit.io/library/api-reference
import pandas as pd                     # https://pandas.pydata.org/docs/reference/index.html
import matplotlib.pyplot as plt

df = pd.read_csv('data/round2.csv')
st.data_editor(df)

sns.catplot(
    data=df, 
    x='Subject', 
    y='Time', 
    kind="bar",
)
#st.write(plt)
responses = df.loc[df['Correct']==1]
responses_fil = responses[['Sex','Correct']]

male_responses=responses.loc[responses['Sex']=='M']
print(len(male_responses))
st.write('Total Correct responses by male: ')
st.write(len(male_responses))

female_responses=responses.loc[responses['Sex']=='F']
st.write('Total Correct responses by female: ')
st.write(len(female_responses))
print(len(female_responses))
fig = plt.figure( )
sns.histplot(df['Time'], bins=10, kde=True)
st.pyplot(fig)
#st.write(plt)
#sns.catplot(data=responses_fil, x='Sex', y='Correct')