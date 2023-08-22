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

#Subject,Trial,Angle,Matching,Response,Time,Correct,Age,Sex

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
st.write('The number of participants is '+str(len(df['Subject'].unique())))

unique_participants=df['Subject'].unique()

res = pd.DataFrame(columns=['participant_id', 'n_trials', 'performance'])
for i, p in enumerate(unique_participants):
    res.at[i,'participant_id'] = p
    res.at[i, 'n_trials'] = len(df[df.Subject== p]) 
    res.at[i, 'performance'] = df[df.Subject== p]['Correct'].sum()/  res.at[i, 'n_trials']
st.write(res)

fig, ax = plt.subplots(2,1, layout='constrained') #set figure

ax[0].hist(res['performance'])
ax[0].set_xlabel('performance')

ax[1].hist(res['n_trials'])
ax[1].set_xlabel('number of trials')

fig.supylabel('Number [#]')
st.write(fig)

fig,ax=plt.subplots(1,1)
ax.scatter(df['Trial'],df['Time'])
ax.set_xlabel('Trial')
ax.set_ylabel('Time')
st.write(fig) #writes figure to board
