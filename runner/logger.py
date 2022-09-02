import runner.utilties  as utils 

class ArduousLogger:
    def __init__(self, logger, *args, **kwargs):
        self.logger = logger;

    def virtual_memory_log(self):
        mem_vir = utils.virtual_memory()
        self.logger.info("[[ VIRTUAL MEMORY REAL-TIME STATS ]]...")
        self.logger.info(f"[TOTAL MEMORY ]: {utils.gigaByte(mem_vir.total)}")
        self.logger.info(f"[USED MEMORY ]: {utils.gigaByte(mem_vir.used)}")
        self.logger.info(f"[AVAILABLE MEMORY ]: {utils.gigaByte(mem_vir.available)}")
        self.logger.info(f"[FREE MEMORY ]: {utils.gigaByte(mem_vir.free)}")
        self.logger.info(f"[MEMORY USAGE]: {utils.prcnt(mem_vir.percent)}")

    def swap_memorys_log(self):
        mem_swap = utils.swap_memory()
        self.logger.info("[[ SWAP MEMORY REAL-TIME STATS ]]...")
        self.logger.info(f"[TOTAL ]: {utils.gigaByte(mem_swap.total)}")
        self.logger.info(f"[USED  ]: {utils.gigaByte(mem_swap.used)}")
        self.logger.info(f"[SIN  ]: {mem_swap.sin}")
        self.logger.info(f"[SOUT  ]: {utils.gigaByte(mem_swap.sout)}")
        self.logger.info(f"[USAGE ]: {utils.prcnt(mem_swap.percent)}")

    def cpu_usage_log(self):
        cpu_use = utils.cpu_usage
        self.logger.info(f"[ CPU USAGE PRECENTAGE ] {utils.prcnt(cpu_use)}")


    def cpu_stats_log(self):
        cpu_stats = utils.cpu_stats()
        self.logger.info(f"[ CPU STATS ]: Context swtiches: {cpu_stats.ctx_switches}  ")
        self.logger.info(f"[ CPU STATS ]: interrupts: {cpu_stats.interrupts}  ")
        self.logger.info(f"[ CPU STATS ]: soft_interrupts: {cpu_stats.soft_interrupts}  ")
        self.logger.info(f"[ CPU STATS ]: syscalls: {cpu_stats.syscalls}  ")

    def cpu_freq_log(self):
        cpu_freq = utils.cpu_freq()
        self.logger.info(f"[ CPU BASE SPEED ]: {utils.gigaHz(cpu_freq.current)} - [ CPU MAX SPEED ]: {utils.gigaHz(cpu_freq.max)} - [ CPU MIN SPEED ]: {utils.gigaHz(cpu_freq.min)} %")


    def disk_log(self):
        disks = utils.disk()
        for disk in disks:
            self.logger.info("[[ DISK PARTITIONS REAL-TIME STATS ]]...")
            self.logger.info(f"[DISK PARTITION ]: device: {disk['device']}")
            self.logger.info(f"[DISK PARTITION ]: mountpoint: {disk['mountpoint']}")
            self.logger.info(f"[DISK PARTITION ]: fstype: {disk['fstype']}")
            self.logger.info(f"[DISK PARTITION ]: opts: {disk['opts']}")
            self.logger.info(f"[DISK PARTITION ]: maxfile: {disk['maxfile']}")
            self.logger.info(f"[DISK PARTITION ]: maxpath: {disk['mountpoint']}")
            
            self.logger.info(f"[DISK PARTITION USAGE ]: total: {utils.gigaByte(disk['disk_usage']['total'])}")
            self.logger.info(f"[DISK PARTITION USAGE ]: used: {utils.gigaByte(disk['disk_usage']['used'])}")
            self.logger.info(f"[DISK PARTITION USAGE ]: free: {utils.prcnt(disk['disk_usage']['percent'])}")
            
            self.logger.info(f"[DISK IO COUNTERS ]: read_count: {disk['disk_io']['read_count']}")
            self.logger.info(f"[DISK IO COUNTERS ]: write_count: {disk['disk_io']['write_count']}")
            self.logger.info(f"[DISK IO COUNTERS ]: read_bytes: {disk['disk_io']['read_bytes']}")
            self.logger.info(f"[DISK IO COUNTERS ]: write_bytes: {disk['disk_io']['write_bytes']}")
            self.logger.info(f"[DISK IO COUNTERS ]: read_time: {disk['disk_io']['read_time']}")
            self.logger.info(f"[DISK IO COUNTERS ]: write_time: {disk['disk_io']['write_time']}")

            
    def network_io_log(self):
        net_io = utils.network_io()
        for key in net_io.keys():
            conn = net_io[key]
            self.logger.info(f"[[ NETWORK IO TO THE FIRST EHTERNET INTERFACE {key} ]]...")
            self.logger.info(f"[ {key} NETOWRK IO ]: bytes_sent: {utils.gigaByte(conn.bytes_sent)}")
            self.logger.info(f"[ {key}  NETOWRK IO ]: bytes_recv: {utils.gigaByte(conn.bytes_recv)}")
            self.logger.info(f"[ {key}  NETOWRK IO ]: packets_sent: {conn.packets_sent} bits per second")
            self.logger.info(f"[ {key}  NETOWRK IO ]: packets_recv: {conn.packets_recv} bits per second")
            self.logger.info(f"[ {key}  NETOWRK IO ]: errin: {conn.errin}")
            self.logger.info(f"[ {key}  NETOWRK IO ]: errout: {conn.errout}")
            self.logger.info(f"[ {key}  NETOWRK IO ]: dropin: {conn.dropin}")
            self.logger.info(f"[ {key}  NETOWRK IO ]: dropout: {conn.dropout}")
            

    def network_conn_log(self):
        net_conn = utils.network_conn()
        for nc in net_conn:
            self.logger.info("[[ NETWORK TCP CONNECTIONS ]]...")
            self.logger.info(f"[TCP CONNECTION ]: fd: {nc.fd}")
            self.logger.info(f"[TCP CONNECTION ]: family: {nc.family}")
            self.logger.info(f"[TCP CONNECTION ]: type: {nc.type}")
            self.logger.info(f"[TCP CONNECTION ]: laddr: {nc.laddr}")
            self.logger.info(f"[TCP CONNECTION ]: raddr: {nc.raddr}")
            self.logger.info(f"[TCP CONNECTION ]: status: {nc.status}")
            self.logger.info(f"[TCP CONNECTION ]: pid: {nc.pid}")




    def network_addr_log(self):
        net_if_addr = utils.network_addr()
        for key in net_if_addr.keys():
            for conn in net_if_addr[key]:
                self.logger.info(f"[[ NETWORK ADDRESS {key} ]]...")
                self.logger.info(f"[ {key} CONNECTIONS ]: family: {conn.family}")
                self.logger.info(f"[ {key} CONNECTIONS ]: address: {conn.address}")
                self.logger.info(f"[ {key} CONNECTIONS ]: netmask: {conn.netmask}")
                self.logger.info(f"[ {key} CONNECTIONS ]: broadcast: {conn.broadcast}")
                self.logger.info(f"[ {key} CONNECTIONS ]: ptp: {conn.ptp}")
                

    def network_stats_log(self):
        net_stats = utils.network_stats()
        for key in net_stats.keys():
            conn = net_stats[key]
            self.logger.info(f"[[ NETWORK STATS {key} ]]...")
            self.logger.info(f"[ {key} CONNECTIONS ]: isup: {conn.isup}")
            self.logger.info(f"[ {key} CONNECTIONS ]: duplex: {conn.duplex}")
            self.logger.info(f"[ {key} CONNECTIONS ]: speed: {conn.speed}")
            self.logger.info(f"[ {key} CONNECTIONS ]: mtu: {conn.mtu}")

    def temp_log(self):
        temp_stats = utils.temp()
        self.logger.info(f"[[ TEMPERATUES STATS]]...")
        self.logger.info(f"[  CPU ]: label: {temp_stats['cpu']}")
        self.logger.info(f"[  GPU ]: label: {temp_stats['gpu']}")



    def fans_log(self):
        fans_stats = utils.fans()
        for key in fans_stats.keys(self):
            for fan in fans_stats[key]:
                self.logger.info(f"[[ FANS STATS {key} ]]...")
                self.logger.info(f"[  {key} ]: label: {fan.label}")
                self.logger.info(f"[  {key} ]: current: {fan.current}")
              

    def power_log(self):
        power_stats = utils.fans()
        for ps in power_stats:
            self.logger.info(f"[[ BATTERY STATS ]]...")
            self.logger.info(f"[  ]: label: {utils.prcnt(ps.percent)}")
            self.logger.info(f"[  ]: secsleft: {ps.secsleft}")
            self.logger.info(f"[  ]: power_plugged: {ps.power_plugged}")

    def boot_time_log(self):
        boottime = utils.boot_time()
        self.logger.info(f"[[ BOOT TIME  ]]...")
        self.logger.info(f"[  ]: label: {boottime} s")

    def proc_log(self):
        processes = utils.proc()
        for p in processes:
            self.logger.info(f"[[ System processes  ]]...")
            self.logger.info(f"[  process {p.name}]: label: {p}")
