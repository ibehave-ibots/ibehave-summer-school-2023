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

st.write(f"Number of participants: "+ str(df["Subject"].unique().shape[0]))
col1, col2 = st.columns(2)
with col1:

    plot = sns.catplot(
        data=df, 
        x='Subject', 
        y='Time', 
        kind="bar",
    )
    st.pyplot(plot)
    #st.write(plt)
    st.subheader("All correct answers, all participants")
    plot = sns.catplot(
        data=df, 
        x='Subject', 
        y='Matching', 
        kind="bar",
    )
    st.pyplot(plot)

m_col, f_col = st.columns(2)
male_df = df[df["Sex"] == "M"]
female_df = df[df["Sex"] == "F"]
with m_col:
    st.subheader("All correct answers, Male")
    plot = sns.catplot(
        data=male_df, 
        x='Subject', 
        y='Matching', 
        kind="bar",
    )
    st.pyplot(plot)
    plot = sns.catplot(
        data=male_df, 
        x='Subject', 
        y='Time', 
        kind="violin",
    )
    st.pyplot(plot)

with f_col:
    
    st.subheader("All correct answers, Females")
    plot = sns.catplot(
        data=female_df, 
        x='Subject', 
        y='Matching', 
        kind="bar",
    )
    st.pyplot(plot)
    plot = sns.catplot(
        data=female_df, 
        x='Subject', 
        y='Time', 
        kind="violin",
    )
    st.pyplot(plot)

st.subheader("All correct answers, all participants")
plot = sns.catplot(
        data=male_df, 
        x='Matching', 
        y='Time', 
        kind="bar",
    )
st.pyplot(plot)
