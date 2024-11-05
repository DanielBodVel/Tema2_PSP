import threading

lock = threading.Lock()


def calcularPrimos(num):
    global n
    for n in range(2, num):
        with lock:
            if num % n == 0:
                print(n, "Es primo")
            else:
                print("No es primo", n, "es divisor")


if __name__ == '__main__':
    print("Introduce para calcular los num primos hasta ese num: ")
    n = int(input())

    hilos = []

    if n < 10:
        for i in range(n):
            hilo = threading.Thread(target=calcularPrimos(n))
            hilos.append(hilo)
            hilo.start()
    else:
        for i in range(10):
            hilo = threading.Thread(target=calcularPrimos(n))
            hilos.append(hilo)
            hilo.start()

    for hilo in hilos:
        hilo.join()