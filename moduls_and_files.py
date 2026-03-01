import math
import os
from pprint import pprint

from calculator import scale_recipe
import calendar
from os import name, environ
import sys


# from string import ascii_lowercase, ascii_uppercase, punctuation

# recipe_calculator.py

# def get_recipe(dish_name):
#     recipes = {
#         "паста": {"макароны": 100, "соус": 50, "сыр": 30},
#         "салат": {"помидоры": 50, "огурцы": 50, "масло": 20},
#         "бутерброд": {"хлеб": 2, "сыр": 1, "ветчина": 1}
#     }
#     return recipes.get(dish_name.lower())
#
#
# def main():
#     dish = input("Введите название блюда (паста, салат, бутерброд): ")
#     recipe = get_recipe(dish)
#
#     if recipe is None:
#         print("Такого рецепта нет.")
#         return
#
#     portions = int(input("Сколько порций вы хотите? "))
#     scaled = scale_recipe(recipe, portions)
#
#     print(f"\nИнгредиенты на {portions} порций:")
#     for ingredient, amount in scaled.items():
#         print(f"- {ingredient}: {amount} г")
#
# main()



# c = calendar.TextCalendar(calendar.MONDAY)
# print(c.formatyear(2026))

# print(dir(calendar))

# print(dir(name))


# print(sys.getrecursionlimit())


# print(ascii_lowercase, ascii_uppercase, punctuation, sep='\n')




# def main(n):
#     n = str(n)[::-1]
#     yield n
#
# user = -3242342
# print(*list(main(user)))



