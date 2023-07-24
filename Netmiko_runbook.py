from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

    
def show_command(task):
    task.run(task=netmiko_send_command, command_string="show ip interface brief")


command_list= ["show ip interface brief", "show version"]
def show_command_list(task):
    for cmd in command_list:
        task.run(task=netmiko_send_command, command_string=cmd)

def send_config(task):
    task.run(task=netmiko_send_config, config_commands=["ntp server 10.253.11.56", "logging 10.253.24.52"])


def send_config_file(task):
    task.run(task=netmiko_send_config, config_file="ConfigsList.txt")


nr = InitNornir(config_file="config.yaml")

results= nr.run(task=show_command)
#results= nr.run(task=show_command_list)

#results= nr.run(task=send_config)
#results= nr.run(task=send_config_file)

print_result(results)


