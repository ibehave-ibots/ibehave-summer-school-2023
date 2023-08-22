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
import numpy as np

df = pd.read_csv('data/round2.csv')
st.data_editor(df)

sns.catplot(
    data=df, 
    x='Subject', 
    y='Time', 
    kind="bar",
)


# intro information
st.title("Nature Cover Article")
st.subheader('some stats')
st.metric('number of subjects', len(np.unique(df['Subject'])))
st.metric('average age', np.mean(df['Age']))
st.metric('Average Performance (%)', 100 * np.sum(df['Correct']) / len(df['Correct']))
df.query("Sex=='F'")["Age"]
st.text(df.query("Sex=='F'")["Correct"])
st.bar_chart(data=df, x='Sex', y='Correct')

st.write('distribution of age')

fig, ax = plt.subplots()
ax.hist(df['Age'],bins=10)
st.pyplot(fig)

st.write('Bar chart for correctness across trials')

st.bar_chart(data=df, x='Trial', y='Correct')