import pandas as pd
import datetime
from datetime import datetime, date
import os

#Import CSV files using pandas, with usecols excluding unnecessary data columns.

AnimeLists_Filtered = pd.read_csv(os.path.join('Anime','csv_files', 'animelists_filtered.csv'), usecols=[0,1,2,5,8])
print('AnimeLists_Filtered')
print(AnimeLists_Filtered.keys())

AnimeList = pd.read_csv(os.path.join('Anime','csv_files', 'AnimeList.csv'), usecols=[0,1,22])
print('AnimeList')
print(AnimeList.keys())

# Convert original air date of anime to display only year value.

AnimeList['premiered'] = AnimeList['premiered'].astype(str).str.replace('\D+', '')

UserList = pd.read_csv(os.path.join('Anime','csv_files', 'UserList.csv'), usecols=[0,8,10])
print('UserList')
print(UserList.keys())

# Convert birth_date column results to correct dd/mm/yyyy format.
date = pd.Timestamp('2000-01-01')

UserList['birth_date'] = pd.to_datetime(UserList['birth_date'], errors='coerce').fillna(date)
UserList['birth_date'] = UserList['birth_date'].dt.strftime('%d/%m/%Y')

# Calculate age based on birth_date column, and drop birth_date column.
def age(born):
    born = datetime.strptime(born, "%d/%m/%Y").date()
    today = date.today()
    return today.year - born.year - ((today.month, 
                                      today.day) < (born.month, 
                                                    born.day))
  
UserList['age'] = UserList['birth_date'].apply(age)

print(UserList['age'])

UserList = UserList.drop(['birth_date'], axis=1)

# Merge AnimeLists_Filtered and AnimeList based on anime_id, and drop said column.
data1 = AnimeLists_Filtered
data2 = AnimeList
  
output = pd.merge(data1, data2, on='anime_id', how='left')
print(output.keys())

output = output.drop(['anime_id'], axis=1)

#Merge output and UserList based on username, and drop said column.
data1 = output
data2 = UserList

output1 = pd.merge(data1, data2, on='username', how='left')
print(output1.keys())

output1 = output1.drop(['username'], axis=1)

output1.to_csv(os.path.join('Anime','csv_files', 'joined2.csv'), index=False)