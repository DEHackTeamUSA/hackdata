# DEHackTeamUSA
# hackdataHR 2016

# Transfers machine learning output (CSV) to database visualization feed.

import csv, sqlite3

con = sqlite3.connect("safetyeducation.sqlite")
cur = con.cursor()
cur.execute("CREATE TABLE t (qtr1, qtr2, ind_name_1, loc_1, ind_value_1, ind_name_2, loc_2, ind_value_2);")

with open('safetyeducation.csv','rb') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['quater'], i['quater (2)'], i['Indicator Name'], i['Location'], i['Indicator Value'], i['Indicator Name (2)'], i['Location (2)'], i['Indicator Value (2)'],) for i in dr]

cur.executemany("INSERT INTO t (qtr1, qtr2, ind_name_1, loc_1, ind_value_1, ind_name_2, loc_2, ind_value_2) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()
