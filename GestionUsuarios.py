import threading
import time


def procesar_usuario (id, nombreIn, edadIn):
    time.sleep(2)
    print(f"Mi id es: {id}, ni nombre es: {nombreIn} y mi edad es {edadIn}")


if __name__ == '__main__':

    hilos = []
    ids = [100, 200, 300, 400, 500]
    nombres = ["Daniel", "David", "Juan", "Claudia", "Abel"]
    edades = [21, 20, 19, 18, 17]

    for i in range(5):
        nombre = nombres[i - 1]
        edad = edades[i - 1]
        #TODO: Porque hay que poner una coma en args para que funcione
        hilo = threading.Thread(target=procesar_usuario, args=(ids[i-1],), kwargs={'nombreIn': nombre, 'edadIn': edad})
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

print("Fin de ejecución")
