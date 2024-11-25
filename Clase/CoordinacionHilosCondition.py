import threading
import time


def preparacion(cond1, contador):
    global cont
    for _ in range(5):
        time.sleep(0.01)
        with cond1:
            cond1.wait()
            print(f"Pedido {contador} completado")
            cont +=1
            cond1.notify()


def procesamiento(cond1, cond2, contador):
    global cont
    for _ in range(5):
        time.sleep(0.01)
        with cond1:
            cond1.wait()
            cond2.wait()
            print(f"Procesamiento {contador} completado")
            cont += 1
            cond2.notify()


def empaque(cond2, contador):
    global cont
    for _ in range(5):
        time.sleep(0.01)
        with cond2:
            cond2.wait()
            print(f"Pedido {contador} completado")
            cont += 1
            cond2.notify()


if __name__ == '__main__':
    condition1 = threading.Condition()
    condition2 = threading.Condition()
    cont = 1

    hilo1 = threading.Thread(target=preparacion, args=(condition1, cont,))
    hilo2 = threading.Thread(target=procesamiento, args=(condition1, condition2, cont,))
    hilo3 = threading.Thread(target=empaque, args=(condition2, cont,))

    hilo1.start()
    hilo2.start()
    hilo3.start()

    with condition1:
        condition1.notify()

    with condition2:
        condition2.notify()

    hilo1.join()
    hilo2.join()
    hilo3.join()