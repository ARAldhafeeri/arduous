from __future__ import division
from __future__ import annotations
import os
import psutil
import wmi

def gigaHz(num) -> str:
    n = round(num / 1000,2)
    return f"{n}GHz"

def prcnt(num) -> str:
    return f"{num}%"

def gigaByte(num) -> str:
    n = round(num / 10**9, 2)
    return f"{n}GB"

def avg(value_list):
	num = 0
	length = len(value_list)
	for val in value_list:
		num += val
	return num/length

def virtual_memory() -> psutil.virtual_memory:
    return psutil.virtual_memory() 

def swap_memory() -> psutil.swap_memory:
    return psutil.swap_memory()

def cpu_usage() -> str:
    return prcnt(psutil.cpu_percent(interval=1))

def cpu_stats() -> psutil.cpu_stats:
    return psutil.cpu_stats()

def cpu_freq() -> psutil.cpu_freq:
    return psutil.cpu_freq()

def disk() -> list(dict(dict)):
    disks = psutil.disk_partitions()
    disk_io = psutil.disk_io_counters(perdisk=False)
    res = []
    for i in range(len(disks)):
        disk = disks[i]
        disk_usage = psutil.disk_usage(disk.mountpoint)
        temp = {
            "device":disk.device,
            "fstype": disk.device,
            "mountpoint": disk.mountpoint,
            "opts": disk.opts,
            "maxfile": disk.maxfile, 
            "maxpath": disk.mountpoint,
            "disk_usage": {
                "total": disk_usage.total, 
                "used": disk_usage.used, 
                "percent": prcnt(disk_usage.percent)
            }, 
            "disk_io": {
                "read_count": disk_io.read_count, 
                "write_count": disk_io.write_count, 
                "write_bytes": disk_io.write_bytes,
                "read_bytes": disk_io.read_bytes, 
                "read_time": disk_io.read_time, 
                "write_time": disk_io.write_time
            }
        }
        res.append(temp)
    return res
        


def network_io() -> dict :
    return  psutil.net_io_counters(pernic=True)

def network_conn() -> dict:
    return psutil.net_connections(kind='tcp')



def network_addr() -> psutil.net_if_addrs:
    return psutil.net_if_addrs()

def network_stats() -> psutil.net_if_stats:
    return psutil.net_if_stats()

# only for linux 

def temp() -> psutil.sensors_temperatures:
   return psutil.sensors_temperatures()

def fans() -> psutil.sensors_fans:
    return psutil.sensors_fans()

def power() -> psutil.sensors_batter:
    return psutil.sensors_battery()

def boot_time() -> psutil.boot_time:
    return psutil.boot_time()

def proc() -> list(dict(dict)):
    res = []
    processes = psutil.pids()
    
    for process in processes:
        p = psutil.Process(process)
        temp = {
            "name": p.name(), "exe": p.exe(), "cwd": p.cwd(), "cmdline": p.cmdline(), "process_childreen": p.children(),
            "cpu_times": p.cpu_times(), "process_cpu_precent": p.cpu_percent(), "real_USS_MEMORY_UESAGE_WIN_LINUX_ONLY": p.memory_full_info(),
            "io_counters": p.io_counters(), "process_connections": p.connections(kind="tcp"), "num_threads": p.threads(),
            "process_user": p.username()
        }
        res.append(temp)

    return res


