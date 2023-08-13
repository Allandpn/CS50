import csv
from cs50 import SQL


db = SQL('sqlite:///shows.db')

with open('imdb_top_1000.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        db.execute("INSERT INTO shows (Poster_Link,Series_Title,Released_Year,Certificate,Runtime,Genre,IMDB_Rating,Overview,Meta_score,Director,Star1,Star2,Star3,Star4,No_of_Votes,Gross) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row['Poster_Link'], row['Series_Title'], row['Released_Year'], row['Certificate'], row['Runtime'], row['Genre'], row['IMDB_Rating'], row['Overview'], row['Meta_score'], row['Director'], row['Star1'], row['Star2'], row['Star3'], row['Star4'],row['No_of_Votes'], row['Gross'])
            




