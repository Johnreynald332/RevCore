import platform as p
import psutil as ps
import socket

def command():
    os_system = p.system()
    return os_system

def release():
    os_release = p.release()
    return f"os version {os_release}"

def check_cpu():
    os_cpu_count = ps.cpu_count()
    os_percent = ps.cpu_percent()
    return dict(count=os_cpu_count, percent=os_percent)

def check_drive():
    os_drive = ps.disk_partitions()
    return os_drive

def check_id():
    for prs in ps.process_iter(["pid","name"]):
        print(prs.info)

def system_information():
    os_user = ps.users()
    os_boot_time = ps.boot_time()
    return dict(user=os_user, os_boot_time=os_boot_time)

def check_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('8.8.8.8', 80))
        print(s.getsockname()[0])
    except Exception as e:
        print(e)

def check_battery():
    battery = ps.sensors_battery()
    return battery

def c_drive():
    ch_d = ps.virtual_memory().total
    x_f = int(str(ch_d)[0])
    return x_f

