# Area Calc
import math

def paint_calc(wall_height, wall_width, coverage):
    number_of_cans = (wall_height * wall_width) / coverage
    round_cans = math.ceil(number_of_cans)
    print(f'You\'ll need {round_cans} cans of paint.')

paint_calc(7, 9, 2)

# Este codigo dice cuantas latas de pintura necesitaras para pintar una pared
# de un tamano especifico con una pintura de cobertura especifica. 