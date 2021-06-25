# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class interface(peewee.Model):
    device_ip = CharField(max_length=40)
    intf_name = CharField(max_length=40)
    description = CharField(max_length=90)
    is_enabled = BooleanField()
    mac_address = CharField(max_length=30)
    mtu = IntegerField()
    speed = IntegerField()
    status_date = DateTimeField()
    class Meta:
        table_name = "interface"


