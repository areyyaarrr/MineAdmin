import psutil

def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "net": psutil.net_io_counters().bytes_sent
    }
