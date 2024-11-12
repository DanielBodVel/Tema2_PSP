import threading

hilos = []

archivo1 = "\n\n\n"
archivo2 = "\n\n\n"
archivo3 = "\n\n\n"

nombresArchivo = [archivo1, archivo2, archivo3]


class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombreArchivo):
        super().__init__()
        self.nombreArchivo = nombreArchivo

    def run(self):
        contadorLinea = 0
        for i in len(nombresArchivo):
            for f in nombresArchivo[i]:
                if f == "\n":
                    contadorLinea +=1


if __name__ == '__main__':
    for i in nombresArchivo:
        hilo = ProcesadorArchivo(nombreArchivo=nombresArchivo)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
