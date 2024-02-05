import psutil

PID = input("Ingresa el PID: ")

proceso = psutil.Process(int(PID))
nombre = proceso.name()
ram_mb = proceso.memory_info().rss / 1024 / 1024
cpu = proceso.cpu_percent(interval=1) / len(proceso.threads())
ruta = proceso.exe()
usuario = proceso.username()
estado = proceso.status()

print(f"El nombre del proceso es: {nombre}")
print(f"La ruta del proceso es: {ruta}")
print(f"La RAM del proceso es: {ram_mb} MB")
print(f"El CPU del proceso es: {cpu}%")
print(f"El usuario del proceso es: {usuario}")
print(f"El estado del proceso es: {estado}")
