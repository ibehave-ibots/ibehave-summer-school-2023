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
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('data/round2.csv')
st.data_editor(df)

sns.catplot(
    data=df, 
    x='Subject', 
    y='Time', 
    kind="bar",
)
st.write(plt)

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Create a DataFrame for the principal components
principal_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])

# Concatenate the original DataFrame with the principal components
final_df = pd.concat([df, principal_df], axis=1)