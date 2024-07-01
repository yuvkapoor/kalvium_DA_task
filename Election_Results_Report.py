#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv


# In[17]:


import requests
from bs4 import BeautifulSoup
url = "https://results.eci.gov.in/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for i in soup.find_all("code"):
    print(i.text)
    


# In[32]:


#Printing the title of the webpage
title = soup.title
print(title)


# In[38]:


print(soup.find('p').get_text())


# In[33]:


#Finding all the paragraph tags
paras = soup.find_all('p')
print(paras)


# In[40]:


anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://results.eci.gov.in/" +link.get('href')
        all_links.add(link)
        print(linkText)


# In[41]:


navbarSupportedContent = soup.find(id='navbarSupportedContent')


# In[45]:


#Finding any anchor tags in paragraphs
anchors = soup.find_all('a')
for i in paras:
    print(i.get('href'))


# In[46]:


#Finding lists
ul = soup.find("ul")
for i in ul.children:
	print(i)


# In[47]:


ul = soup.find("ul")
print(ul.parent)


# In[48]:


print(ul.parent.parent)


# In[53]:


# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Handle missing values (example: fill with zeros or drop rows)
data.fillna(0, inplace=True)


# In[61]:


pip install selenium pandas


# In[62]:


pip install pandas matplotlib seaborn


# In[66]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Manually input the data into a DataFrame
data = {
    'Party': ['Bharatiya Janata Party - BJP', 'Indian National Congress - INC', 'Samajwadi Party - SP',
              'All India Trinamool Congress - AITC', 'Dravida Munnetra Kazhagam - DMK', 'Telugu Desam - TDP',
              'Janata Dal (United) - JD(U)', 'Shiv Sena (Uddhav Balasaheb Thackeray) - SHSUBT',
              'Nationalist Congress Party - NCPSP', 'Shiv Sena - SHS', 'Lok Janshakti Party (Ram Vilas) - LJPRV',
              'Yuvajana Sramika Rythu Congress Party - YSRCP', 'Rashtriya Janata Dal - RJD',
              'Communist Party of India (Marxist) - CPI(M)', 'Indian Union Muslim League - IUML',
              'Aam Aadmi Party - AAAP'],
    'Won': [240, 99, 37, 29, 22, 16, 12, 9, 8, 7, 5, 4, 4, 4, 3, 3],
    'Leading': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Total': [240, 99, 37, 29, 22, 16, 12, 9, 8, 7, 5, 4, 4, 4, 3, 3]
}

# Create DataFrame
df = pd.DataFrame(data)


# In[68]:


#REPORT
#1 There are a total of 543 parliamentary constituencies
#2 Andhra Pradesh has 175 assemble constituencies
#3 Odisha has 147 assembly constituencies


# In[69]:


#4 The plot shows the parties with the most wins in the elections

plt.figure(figsize=(14, 8))
sns.barplot(x='Won', y='Party', data=df, palette='viridis')
plt.title('Number of Seats Won by Each Party')
plt.xlabel('Seats Won')
plt.ylabel('Party')
plt.show()


# In[71]:


#5 Top 5 parties 
import pandas as pd

# Manually input the data into a DataFrame
data = {
    'Party': [
        'Bharatiya Janata Party - BJP', 'Indian National Congress - INC', 'Samajwadi Party - SP',
        'All India Trinamool Congress - AITC', 'Dravida Munnetra Kazhagam - DMK', 'Telugu Desam - TDP',
        'Janata Dal (United) - JD(U)', 'Shiv Sena (Uddhav Balasaheb Thackeray) - SHSUBT',
        'Nationalist Congress Party - NCPSP', 'Shiv Sena - SHS', 'Lok Janshakti Party (Ram Vilas) - LJPRV',
        'Yuvajana Sramika Rythu Congress Party - YSRCP', 'Rashtriya Janata Dal - RJD',
        'Communist Party of India (Marxist) - CPI(M)', 'Indian Union Muslim League - IUML',
        'Aam Aadmi Party - AAAP'
    ],
    'Won': [240, 99, 37, 29, 22, 16, 12, 9, 8, 7, 5, 4, 4, 4, 3, 3],
    'Leading': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Total': [240, 99, 37, 29, 22, 16, 12, 9, 8, 7, 5, 4, 4, 4, 3, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by the 'Won' column in descending order and get the top five rows
top_five_parties = df.sort_values(by='Won', ascending=False).head(5)

# Print the top five parties
print(top_five_parties[['Party', 'Won']])


# In[72]:


#6 BJP won the elections with a huge margin


# In[73]:


#7 BJP lost in Ayodhya constituency even after the construction of Ram Mandir


# In[74]:


#8 INC got a 25% increase in constituencies


# In[75]:


#9 INC and AAAP formed a coaliton government for the elections


# In[ ]:


#10 There was a significant decline in voters as compared to the previous elections

