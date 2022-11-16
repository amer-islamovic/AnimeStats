from fileinput import close
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import datetime as dt
import os
import csv
from csv import writer
from csv import reader
from urllib.request import urlretrieve
from sqlalchemy import true

AnimeLists_Filtered = pd.read_csv(os.path.join('Anime','csv_files', 'animelists_filtered.csv'), usecols=[0,1,2,5,8])
print('AnimeLists_Filtered')
print(AnimeLists_Filtered.keys())

AnimeList = pd.read_csv(os.path.join('Anime','csv_files', 'AnimeList.csv'), usecols=[0,1,22])
print('AnimeList')
print(AnimeList.keys())

UserList = pd.read_csv(os.path.join('Anime','csv_files', 'UserList.csv'), usecols=[0,8,9,10])
print('UserList')
print(UserList.keys())

# Merge AnimeLists_Filtered and AnimeList
data1 = AnimeLists_Filtered
data2 = AnimeList
  
# # using merge function by setting how='left'
output = pd.merge(data1, data2, on='anime_id', how='left')
print(output.keys())

output.to_csv(os.path.join('Anime','csv_files', 'joined1.csv'), index=False)
UserList.to_csv(os.path.join('Anime','csv_files', 'Users1.csv'), index=False)

#Merge output and UserList
data1 = output
data2 = UserList
  
# # using merge function by setting how='left'
output1 = pd.merge(data1, data2, on='username', how='left')
print(output1.keys())

output1.to_csv(os.path.join('Anime','csv_files', 'joined2.csv'), index=False)