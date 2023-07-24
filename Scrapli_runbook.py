from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_commands
from nornir_scrapli.tasks import send_commands_from_file
from nornir_scrapli.tasks import send_config
from nornir_scrapli.tasks import send_configs
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result


def show_command(task):
    task.run(task=send_command, command="show version")

command_list= ["show ip interface brief", "show version"]
def show_command_list(task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd)

def show_commands(task):
    task.run(task=send_commands, commands=["show ip interface brief", "show version"])

def show_commands_fromfile_test(task):
    task.run(task=send_commands_from_file, file="CommandsList.txt")


def send_config_test(task):
    task.run(task=send_config, config="ntp server 10.253.11.56")

def random_config(task):
    task.run(task=send_config, config=f"ntp server {task.host['ntp_server']}")

def send_configs_test(task):
    task.run(task=send_configs, configs=["ntp server 10.253.11.56", "logging server 10.252.20.40"], dry_run=True)

def send_configs_fromfile_test(task):
    task.run(task=send_configs_from_file, file="ConfigsList.txt")


nr = InitNornir(config_file="config.yaml")

###SHOW With Scrapli
#results = nr.run(task=show_command)
#results = nr.run(task=show_command_list)
#results = nr.run(task=show_commands)
#results = nr.run(task=show_commands_fromfile_test)

###Config With Scrapli
#results= nr.run(task=send_config_test)
results= nr.run(task=random_config)
#results= nr.run(task=send_configs_test)
#results= nr.run(task=send_configs_fromfile_test)

print_result(results)
