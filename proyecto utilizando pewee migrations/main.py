
import datetime
from napalm import get_network_driver
from models import interface
driver= get_network_driver('ios')
inventory = [
{'hostname': 'ios-xe-mgmt-latest.cisco.com','username': 'developer','password': 'C1sco12345', 'optional_args' : {'port': 22}},
{'hostname': 'ios-xe-mgmt.cisco.com','username': 'developer','password': 'C1sco12345', 'optional_args' : {'port': 8181}}
]
if __name__ == '__main__':
    for device in inventory:
        try:
            connection = driver(**device)
            connection.open()
            comando = connection.get_interfaces()
            connection.close()
            for data in comando.items():
                validar = interface.select().where(interface.device_ip == device['hostname'], interface.intf_name == data[0])
                if not validar.exists():
                    new_row = interface.create(
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
                    update_row = interface.update(is_enabled=data[1]['is_enabled']).where(interface.device_ip == device['hostname'], interface.intf_name == data[0])
                    update_row.execute()
        except Exception as error:
            print (" Error identificado: \n", error)  
