
from random import randint, random

def roll_dice(cube_pattern, cube_color, cube_eyes, color_lab, direct_lab):    # бросаем четыре кубика и получаем рандомный результат
    lab_cube = []
    rand = randint(0, 100)
    if rand % 2 != 0:
        pattern_cube = cube_pattern[0]
        eyes_cube = cube_eyes[1]
    else:
        pattern_cube = cube_pattern[1]
        eyes_cube = cube_eyes[0]
    rand = randint(0, 100)
    if rand % 2 == 0:
        color_cube = cube_color[0]
        lab_cube.append(direct_lab[1])
    else:
        color_cube = cube_color[1]
        lab_cube.append(direct_lab[0])
    rand = random()
    if rand <= 0.3333:
        lab_cube.append(color_lab[0])
    elif rand >= 0.3333 or rand <= 0.6666:
        lab_cube.append(color_lab[1])
    else:
        lab_cube.append(color_lab[2])
    return [color_cube, pattern_cube, eyes_cube, lab_cube]

class Player():    # игрок
    def __init__(self):
        self.name = 'player'
        self.number = None
        self.token = 0
        #self.win = False

    player_win = False

    def token_add(self):  # добавляет жетон игроку
        self.token += 1
        if self.token == 5:     # игрок победил, если набрал 5 жетонов
            #self.win = True
            self.__class__.player_win = True

    def token_sub(self):   # вычитает жетон у игрока
        if self.token > 0:
            self.token -= 1

    @staticmethod
    def roll_the_dice(cube_pattern, cube_color, cube_eyes, color_lab, direct_lab):   # игрок бросает кости. Функция roll_dice() находится выше
        return roll_dice(cube_pattern, cube_color, cube_eyes, color_lab, direct_lab)

class Ameba():   # амеба
    def __init__(self):
        self.name = 'ameba'
        self.number = None
        self.color = None
        self.pattern = None
        self.eyes = None

    found_ameba = False     # если амеба найдена - False
    num_found_ameba = 0     # сохраняем номер найденной амебы(начинаются с единицы)

    @classmethod
    def ameba_found(cls, number):  # регистрируем что амеба найдена и сохраняем ее номер
        cls.found_ameba = True
        cls.num_found_ameba = number

class Ventilation():  # вентиляция
    def __init__(self):
        self.name = 'ventilation'

    ventilation_transit = False     # если True - амеба прошла через вентиляцию и пропускаем все тайлы до следующей вентиляции

    @classmethod
    def transit_thr_vent(cls):  # если амеба вошла в вентиляцию ставим - True, если вышла - False
        if cls.ventilation_transit is False:
            cls.ventilation_transit = True
        else:
            cls.ventilation_transit = False


class Laboratory():   # лаборатория
    def __init__(self):
        self.name = 'laboratory'
        self.color = None


class MutationRoom():  # комната мутации
    def __init__(self):
        self.name = 'mutation'
        self.number = None
        self.mutation = None
        self.mutation_var = None

    last_lab = False  # после четвертой мутации будет True
    count = 0  # переменная, куда сохраняется количество проходов через комнаты мутаций
    num_last_mutroom = 0  # нормер последней комнаты мутации

    def mutation_revers(self, ameba_name):  # смена цвета, узора или количества глаз
        if self.mutation == "color":
             if ameba_name.color == self.mutation_var[0]:
                 ameba_name.color = self.mutation_var[1]
             else:
                 ameba_name.color = self.mutation_var[0]
        elif self.mutation == "pattern":
            if ameba_name.pattern == self.mutation_var[0]:
                ameba_name.pattern = self.mutation_var[1]
            else:
                ameba_name.pattern = self.mutation_var[0]
        else:
            if ameba_name.eyes == self.mutation_var[0]:
                ameba_name.eyes = self.mutation_var[1]
            else:
                ameba_name.eyes = self.mutation_var[0]
    @classmethod
    def count_mutation(cls, number):     # метод запускает счетчик прохода через комнату мутации
        cls.count += 1
        if cls.count == 4:      # если произошел четвертый проход через комнату мутации, сохраняем событие и номер последней комнаты
            cls.last_lab = True
            cls.num_last_mutroom = number

class Tokens():             # 30 жетонов
    tokens = 30
    @classmethod
    def Add(cls, player_name):  # добавляет игроку жетон, вычитает из банка
        if cls.tokens > 0:
            cls.tokens -= 1
            player_name.token_add()
    @classmethod
    def Sub(cls, player_name):  # вычитает жетон у игрока, добавляет в банк
        if cls.tokens < 30:
            cls.tokens += 1
            player_name.token_sub()