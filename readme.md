# Anime Stats
A tool looking at Anime data.

![This is an image](/Figure_1.png)
![This is an image](/Figure_2.png)

## Project Description
This tool looks at age, gender, rating for some of our favorite anime through the years!

## How to use

1. Clone the repository through a program like git bash, or directly from the code dropdown in github!
2. Download animelists_filtered.csv, AnimeList.csv and UserList.csv from https://www.kaggle.com/datasets/azathoth42/myanimelist!
3. Create a virtual environment by typing in command line: 
    python3 -m venv venv
    source ./venv/bin/activate
4. Install the requirements by typing the following command in your code editor: pip install -r requirements.txt
5. Open and run clean_data.py to merge and clean downloaded files to a new CSV file.
6. Open and run Anime.py!

## Features
- Read TWO data files (JSON, CSV, Excel, etc.) - animelists_filtered.csv, AnimeList.csv and UserList.csv
- Clean and operate on the data while combining them - Removed NaN values, corrected datetime, and used to get age. Merged to one file.
- Visualize / Present your data - Pandas pivot tables and matplotlib charts.
- Best practices - Venv used and explained in readme.
- Interpretation of your data - Notations made through the project.
