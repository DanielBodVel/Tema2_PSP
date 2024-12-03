import threading
import time
from random import randint


def carrera(numCorredor):
    print(f"Corredor {numCorredor} en posición, esperando señal de salida...")
    evento.wait()
    time.sleep(randint(1,3))
    print(f"Corredor {numCorredor} ha llegado a la meta.")


def pistoletazo():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)
    print("¡Salida! Los corredores han comenzado.")
    evento.set()


if __name__ == '__main__':
    corredores = []
    evento = threading.Event()
    for i in range(0, 5):
        corredor = threading.Thread(target=carrera, args=(i,))
        corredores.append(corredor)
        corredor.start()

    pistola = threading.Thread(target=pistoletazo)
    pistola.start()

    for corredor in corredores:
        corredor.join()

    pistola.join()
