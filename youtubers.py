#importing libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#connecting to the databae
conn = sqlite3.connect('yt_database')

#reading the query
sql_query1 = pd.read_sql_query('''
                               SELECT
                               *
                               FROM yttable132
                               ''', conn)

#creating the dataframe
df = pd.DataFrame(sql_query1, columns=['pewdiepie','JuegaGerman','Fernanfloo','Mikecrack','JessNoLimit','MrBeastGaming','TotalGaming','TechnoGamerz','Markiplier','jacksepticeye'])

#plotting the graph from the dataframe
df.plot(label=['Pewdiepie','JuegaGerman','Fernanfloo','Mikecrack','JessNoLimit','MrBeastGaming','TotalGaming','TechnoGamerz','Markiplier','jacksepticeye'], color=['red','blue','black','pink','gray','brown','yellow','green','purple','orange'], kind="line")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13], ["2010", "2011", "2012", "2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"])

print(df)
plt.show()