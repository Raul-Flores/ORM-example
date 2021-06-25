from peewee import *
import psycopg2
import pymysql
import sqlite3
import datetime
from napalm import get_network_driver
secretvar= "Secret"
db = ""
class BaseModel(Model):
    class Meta:
        while True:
            try:
                db = input("BD Options: [mariadb|postgres|sqlite] :")
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
class Interface(BaseModel):
    device_ip = CharField(max_length=40)
    intf_name = CharField(max_length=40)
    description = CharField(max_length=90)
    is_enabled = BooleanField()
    mac_address = CharField(max_length=30)
    mtu = IntegerField()
    speed = IntegerField()
    status_date = DateTimeField()
    #class Meta:
    #    db_table = 'interface'


driver= get_network_driver('ios')
inventory = [
{'hostname': 'ios-xe-mgmt-latest.cisco.com','username': 'developer','password': 'C1sco12345', 'optional_args' : {'port': 22}},
{'hostname': 'ios-xe-mgmt.cisco.com','username': 'developer','password': 'C1sco12345', 'optional_args' : {'port': 8181}}
]
if __name__ == '__main__':
    if not Interface.table_exists():
        Interface.create_table()
    for device in inventory:
        try:
            connection = driver(**device)
            connection.open()
            comando = connection.get_interfaces()
            connection.close()
            for data in comando.items():
                validar = Interface.select().where(Interface.device_ip == device['hostname'], Interface.intf_name == data[0])
                if not validar.exists():
                    new_row = Interface.create(
                        device_ip=device['hostname'], 
                        intf_name=data[0], 
                        description=data[1]['description'],
                        is_enabled=data[1]['is_enabled'],
                        mac_address=data[1]['mac_address'],
                        mtu=data[1]['mtu'],
                        speed=data[1]['speed'],
                        status_date= datetime.datetime.now()
                        )
                    new_row.save()
                    print (device['hostname'], "Interfaz agregada a la BD")
                else:
                    update_row = Interface.update(is_enabled=data[1]['is_enabled']).where(Interface.device_ip == device['hostname'], Interface.intf_name == data[0])
                    update_row.execute()
        except Exception as error:
            print (" Error identificado: \n", error)  

