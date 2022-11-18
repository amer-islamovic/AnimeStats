import matplotlib.pyplot as plt 
import pandas as pd
import os
import collections

# Import clean data

AnimeList = pd.read_csv(os.path.join('Anime','csv_files', 'joined2.csv'))

# Average rating and total watched episodes by gender

pivot = pd.pivot_table(
    data=AnimeList,
    index='gender',
    aggfunc={'my_score': 'mean', 'my_watched_episodes': 'sum'}
)

print(pivot)

# Top 10 watched Anime.

list = AnimeList['title']
ctr = collections.Counter(list)
print(ctr.most_common(10))

# Episodes watched by age and gender.

df_grouped = AnimeList.groupby(['age', 'gender'])['my_watched_episodes'].sum()
df_grouped.unstack().plot()
plt.show()

# Episodes watched and average rating by release year.

df_grouped = AnimeList.groupby(['premiered', 'my_score'])['my_watched_episodes'].sum()
df_grouped.unstack().plot()
plt.show()