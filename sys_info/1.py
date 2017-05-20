import platform
import psutil
import os
import socket
import json
def func(time):
	mins,secs=divmod(time,60)
	hrs,mins =divmod(mins,60)
	return "%d:%02d:%02d" % (hrs,mins,secs)

filename = "properties.json"	
dictionary={}
dictionary['sys']={}
dictionary['sys']['version']=platform.version()
dictionary['sys']['os']=platform.system()
dictionary['sys']['processor']=platform.processor()
dictionary['sys']['machine_type']=platform.machine()
dictionary['memory']={}
dictionary['memory']['total_space']=str(psutil.disk_usage(".").total>>20)+" MB"
dictionary['memory']['used_space']=str(psutil.disk_usage(".").used>>20)+" MB"
dictionary['memory']['free_memory']=str(psutil.disk_usage(".").free>>20)+" MB"
dictionary['ram']={}
dictionary['ram']['total']=str(psutil.virtual_memory().total>>20)+" MB"
dictionary['ram']['used']=str(psutil.virtual_memory().used>>20)+" MB"
dictionary['ram']['free']=str(psutil.virtual_memory().available>>20)+" MB"
dictionary['user_info']={}
users=psutil.users()
for user in users:
	dictionary['user_info']['username']=user.name
	dictionary['user_info']['teminal']=user.terminal
	dictionary['user_info']['host']=user.host
dictionary['user_info']['hostname']=socket.gethostname()
dictionary['sys']['cpu_count']=psutil.cpu_count()
dictionary['battery_info']={}
dictionary['battery_info']['pecentage']=psutil.sensors_battery().percent
dictionary['battery_info']['time_left']=func(psutil.sensors_battery().secsleft)
with open(filename,"w") as properties:
				json.dump(dictionary, properties,ensure_ascii=False,indent=4)
