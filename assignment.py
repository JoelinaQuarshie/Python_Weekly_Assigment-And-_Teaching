import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st
 

df = pd.read_csv("metadata.csv",nrows=200)

# #Display the first few rows of the dataframe
print(df.head()) 

# #Identify data types of each column
print(df.dtypes)

# #Check for missing values in important columns
print(df.isnull().sum())

#Generate basic statistics for numerical columns
# print(df.describe())

# #Decide how to handle missing values (removal or filling)
df= df.dropna()
df= df.dropna(subset=['mag_id', 'who_covidence_id', 'arxiv_id', 's2_id'])

# #Filling columns With less missing values
df.fillna({'sha': 'Unknown', 'authors': 'Unknown', 'abstract': 'Unknown' , 'pdf_json_files': 'Unknown' ,'pmc_json_files': 'Unknown'}, inplace=True)

# #Count papers by publication year
paper_counts = df['publish_time'].value_counts().sort_index()
print(paper_counts)


# #Identify top journals publishing COVID-19 research
top_journals = df['journal'].value_counts().head(10)
print(top_journals)

# #Find most frequent words in titles (using simple word frequency)

all_words = ' '.join(df['title'].dropna().astype(str)).lower().split()
word_freq = pd.Series(all_words).value_counts().head(20)
print(word_freq)


#Plot number of publications over time
#Make sure publish_time is datetime
df['publish_time'] = pd.to_datetime(df['publish_time'])

# #Extract year and count publications per year
publish_per_year = df['publish_time'].dt.year.value_counts().sort_index()
#plot
plt.figure(figsize=(15, 5))  # Adjust width as needed
plt.plot(publish_per_year.index, publish_per_year.values, marker='o')
plt.xticks(rotation=45)
plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.title('Publications Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# #Count number of publications per journal
journal_counts = df['journal'].value_counts().reset_index()
journal_counts.columns = ['Journal', 'Count']

# #Plot
plt.figure(figsize=(15, 5))
sns.barplot(data=journal_counts, x='Journal', y='Count', palette='viridis')
plt.title("Top Publishing Journals")
plt.xlabel("Name of Journals")
plt.ylabel("Number of Publications")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# #Combine all titles into one text string
text = ' '.join(df['title'].dropna().astype(str))

#Create and configure the word cloud
wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='white',
    colormap='viridis',
    max_words=200,
    stopwords=None  # You can add your own stopwords if needed
).generate(text)

# Plot the word cloud
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Paper Titles", fontsize=18)
plt.tight_layout()
plt.show()


# Count number of papers per source
source_counts = df['source_x'].value_counts().reset_index()
source_counts.columns = ['Source', 'Count']

# # Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=source_counts, x='Source', y='Count', palette='crest')
plt.title("Distribution of Paper Counts by Source")
plt.xlabel("Source")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





