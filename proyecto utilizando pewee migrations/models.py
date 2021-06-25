
import pymysql
import sqlite3
import psycopg2
from peewee import *
db = "postgres"
class BaseModel(Model):
    class Meta:
        global db
        secretvar= "Secret"
        while True:
            try:
                #db = input("BD Options: [mariadb|postgres|sqlite] :")
                db_migration = db
                if db == "mariadb":
                    db = MySQLDatabase("TEST", host="localhost", port=3306, user="root", password=secretvar)
                    break
                elif db == "postgres":
                    db = PostgresqlDatabase("TEST", host="localhost", port=5432, user="postgres", password=secretvar)
                    break
                elif db == "sqlite":
                    db = SqliteDatabase('TEST.db')
                    break
            except:
                print ("Los valores introducidos no son correctos") 
        database = db

class interface(BaseModel):
    device_ip = CharField(max_length=40)
    intf_name = CharField(max_length=40)
    description = CharField(max_length=90)
    is_enabled = BooleanField()
    mac_address = CharField(max_length=30)
    mtu = IntegerField()
    speed = IntegerField()
    status_date = DateTimeField()
    validation1 = BooleanField(default=True)
    detalles = CharField(max_length=50)
    #class Meta:
    #    db_table = 'interface'