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
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Team2 iBots workshop')
st.subheader('coolest kids') 
st.text('`i am having fun`')
st.write('## Subheader')
df = pd.read_csv('data/round1.csv') 
st.write(df)
st.text(f"The average age of subjects is {df['Age'].mean()}")
st.text(f"The ratio of each sex of subject is {df[(df['Sex']=='M')].count() & df[(df['Sex']=='F')].count()}")

fig, ax = plt.subplots(1,2)
ax[0].hist(df[(df['Sex']=='M')]['Age'], color = '#EF767A')
ax[1].hist(df[(df['Sex']=='F')]['Age'], color = '#456990')
ax[0].xlabel('age')
ax[0].ylabel('count')
ax[1].xlabel('age')
ax[1].ylabel('count')
st.pyplot(fig)
# Create a violin plot using Seaborn
plt.figure(figsize=(8, 6))  # Set the figure size
sns.violinplot(x="Sex", y="Age", data=df)

# Set labels and title
plt.xlabel("Sex")
plt.ylabel("Age")
plt.title("Violin Plot of Age by Sex")
# Show the plot
plt.show()