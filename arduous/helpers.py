from __future__ import annotations
from arduous.messenger import messenger

def trace_here(            
    logger_subs_activate,
    logger: bool = True,
    virtual_memory: bool = True,
    swap_memory: bool = True,
    cpu_usage: bool = True,
    cpu_freq: bool = True,
    cpu_stats: bool = True,
    disk: bool = True,
    network: bool = True,
    temp: bool = True,
    fans: bool = True,
    power: bool = True,
    boot_time: bool = True,
    process: bool = True,
    real_time_vis: bool = True
    ):
        if logger : logger_subs_activate()

        # memory logs events
        if swap_memory : messenger.publish("swap_memorys_log")

        if virtual_memory :  messenger.publish("virtual_memory_log")
        
        # cpu logs
        if cpu_usage :  messenger.publish("cpu_usage_log")
        
        if cpu_freq :  messenger.publish("cpu_freq_log")

        if cpu_stats : messenger.publish("cpu_stats_log")

        # disk logs events
        if disk :  messenger.publish("disk_log")

        # network logs events
        if network :  messenger.publish("network_io_log")

        if network :  messenger.publish("network_conn_log")

        if network :  messenger.publish("network_addr_log")

        if network :  messenger.publish("network_stats_log")

        # other events temp, fans, power, boot_time, process
        if temp :  messenger.publish("temp_log")

        if fans :  messenger.publish("fans_log")

        if power :  messenger.publish("power_log")

        if boot_time :  messenger.publish("boot_time_log")

        if process :  messenger.publish("proc_log")
