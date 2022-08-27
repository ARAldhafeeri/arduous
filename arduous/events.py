from arduous.messenger import messenger


class LoggerEvents:
    def __init__(self, arduous_logger, *args, **kwargs) -> None:
        self.arduous_logger = arduous_logger

    def logger_subs_activate(self):

        messenger.subscribe("virtual_memory_log", self.arduous_logger.virtual_memory_log)

        messenger.subscribe("swap_memorys_log", self.arduous_logger.swap_memorys_log)

        messenger.subscribe("cpu_usage_log", self.arduous_logger.cpu_usage_log)

        messenger.subscribe("cpu_stats_log", self.arduous_logger.cpu_stats_log)

        messenger.subscribe("cpu_freq_log", self.arduous_logger.cpu_freq_log)

        messenger.subscribe("disk_log", self.arduous_logger.disk_log)

        messenger.subscribe("network_io_log", self.arduous_logger.network_io_log)

        messenger.subscribe("network_conn_log", self.arduous_logger.network_conn_log)

        messenger.subscribe("network_addr_log", self.arduous_logger.network_addr_log)

        messenger.subscribe("network_stats_log", self.arduous_logger.network_stats_log)

        messenger.subscribe("temp_log", self.arduous_logger.temp_log)

        messenger.subscribe("fans_log", self.arduous_logger.fans_log)

        messenger.subscribe("power_log", self.arduous_logger.power_log)

        messenger.subscribe("boot_time_log", self.arduous_logger.boot_time_log)

        messenger.subscribe("proc_log", self.arduous_logger.proc_log)



    def logger_shut_down_all(self):

        messenger.update("virtual_memory_log", self.arduous_logger.virtual_memory_log)

        messenger.update("swap_memorys_log", self.arduous_logger.swap_memorys_log)

        messenger.update("cpu_usage_log", self.arduous_logger.cpu_usage_log)

        messenger.update("cpu_stats_log", self.arduous_logger.cpu_stats_log)

        messenger.update("cpu_freq_log", self.arduous_logger.cpu_freq_log)

        messenger.update("disk_log", self.arduous_logger.disk_log)

        messenger.update("network_io_log", self.arduous_logger.network_io_log)

        messenger.update("network_conn_log", self.arduous_logger.network_conn_log)

        messenger.update("network_addr_log", self.arduous_logger.network_addr_log)

        messenger.update("network_stats_log", self.arduous_logger.network_stats_log)

        messenger.update("temp_log", self.arduous_logger.temp_log)

        messenger.update("fans_log", self.arduous_logger.fans_log)

        messenger.update("power_log", self.arduous_logger.power_log)

        messenger.update("boot_time_log", self.arduous_logger.boot_time_log)

        messenger.update("proc_log", self.arduous_logger.proc_log)


    def update_single_log_event(event, callback):
        messenger.update(event, callback)