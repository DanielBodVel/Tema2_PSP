import threading

# Lista para almacenar los números primos
numeros_primos = []
# Lock para controlar el acceso a la lista de números primos
lock = threading.Lock()

def calcular_primo(rango_inicio, rango_fin):
    primos_en_rango = []
    
    for num in range(rango_inicio, rango_fin):
        if num < 2:
            continue
        es_primo = True
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                es_primo = False
                break
        if es_primo:
            primos_en_rango.append(num)

    # Bloquea y agrega los primos encontrados a la lista global
    with lock:
        numeros_primos.extend(primos_en_rango)

if __name__ == '__main__':
    hilos = []
    # Crear 10 hilos, cada uno con un rango de 10 números
    for i in range(0, 100, 10):
        hilo = threading.Thread(target=calcular_primo, args=(i, i + 10))
        hilos.append(hilo)
        hilo.start()

    # Espera a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Ordena la lista de números primos y la imprime
    numeros_primos.sort()
    print("Los primeros números primos en el rango de 0 a 100 son:", numeros_primos)