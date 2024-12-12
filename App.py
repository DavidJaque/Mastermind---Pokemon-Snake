import os
import random
import readchar

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



mi_posicion = [6, 8]
tail_length = 0
tail = []
entrenadores_en_mapa = []
entrenador_derrotado = []

end_game = False
died = False
gana_combate = False

#   create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

#   Main Loop
while not end_game:
    os.system("cls")
    #generate random objects

    while len(entrenadores_en_mapa) < cant_entrenadores:
        new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

        if new_position not in entrenadores_en_mapa and new_position != mi_posicion and new_position not in entrenador_derrotado:
            entrenadores_en_mapa.append(new_position)


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
                    char_to_draw = "*"
                    object_in_cell = map_object


            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if mi_posicion[POS_X] == coordinate_x and mi_posicion[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    entrenadores_en_mapa.remove(object_in_cell)
                    tail_length +=1

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

    os.system("cls")

if died:
    print("HAS PERDIDO !")