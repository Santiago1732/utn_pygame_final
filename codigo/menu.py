import pygame
import sys
from bdd import *

class Menu():
    def __init__(self, nombre_jugador, sonido_activado):
        super().__init__()
        self.nombre_jugador = nombre_jugador
        self.sonido_activado = sonido_activado


# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Santiago Oliveira - UTN - TP Pygame ')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

def main_menu(self):
    '''
    Representa el menú principal del juego. Muestra opciones como jugar, opciones y salir, y maneja las acciones del usuario en el menú.
    :param self:
    :return:
    '''
    menu = Menu('None',True)
    sonido_activado = True
    nombre_jugador = ''
    while True:
        screen.fill(WHITE)
        dibujar_texto('Main Menu', font, BLACK, screen, 20, 20)
        dibujar_texto('1. Jugar', font, BLACK, screen, 20, 100)
        dibujar_texto('2. Opciones', font, BLACK, screen, 20, 140)
        dibujar_texto('3. Salir', font, BLACK, screen, 20, 180)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:

                    # NOMBRE JUGADOR
                    case pygame.K_1:
                        menu.nombre_jugador = pantalla_de_juego(sonido_activado)
                        return menu

                    # OPCIONES
                    case pygame.K_2:
                        menu.sonido_activado = pantalla_de_opciones()

                    # SALIR
                    case pygame.K_3:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


def pantalla_de_juego(self, sonido_activado = True):
    '''
     Esta función representa la pantalla del juego y permite al jugador ingresar su nombre. Devuelve el nombre del jugador.
    :param self:
    :param sonido_activado:
    :return:
    '''
    running = True
    while running:
        screen.fill(WHITE)
        player_name = text_input()

        if player_name is not None:
            return player_name

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.nombre_jugador = pantalla_de_juego(sonido_activado)
                    pygame.display.update()


sonido_activado = True
def pantalla_de_opciones():
    '''
    representa la pantalla de opciones donde el jugador puede activar o desactivar el sonido y volver al menú principal.
    :return:
    '''
    global sonido_activado  # Usar la variable global

    while True:
        screen.fill(WHITE)
        dibujar_texto(' - OPCIONES- ', font, BLACK, screen, 20, 20)
        dibujar_texto('2) Atras', font, BLACK, screen, 20, 140)

        if sonido_activado:
            dibujar_texto('1) Desactivar Sonido', font, BLACK, screen, 20, 100)
        else:
            dibujar_texto('1) Activar Sonido', font, BLACK, screen, 20, 100)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sonido_activado = not sonido_activado
                elif event.key == pygame.K_2:
                    return sonido_activado

        pygame.display.update()


def text_input():
    '''
    Permite al jugador ingresar su nombre y maneja las entradas de teclado. Devuelve el nombre ingresado.
    :return:
    '''
    nombre_jugador = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.K_ESCAPE:
            #     main_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                    return nombre_jugador

                elif event.key == pygame.K_ESCAPE:
                    main_menu()
                elif event.key == pygame.K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]
                else:
                    nombre_jugador += event.unicode

        screen.fill(WHITE)
        dibujar_texto("Ingrese su nombre:", font, BLACK, screen, 20, 20)
        dibujar_texto(nombre_jugador, font, BLACK, screen, 20, 80)

        dibujar_texto('Enter -> Jugar:', font, BLACK, screen, 20, 120)
        pygame.display.flip()

    return nombre_jugador


def dibujar_texto(text, font, color, surface, x, y):
    '''
    dibuja texto en una superficie Pygame con la fuente, color y posición especificados.
    :param text:
    :param font:
    :param color:
    :param surface:
    :param x:
    :param y:
    :return:
    '''
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def mostrar_puntuaciones(screen):
    '''
    muestra las puntuaciones de los jugadores guardades en una base de datos ventana.
    :param screen:
    :return:
    '''
    conn = sqlite3.connect('../base_de_datos/database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jugador")
    column_names = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont('../graficos/fuentes/HOLIDAYZONE.ttf',24)

    screen.fill(BLACK)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        y = 0

        column_text = ' | '.join(column_names)
        text_surface = font.render(column_text, True, WHITE)
        screen.blit(text_surface, (50, y))
        y += 30  # Ajusta la posición y para la primera fila de datos

        for row in rows:
            text = font.render(str(row), True, WHITE)
            screen.blit(text, (100, y))
            y += 30

        pygame.display.flip()

    pygame.quit()


# Bucle principal
def main():
    while True:
        main_menu()

if __name__ == '__main__':
    main()

