import threading
import time

datos_sesion = threading.local()


def iniciar_sesion(nombre_usuario):
    datos_sesion = nombre_usuario
    time.sleep(2)
    mostrar_sesion(datos_sesion)


def mostrar_sesion(datos):
    print(f"Sesión iniciada para el usu: {datos}")


if __name__ == '__main__':
    nombres = ["Daniel", "David", "Juan", "Claudia", "Abel"]
    hilos = []
    for nombre in nombres:
        hilo = threading.Thread(target=iniciar_sesion, args=(nombre,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
