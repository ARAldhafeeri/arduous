from __future__ import annotations
from runner.messenger import messenger

def trace(            
            logger_subs_activate,
            logger: bool = True,
            virtual_memory: bool = False,
            swap_memory: bool = False,
            cpu_usage: bool = False,
            cpu_freq: bool = False,
            cpu_stats: bool = False,
            disk: bool = False,
            network: bool = False,
            temp: bool = False,
            fans: bool = False,
            power: bool = False,
            boot_time: bool = False,
            process: bool = False,
            all: bool = False
            ):
    if logger : logger_subs_activate()

    # memory logs events
    if swap_memory or all : messenger.publish("swap_memorys_log")

    if virtual_memory or all :  messenger.publish("virtual_memory_log")

    # cpu logs
    if cpu_usage or all  :  messenger.publish("cpu_usage_log")

    if cpu_freq or all:  messenger.publish("cpu_freq_log")

    if cpu_stats or all  : messenger.publish("cpu_stats_log")

    # disk logs events
    if disk or all :  messenger.publish("disk_log")

    # network logs events
    if network or all:  messenger.publish("network_io_log")

    if network or all:  messenger.publish("network_conn_log")

    if network or all :  messenger.publish("network_addr_log")

    if network  or all:  messenger.publish("network_stats_log")

    # other events temp, fans, power, boot_time, process
    if temp or all :  messenger.publish("temp_log")

    if fans or all:  messenger.publish("fans_log")

    if power or all:  messenger.publish("power_log")

    if boot_time  or all:  messenger.publish("boot_time_log")

    if process or all :  messenger.publish("proc_log")