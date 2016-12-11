from peewee import SqliteDatabase, Model, CharField
from app import Record, db
import json

print('Please input the ID which you want to query:')
id = int(input())
data = json.loads(Record.select().where(Record.id == str(id)).get().data)
for id, key in data.items():
	print(id + ', ' + key)
	
