import threading

def preparacion():
    global contador
    for i in range(1, total_iteraciones + 1):
        with condicion:
            condicion.wait_for(lambda: contador == 1)  # Espera su turno
            print(f"Preparación {i} completada")
            contador = 2  # Actualiza al siguiente paso
            condicion.notify_all()  # Notifica a los demás hilos


def procesamiento():
    global contador
    for i in range(1, total_iteraciones + 1):
        with condicion:
            condicion.wait_for(lambda: contador == 2)  # Espera su turno
            print(f"Procesamiento {i} completado")
            contador = 3  # Actualiza al siguiente paso
            condicion.notify_all()  # Notifica a los demás hilos


def empaque():
    global contador
    for i in range(1, total_iteraciones + 1):
        with condicion:
            condicion.wait_for(lambda: contador == 3)  # Espera su turno
            print(f"Empaque {i} completado")
            contador = 1  # Reinicia el contador para el próximo ciclo
            condicion.notify_all()  # Notifica a los demás hilos


if __name__ == '__main__':
    contador = 1
    condicion = threading.Condition()
    total_iteraciones = 5

    hilo_preparacion = threading.Thread(target=preparacion)
    hilo_procesamiento = threading.Thread(target=procesamiento)
    hilo_empaque = threading.Thread(target=empaque)

    hilo_preparacion.start()
    hilo_procesamiento.start()
    hilo_empaque.start()

    hilo_preparacion.join()
    hilo_procesamiento.join()
    hilo_empaque.join()
