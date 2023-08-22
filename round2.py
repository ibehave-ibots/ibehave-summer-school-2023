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
from math import pi

df = pd.read_csv('data/round2.csv')
st.data_editor(df)

sns.catplot(
data=df, 
x='Subject', 
y='Time', 
kind="bar",
)
st.write(plt)

###
angles = df.Angle
grouped = df.groupby('Angle')['Correct'].agg(['sum', 'count'])
grouped['hit_rate'] = grouped['sum'] / grouped['count']

# Reset the index for the resulting DataFrame
grouped = grouped.reset_index()


angles = [n / float(4) * 2 * pi for n in range(4)]
angles += angles[:1]

ax = plt.subplot(111,polar=True)

ax = set_theta_offset(pi/2)
ax.set_theta_direction(-1)

categories = pd.unique(angles, dtype=str)

plt.xticks(angles[:-1], categories)

ax.plot(angles, grouped['hit_rate'])
ax.fill(angles, grouped['hit_rate'])

plt.show()