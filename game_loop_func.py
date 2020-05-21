
def create_players(Player, quantity_players): # функция создания игроков(сейчас не используется)
    players_list = []
    for quan in range(quantity_players): # количество игроков
        players_list.append(Player())
        players_list[quan].name = quan

def view(playing_field, units_name):    # функция печатает на экран игровые тайлы
    for i in range(len(playing_field)):
        if playing_field[i].name == units_name[0]:
            print(f'Амёба номер {playing_field[i].number}, цвет: {playing_field[i].color}, узор: {playing_field[i].pattern}, количество глаз: {playing_field[i].eyes}' )
        elif playing_field[i].name == units_name[1]:
            print('Вентиляция')
        elif playing_field[i].name == units_name[2]:
            print(playing_field[i].color)
        elif playing_field[i].name == units_name[3]:
            print(f'Комната мутации номер {playing_field[i].number}, мутация: {playing_field[i].mutation}')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


def search_initial_lab(playing_field, dice, units_name):  # ищем начальную лабораторию, которая выпала в кубиках
    index_lab = 0
    for lab in range(len(playing_field)):
        if playing_field[lab].name == units_name[2]:
            if playing_field[lab].color == dice[3][1]:
                index_lab = lab                        # сохраняем индекс начальной лаборатории в переменную
                break
    return index_lab

def direction_color(dice, index_lab, summ_tiles, direct_lab):  # вычисляем нарпавление движения по списку в зависимости от цвета стрелки
    begin_1, end_1, step_1, begin_2, end_2, step_2 = 0, 0, 0, 0, 0, 0

    if dice[3][0] == direct_lab[0]:  # если стрелка белая(по часовой), подгатавливем для range() направление вправо
        begin_1 = index_lab + 1
        end_1 = summ_tiles
        step_1 = 1
        begin_2 = 0
        end_2 = index_lab
        step_2 = 1
    elif dice[3][0] == direct_lab[1]:  # если стрелка черная(против часовой, подгатавливем для range() направление влево
        begin_1 = index_lab - 1
        end_1 = -1
        step_1 = -1
        begin_2 = summ_tiles - 1
        end_2 = index_lab
        step_2 = -1

    return [begin_1, end_1, step_1, begin_2, end_2, step_2]


