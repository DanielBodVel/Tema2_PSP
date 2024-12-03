import random
import threading
import time

def acceder_estacionamiento(id_vehiculo):
    semaforo.acquire()
    print(f"Coche {id_vehiculo} ha entrado en el estacionamiento.")
    time.sleep(random.uniform(1, 3))
    print(f"Coche {id_vehiculo} ha salido del estacionamiento")
    semaforo.release()

if __name__ == '__main__':
    semaforo = threading.Semaphore(3)
    coches = []

    for i in range(1, 11):
        hilo = threading.Thread(target=acceder_estacionamiento, args=(i,))
        coches.append(hilo)
        hilo.start()

    for hilo in coches:
        hilo.join()

    print("No hay más coches")