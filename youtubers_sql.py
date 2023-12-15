import sqlite3

#connecting to the database
conn = sqlite3.connect('yt_database')
c = conn.cursor()

#creating the table
c.execute('''
          CREATE TABLE yttable132
          ([year] TEXT, [pewdiepie] INTEGER, [JuegaGerman] INTEGER, [Fernanfloo] INTEGER,[Mikecrack] INTEGER,[JessNoLimit] INTEGER,[MrBeastGaming] INTEGER,[TotalGaming] INTEGER,[TechnoGamerz] INTEGER,[Markiplier] INTEGER,[jacksepticeye] INTEGER)
          ''')
          
#inserting the appropriate values
c.execute('''
          INSERT INTO yttable132 (year,pewdiepie,JuegaGerman,Fernanfloo,Mikecrack,JessNoLimit,MrBeastGaming,TotalGaming,TechnoGamerz,Markiplier,jacksepticeye)

                VALUES
                ('2010',1600,0,0,0,0,0,0,0,0,0),
                ('2011',86700,0,6900,0,0,0,0,0,0,0),
                ('2012',3400000,0,2300000,0,0,0,0,0,56400,50),
                ('2013',18800000,1200000,14200000,0,0,0,0,0,1300000,33100),
                ('2014',33200000,5900000,20600000,0,0,0,0,0,5200000,2400000),
                ('2015',40900000,10500000,25700000,0,0,0,0,0,11000000,7900000),
                ('2016',52000000,16800000,30600000,38500,0,0,0,0,16000000,13900000),
                ('2017',58900000,23600000,32900000,2600000,540000,0,0,2000,19000000,17400000),
                ('2018',78800000,31500000,35100000,8000000,4400000,0,15000,92900,22700000,21100000),
                ('2019',102300000,40200000,40100000,13200000,7100000,0,3800000,609000,24700000,23300000),
                ('2020',107200000,42100000,42100000,29800000,19900000,12000000,18600000,12000000,28000000,26000000),
                ('2021',111100000,43100000,43200000,38300000,28200000,24900000,30500000,23100000,31200000,27800000),
                ('2022',111900000,45500000,45500000,38300000,36000000,30400000,34200000,31400000,33700000,28900000),
                ('2023',111904000,48700000,46500000,44300000,40800000,39300000,36200000,36000000,35600000,30400000)
          ''')

#commit changes
conn.commit()

print('changes done successfully!')