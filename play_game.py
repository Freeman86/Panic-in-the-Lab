
from create_game_func import create_playing_field
from game_loop_func import search_initial_lab, direction_color, main_cycle, view, reset_vars
from variables import *
from classes import *

pl = Player()  # создаем игрока
playing_field = create_playing_field()  # создаем, перемешиваем и сохраняем список всех игровых объектов

#view(playing_field, units_name) # печатаем на экран все игровые тайлы (сделал печать тайлов после каждого броска кубиков)

while Player.player_win is False: # пока игрок не набрал пять жетонов

    # if input('Чтобы бросить кубики, нажмите 1 ') == str(1):
    view(playing_field, units_name)  # печатаем на экран все игровые тайлы
    dice = pl.roll_the_dice(cube_pattern, cube_color, cube_eyes, color_lab, direct_lab)  # бросаем кости и сохраняем результат в переменную
    print(f'Кубик цвета: {dice[0]}', '\n', f'Кубик узора: {dice[1]}', '\n', f'Кубик глаз: {dice[2]}',\
          '\n', f'Кубик стрелки: {dice[3][0]} и цвета лаборатории: {dice[3][1]}')

    index_lab = search_initial_lab(playing_field, dice, units_name)     # ищем начальную лабораторию

    range_direction = direction_color(dice, index_lab, summ_tiles, direct_lab)      # вычисляем направление движения от начальной лаборатории

    while Ameba.found_ameba is False and MutationRoom.last_lab is False:      # ищем нужную амебу или четвертую комнату мутации
        main_cycle(*range_direction, playing_field, dice, cube_color, cube_pattern, cube_eyes, mutation_rooms,\
                units_name, Ameba, Ventilation, MutationRoom)


    if MutationRoom.num_last_mutroom > 0 and Ameba.num_found_ameba == 0:                            # подсказка
        print(f'Подсказка: комната мутации номер {MutationRoom.num_last_mutroom}', '\n', hint)
    elif Ameba.num_found_ameba > 0:
        print(f'Подсказка: амёба номер {Ameba.num_found_ameba}', '\n', hint)

    num_found = int(input('Введите номер найденной амебы или последней лаборатории: '))  # ожидаем пока найдет игрок
    if num_found == Ameba.num_found_ameba:
        Tokens.Add(pl)
        print('Вы правильно нашли нужный обект!', f' Ваше количество жетонов: {pl.token}', '\n', separator)
    elif num_found == MutationRoom.num_last_mutroom:
        Tokens.Add(pl)
        print('Вы правильно нашли нужный обект!',  f' Ваше количество жетонов: {pl.token}', '\n', separator)
    else:
        Tokens.Sub(pl)
        print('Попробуйте еще раз!', f' Ваше количество жетонов: {pl.token}', '\n', separator)

    reset_vars(Ameba, MutationRoom) # обнуляем переменные в классе амебы и комнаты мутации


if Player.player_win == True:   # если игрок набрал пять жетонов
    print('Вы выиграли!')