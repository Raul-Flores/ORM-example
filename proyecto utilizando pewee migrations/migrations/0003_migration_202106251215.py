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
    validation1 = BooleanField(default=True)
    detalles = CharField(max_length=50)
    class Meta:
        table_name = "interface"


def forward(old_orm, new_orm):
    interface = new_orm['interface']
    return [
        # Apply default value '' to the field interface.detalles
        interface.update({interface.detalles: ''}).where(interface.detalles.is_null(True)),
    ]
