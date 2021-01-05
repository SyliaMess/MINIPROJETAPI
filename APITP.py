import pyodbc
import cursor
import requests
import json

con = pyodbc.connect('DRIVER={SQL Server};'
                     'SERVER=DESKTOP-GE0IH3H;'
                     'DATABASE=mydatabase;'
                     'Trusted_Connection=yes;')
cursor = con.cursor()
r = requests.get('https://amiiboapi.com/api/amiibo')

data_json = r.json()
print(json.dumps(data_json, indent=4, sort_keys=True))
for i in data_json['amiibo']:
    date = i["amiiboSeries"]
    date2 = i["name"]
    date3 = i["gameSeries"]
    date5 = i["release"]["au"]

    cursor.execute("insert into api(amiiboSeries,name,gameSeries,au) values (?,?,?,?)", date, date2, date3, date5)

con.commit()