def main_cycle(begin_1, end_1, step_1, begin_2, end_2, step_2, playing_field, dice, cube_color, \
               cube_pattern, cube_eyes, mutation_rooms, units_name, Ameba, Ventilation, MutationRoom): # функция ищет нужную амебу или комнату мутации
    for i in range(begin_1, end_1, step_1):  # обходим игровой список ПОСЛЕ начальной лаборатории
                                            # ----ИЩЕМ АМЕБУ ПОСЛЕ НАЧАЛЬНОЙ ЛАБОРАТОРИИ-----
        if Ameba.found_ameba is False and Ventilation.ventilation_transit is False \
                and playing_field[i].name == units_name[0]:  # если в списке попадается амеба, смотрим является ли она искомой
            #print(playing_field[i].number, playing_field[i].name, playing_field[i].color, playing_field[i].pattern, playing_field[i].eyes)
            if playing_field[i].pattern == dice[1] and playing_field[i].color == dice[0] \
                    and playing_field[i].eyes == dice[2]:
                if MutationRoom.last_lab is False:   # если еще небыло четвертой мутации
                    playing_field[i].ameba_found(playing_field[i].number)  # если найдена искомая амеба, сохраняем ее номер
                    #print(playing_field[i].number, playing_field[i].name, playing_field[i].color, playing_field[i].pattern, playing_field[i].eyes)
                                            # ----ИЩЕМ ВЕНТИЛЯЦИЮ ПОСЛЕ НАЧАЛЬНОЙ ЛАБОРАТОРИИ-----
        elif playing_field[i].name == units_name[1]:  # если попадается вентиляция
            Ventilation.transit_thr_vent()      # выставляем флаг входа в вентиляцию до следующей вентиляции
            #print(playing_field[i].name)
                                            # ----ИЩЕМ КОМНАТУ МУТАЦИИ ПОСЛЕ НАЧАЛЬНОЙ ЛАБОРАТОРИИ-----
        elif Ventilation.ventilation_transit is False and Ameba.found_ameba is False and playing_field[i].name == units_name[3]:  # если попадается комната мутации, смотрим какие мутации она делает
            playing_field[i].count_mutation(playing_field[i].number)  # плюсуем счетчик проходов через комнату мутации и передаем номер комнаты
            #print(playing_field[i].number, f'mutation count: {playing_field[i].count}')
            if playing_field[i].mutation == mutation_rooms[0]:
                #print(playing_field[i].number, playing_field[i].mutation)
                if dice[0] == cube_color[0]:
                    dice[0] = cube_color[1]
                else:
                    dice[0] = cube_color[0]
                #print(playing_field[i].mutation_var, f'Новые параметры поиска: {dice[0]}, {dice[1]}, {dice[2]}')
            elif playing_field[i].mutation == mutation_rooms[1]:
                #print(playing_field[i].mutation)
                if dice[1] == cube_pattern[0]:
                    dice[1] = cube_pattern[1]
                else:
                    dice[1] = cube_pattern[0]
                #print(playing_field[i].mutation_var, f'Новые параметры поиска: {dice[0]}, {dice[1]}, {dice[2]}')
            elif playing_field[i].mutation == mutation_rooms[2]:
                #print(playing_field[i].mutation)
                if dice[2] == cube_eyes[0]:
                    dice[2] = cube_eyes[1]
                else:
                    dice[2] = cube_eyes[0]
                #print(playing_field[i].mutation_var, f'Новые параметры поиска: {dice[0]}, {dice[1]}, {dice[2]}')
    for i in range(begin_2, end_2, step_2):  # обходим игровой список ДО начальной лаборатории
                                        # ----ИЩЕМ АМЕБУ ДО НАЧАЛЬНОЙ ЛАБОРАТОРИИ-----
        if Ameba.found_ameba is False and Ventilation.ventilation_transit is False  \
                and playing_field[i].name == units_name[0]:  # если в списке попадается амеба, смотрим является ли он а искомой
            #print(playing_field[i].number, playing_field[i].name, playing_field[i].color, playing_field[i].pattern, playing_field[i].eyes)
            if playing_field[i].pattern == dice[1] and playing_field[i].color == dice[0] \
                    and playing_field[i].eyes == dice[2]:
                if MutationRoom.last_lab is False:  # если еще небыло четвертой мутации
                    playing_field[i].ameba_found(playing_field[i].number)  # если найдена искомая амеба, сохраняем ее номер
                    #print(playing_field[i].number, playing_field[i].name, playing_field[i].color, playing_field[i].pattern, playing_field[i].eyes)
                                        # ----ИЩЕМ ВЕНТИЛЯЦИЮ ДО НАЧАЛЬНОЙ ЛАБОРАТОРИИ-----
        elif playing_field[i].name == units_name[1]:  # если попадается вентиляция
             Ventilation.transit_thr_vent()  # выставляем флаг входа в вентиляцию до следующей вентиляции
             #print(playing_field[i].name)
                                        # ----ИЩЕМ КОМНАТУ МУТАЦИИ ДО НАЧАЛЬНОЙ ЛАБОРАТОРИИ-----
        elif Ventilation.ventilation_transit is False and Ameba.found_ameba is False and playing_field[i].name == units_name[3]:  # если попадается комната мутации, смотрим какие мутации она делает
            playing_field[i].count_mutation(playing_field[i].number)  # плюсуем счетчик проходов через комнату мутации и передаем номер комнаты
            #print(playing_field[i].number, f'mutation count: {playing_field[i].count}')
            if playing_field[i].mutation == mutation_rooms[0]:
                #print(playing_field[i].number, playing_field[i].mutation)
                if dice[0] == cube_color[0]:
                    dice[0] = cube_color[1]
                else:
                    dice[0] = cube_color[0]
                #print(playing_field[i].mutation_var, f'Новые параметры поиска: {dice[0]}, {dice[1]}, {dice[2]}')
            elif playing_field[i].mutation == mutation_rooms[1]:
                #print(playing_field[i].mutation)
                if dice[1] == cube_pattern[0]:
                    dice[1] = cube_pattern[1]
                else:
                    dice[1] = cube_pattern[0]
                #print(playing_field[i].mutation_var, f'Новые параметры поиска: {dice[0]}, {dice[1]}, {dice[2]}')
            elif playing_field[i].mutation == mutation_rooms[2]:
                #print(playing_field[i].mutation)
                if dice[2] == cube_eyes[0]:
                    dice[2] = cube_eyes[1]
                else:
                    dice[2] = cube_eyes[0]
                #print(playing_field[i].mutation_var, f'Новые параметры поиска: {dice[0]}, {dice[1]}, {dice[2]}')

def reset_vars(Ameba, MutationRoom): # сбрасываем флаги найденных классов и номера найденных экземпляров
    Ameba.found_ameba, MutationRoom.last_lab = False, False
    Ameba.num_found_ameba, MutationRoom.num_last_mutroom = 0, 0
