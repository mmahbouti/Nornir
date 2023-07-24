from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")
nr.inventory.hosts
nr.inventory.hosts["SW-21"]
nr.inventory.hosts["SW-21"].hostname
nr.inventory.defaults.username

#task.host['ntp server ']
