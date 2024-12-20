import os
import random
import readchar

from combate_Pokemon import Combate
from Entrenador import Entrenador
from Pokemon import Pokemon


# Detecta el sistema operativo y utiliza el comando adecuado
def limpiar_consola():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS
        os.system('clear')



POS_X = 0
POS_Y = 1
cant_entrenadores = 3

obstacle_definition = """\
####################
#                  #
#            ##    #
#            ##    #
#    ##            #
#    ##            #
#            ####  #
#            ####  #
#                  #
#        ##        #
#        ##        #
#                  #
#                  #
####################\
"""

#crear pokemon
pikachu = Pokemon("Pikachu", 260, "Surf, Rayo, Psicocarga, Onda Certera", "90,90,80,120")
mimikyu = Pokemon("Mimikyu", 250, "Sombra Vil, Garra Umbria, Tajo Aereo, Cuchillada", "110,80,80,80")
charizard = Pokemon("Charizard", 280, "Llamarada, Lanzallamas, Onda Certera, Pulson Dragon", "110,90,120,80")
blastoise = Pokemon("Blastoise", 300, "Hidrobomba, Cabezazo, Terremoto, Megapatada", "100,80,100,80")
venusaur = Pokemon("Venusaur", 320, "Derribo, Rayo Solar, Tormenta Solar, Bomba Lodo", "60,100,90,80")

#   crear entrenadores
nombre_jugador = input("Ingresa tu nombre: ")

jugador = Entrenador(nombre_jugador, pikachu)   #   Este es el jugador

ash = Entrenador("Ash", mimikyu)
red = Entrenador("Red", charizard)
blue = Entrenador("Blue", blastoise)
green = Entrenador("Green", venusaur)

#   crear combate

mi_posicion = [6, 8]
tail_length = 0
tail = []
entrenadores_en_mapa = []
entrenadores = [ash, red, blue, green]
entrenador_derrotado = []

end_game = False
died = False
gana_combate = False

#   create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# generate random objects

while len(entrenadores_en_mapa) < 3:
    new_position = [random.randint(0, MAP_WIDTH - 2), random.randint(0, MAP_HEIGHT - 2)]

    #   validar que el objeto aparezca en una zona valida del mapa
    if new_position not in entrenadores_en_mapa and new_position != mi_posicion and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
        entrenadores_en_mapa.append(new_position)

#   Main Loop
while not end_game:
    limpiar_consola()
    #   draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in entrenadores_en_mapa:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    if map_object[POS_X] != "#" and map_object[POS_Y] != "#":
                        char_to_draw = "*"
                        object_in_cell = map_object


            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if mi_posicion[POS_X] == coordinate_x and mi_posicion[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    limpiar_consola()
                    oponente = random.choice([ash, red, blue, green])   #   Selecciona entrenador al azar
                    print("\nTe encontraste con un entrenador!\n" + oponente.nombre + " te desafia y lanza a su " + oponente.pokemon.nombre)

                    atacante = jugador.pokemon
                    defensor = oponente.pokemon
                    combate = Combate(atacante,defensor)

                    combate.iniciar(atacante,defensor)

                    if jugador.pokemon.getVida() > 0:
                        print(f"Has derrotado a {oponente.nombre}!")
                        char_to_draw = " "
                        tail_length += 1
                        entrenador_derrotado.append(oponente)
                        entrenadores.remove(oponente)
                        print("Curando a tu pokemon...")
                        atacante.vida = jugador.pokemon.vida_inicial
                        atacante.barras_de_vida()
                    else:
                        print(f"\nQue pena! Has sido derrotado por {oponente.nombre}")
                        died = True
                        end_game = True

                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")


    #   Ask user where he wants to move
    #   direction = input("q dirección tomar? [W/A/S/D]: ")
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, mi_posicion.copy())
        tail = tail[:tail_length]
        mi_posicion[POS_Y] -= 1
        mi_posicion[POS_Y] %= MAP_HEIGHT

    elif direction == "s":
        tail.insert(0, mi_posicion.copy())
        tail = tail[:tail_length]
        mi_posicion[POS_Y] += 1
        mi_posicion[POS_Y] %= MAP_HEIGHT

    elif direction == "a":
        tail.insert(0, mi_posicion.copy())
        tail = tail[:tail_length]
        mi_posicion[POS_X] -= 1
        mi_posicion[POS_X] %= MAP_WIDTH

    elif direction == "d":
        tail.insert(0, mi_posicion.copy())
        tail = tail[:tail_length]
        mi_posicion[POS_X] += 1
        mi_posicion[POS_X] %= MAP_WIDTH

    elif direction == "q":
        end_game = True

    #   Check if the snake hits an obstacle
    if obstacle_definition[mi_posicion[POS_Y]][mi_posicion[POS_X]] == "#":
        end_game = True
        died = True

    limpiar_consola()

if died:
    print("HAS PERDIDO !")


