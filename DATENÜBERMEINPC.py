import platform
import socket
import psutil

def get_system_info():
    system_info = {}

    # Betriebssystem-Informationen
    system_info["System"] = platform.system()
    system_info["Release"] = platform.release()
    system_info["Version"] = platform.version()

    # Hostname
    system_info["Hostname"] = socket.gethostname()

    # IP-Adresse
    system_info["IP-Adresse"] = socket.gethostbyname(system_info["Hostname"])

    # CPU-Informationen
    system_info["Prozessor"] = platform.processor()
    system_info["Anzahl der CPU-Kerne"] = psutil.cpu_count(logical=False)
    system_info["Anzahl der logischen CPUs"] = psutil.cpu_count(logical=True)

    # Arbeitsspeicher (RAM)
    mem = psutil.virtual_memory()
    system_info["Installierter RAM"] = f"{mem.total / (1024**3):.2f} GB"

    # Festplattenplatz
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        system_info[f"Festplatte ({partition.device})"] = f"{partition_info.total / (1024**3):.2f} GB frei"

    return system_info

if __name__ == "__main__":
    my_system_info = get_system_info()

    print("Informationen über dein Gerät:")
    for key, value in my_system_info.items():
        print(f"{key}: {value}")

