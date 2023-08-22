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
st.title('Flaming Flamingos Story Time 2')
st.subheader('The Flamingo Squaks Back')
df = pd.read_csv('data/round2.csv')
df.sort_values(by='Age', ascending=True)
st.data_editor(df)

'''
sns.catplot(
    data=df, 
    x='Subject', 
    y='Time', 
    kind="bar",
)
st.write(plt)
'''

age = df[["Age"]]
time = df[["Time"]]
fig, ax = plt.subplots()
ax.hist(time, bins=6)

fig, ax = plt.subplots()
ax.hist(age, bins=6)


#st.pyplot(fig, x= "Time")
fig, ax = plt.subplots()
st.table(df)

from PIL import Image
image = Image.open('iBehave.jpg')
st.image(image, caption='Oh yeah')









