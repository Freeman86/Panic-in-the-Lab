
from random import shuffle
from variables import *
from classes import *

def create_amebas():  # создаем 16 амёб
    eyes, pattern, color = 0, 0, 0
    for num in range(16):
        ameba_list.append(Ameba())
        if num <= 1:
            eyes, pattern, color = 0, 0, 0
        elif num > 1 and num <= 3:
            eyes, pattern, color = 1, 1, 1
        elif num > 3 and num <= 5:
            eyes, pattern = 0, 0
            color = 1
        elif num > 5 and num <= 7:
            eyes, pattern = 1, 1
            color = 0
        elif num > 7 and num <= 9:
            eyes, color = 1, 1
            pattern = 0
        elif num > 9 and num <= 11:
            eyes, color = 0, 0
            pattern = 1
        elif num > 11 and num <= 13:
            pattern, color = 1, 1
            eyes = 0
        elif num > 13 and num <= 15:
            pattern, color = 0, 0
            eyes = 1
        ameba_list[num].eyes = ameba_eyes[eyes]
        ameba_list[num].color = ameba_color[color]
        ameba_list[num].pattern = ameba_pattern[pattern]
        ameba_list[num].number = num + 1

    return ameba_list

def create_units():  # создаем игровые объекты: три вентиляции, три лаборатории и три комнаты мутации
    for num in range(3):
        ventilation_list.append(Ventilation())

        lab_list.append(Laboratory())
        lab_list[num].color = lab_color[num]

        mutation_room_list.append(MutationRoom())
        mutation_room_list[num].number = num + 1
        mutation_room_list[num].mutation = mutation_rooms[num]
        mutation_room_list[num].mutation_var = mutations_var[num]

    return ventilation_list, lab_list, mutation_room_list

def create_playing_field():  # создаём список всех 25 игровых тайлов
    playing_field_list = []
    create_amebas()
    create_units()
    playing_field_list.extend(ameba_list)
    playing_field_list.extend(ventilation_list)
    playing_field_list.extend(lab_list)
    playing_field_list.extend(mutation_room_list)
    shuffle(playing_field_list)
    return playing_field_list




