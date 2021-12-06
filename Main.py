import pygame as py
import threading
import time

class Fortuna:
    def __init__(self, ventana):
        # Colores
        self.fondo = (202, 240, 248)
        self.libre = (144, 224, 239)
        self.ocupado = (10, 138, 161)
        self.rueda = (0, 20, 59)
        self.lineas = (3, 36, 102)
        self.ventana = ventana

    def dibujar(self):
        # rueda
        py.draw.circle(self.ventana, self.rueda, (450, 250), 180, 5)
        py.draw.circle(self.ventana, self.fondo, (455, 255), 10)
        py.draw.line(self.ventana, self.lineas, (450, 70), (450, 430), 4)
        py.draw.line(self.ventana, self.lineas, (300, 160), (600, 345), 4)
        py.draw.line(self.ventana, self.lineas, (600, 140), (310, 360), 4)
        py.draw.circle(self.ventana, self.lineas, (450, 255), 20)
        py.draw.circle(self.ventana, self.fondo, (450, 255), 15)
        py.draw.circle(self.ventana, self.lineas, (450, 255), 10)
        py.draw.circle(self.ventana, self.fondo, (450, 255), 3)

        # Asientos
        self.silla_1 = py.draw.circle(self.ventana, self.libre, (310, 360), 35)
        self.silla_2 = py.draw.circle(self.ventana, self.libre, (300, 155), 35)
        self.silla_3 = py.draw.circle(self.ventana, self.libre, (453, 75), 35)
        self.silla_4 = py.draw.circle(self.ventana, self.libre, (596, 145), 35)
        self.silla_5 = py.draw.circle(self.ventana, self.libre, (450, 420), 35)
        self.silla_6 = py.draw.circle(self.ventana, self.libre, (600, 340), 35)

        py.draw.circle(self.ventana, self.rueda, (310, 360), 35, 4)
        py.draw.circle(self.ventana, self.rueda, (300, 155), 35, 4)
        py.draw.circle(self.ventana, self.rueda, (453, 75), 35, 4)
        py.draw.circle(self.ventana, self.rueda, (596, 145), 35, 4)
        py.draw.circle(self.ventana, self.rueda, (450, 420), 35, 4)
        py.draw.circle(self.ventana, self.rueda, (600, 340), 35, 4)

    def botones(self, boton, titulo):
        tipo_Letra = py.font.SysFont('Calibri', 20)

        if boton.collidepoint(py.mouse.get_pos()):
            py.draw.rect(self.ventana, (41, 99, 189), boton, 0)
        else:
            py.draw.rect(self.ventana, (0, 20, 59), boton, 0)
        texto = tipo_Letra.render(titulo, True, (202, 240, 248))

        self.ventana.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
                                  boton.y+(boton.height-texto.get_height())/2))

    def actualizar(self, opcion):
        if opcion == 0:
            py.draw.circle(self.ventana, self.ocupado, (310, 360), 35)
        elif opcion == 1:
            py.draw.circle(self.ventana, self.ocupado, (310, 360), 35)
            py.draw.circle(self.ventana, self.ocupado, (300, 155), 35)
        elif opcion == 2:
            py.draw.circle(self.ventana, self.ocupado, (310, 360), 35)
            py.draw.circle(self.ventana, self.ocupado, (300, 155), 35)
            py.draw.circle(self.ventana, self.ocupado, (453, 75), 35)
        elif opcion == 3:
            py.draw.circle(self.ventana, self.ocupado, (310, 360), 35)
            py.draw.circle(self.ventana, self.ocupado, (300, 155), 35)
            py.draw.circle(self.ventana, self.ocupado, (453, 75), 35)
            py.draw.circle(self.ventana, self.ocupado, (596, 145), 35)
        elif opcion == 4:
            py.draw.circle(self.ventana, self.ocupado, (310, 360), 35)
            py.draw.circle(self.ventana, self.ocupado, (300, 155), 35)
            py.draw.circle(self.ventana, self.ocupado, (453, 75), 35)
            py.draw.circle(self.ventana, self.ocupado, (596, 145), 35)
            py.draw.circle(self.ventana, self.ocupado, (600, 340), 35)
        elif opcion == 5:
            py.draw.circle(self.ventana, self.ocupado, (310, 360), 35)
            py.draw.circle(self.ventana, self.ocupado, (300, 155), 35)
            py.draw.circle(self.ventana, self.ocupado, (453, 75), 35)
            py.draw.circle(self.ventana, self.ocupado, (596, 145), 35)
            py.draw.circle(self.ventana, self.ocupado, (600, 340), 35)
            py.draw.circle(self.ventana, self.ocupado, (450, 420), 35)


asientosL = [1, 1, 1, 1, 1, 1]
ocupados = []

class Situacion(threading.Thread):
    def __init__(self, asientos, num_Personas):
        threading.Thread.__init__(self)
        asientos[num_Personas] = threading.Semaphore(1)
        self.asientos = asientos
        self.num_Personas = num_Personas

    def run(self):
        print(" + Persona ", self.num_Personas, "Sube al Juego")
        self.asientos[self.num_Personas].acquire()
        ocupados.append(self.num_Personas)
        print(ocupados)
        if len(ocupados) == 6:
            for _ in range(6):
                print("---Girando---")
                self.asientos[self.num_Personas].release()
                time.sleep(2)

            for person in ocupados:
                print("Persona ", person, "Bajando del juego")
                self.asientos[self.num_Personas].acquire()
                time.sleep(2)
        
            for person in range(len(asientosL)):
                print("Lugar ", person, "Libre")
                self.asientos[self.num_Personas].release()
                time.sleep(2)
            
            ocupados.clear()
            

def main():
    ventana = py.display.set_mode((800, 500))
    ventana.fill((202, 240, 248))
    # Clase dibujo
    ruedas = Fortuna(ventana)
    # botones
    boton1 = py.Rect(45, 200, 100, 40)
    ocupado = (10, 138, 161)
    run = True
    contador = (0-1)
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                if boton1.collidepoint(py.mouse.get_pos()):
                    contador += 1
                    hilos = Situacion(asientosL, contador)
                    hilos.start()
                    hilos.join()

        ruedas.dibujar()
        ruedas.botones(boton1, "Subir")
        ruedas.actualizar(contador)
        if contador == 5:
            contador = (0-1)
    
        py.display.flip()


if __name__ == '__main__':
    py.init()
    main()
    py.quit()
