import pandas as pd 
import matplotlib.pyplot as plt 

# Step 1: Read CSV file
df = pd.read_csv('netflix_titles.csv')

# Step 2: Clean the data
df = df.dropna(subset=['type','release_year','rating','country','duration'])

# ---- Plot 1: Movies vs TV Shows ----
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue','orange'])
plt.title('Number of Movies Vs Number of TV shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Movies_vs_TvShows.png')
plt.show()

# ---- Plot 2: Content Ratings Pie Chart ----
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('Content_Ratings_Pie.png')
plt.show()

# ---- Plot 3: Movie Duration Histogram ----
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='blue', edgecolor='black')
plt.title('Distribution of Movies Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('Movie-Duration-Histogram.png')
plt.show()

# ---- Plot 4: Release Year vs Number of Shows ----
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='blue')
plt.title('Release Year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('Release-Year-Scatter.png')
plt.show()

# ---- Plot 5: Top 10 Country Contents ----
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='skyblue')
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Top-10-Countries.png')
plt.show()

# ---- Plot 6 & 7: Movies vs TV Shows Subplots ----
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1, 2, figsize=(12,5), sharex=True)

# Movies subplot
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# TV Shows subplot
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies & TV Shows Release Over Years')
plt.tight_layout()
plt.savefig('Movies_TV-Shows_Comparison.png')
plt.show()
