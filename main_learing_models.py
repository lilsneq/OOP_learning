#импорты
# from typing import List, Tuple
from itertools import count


#начало учебного проекта по ООП



#2.1 Классы, объекты, экземпляры классов

# class Car:
#     model = "BMW"
#     engine = 1.6
#
#
# a = Car()
# b = Car()
#
# print(a, b)
# print(type(a))
# print(type(b))
#
# print('Это объект принадлежит классу Car?', isinstance(a, Car))
# print('Это объект принадлежит классу Car?', isinstance(b, Car))
# print('Это объект принадлежит классу Car?', isinstance('hello', Car))
# print('Это объект принадлежит классу Car?', isinstance(1.6, Car))
#
# a.model = "VAZ"
# b.color = "Black"
# print(a.model, b.color)
# print(Car.engine)

                                                    #

# class Contact:
#     name = 'Barak'
#     phone_number = '+1 202 345 4564'
#
#
# b = Contact()

                                                    #

# class TaskManager:
#     pass
#
#
# todos = [TaskManager() for i in range(20)]
# print(todos)

                                                    #2.2 Атрибуты класса
                                                    #метод getattr ссылает на атрибус и создаёт атрибус если нет третим параметром
# class Person:
#     name = 'Ivan'
#     age = 30
#
#
# Person.name = 'Sergey'
# Person.x =[3,3,3,3,3]
#
# print(getattr(Person, 'x', 100))
# print(getattr(Person, 'name', 100))
# print(getattr(Person, 'OOP', 100))

                                                    #метод setattr

# class Person:
#     name = 'Ivan'
#     age = 30
#
#
#
# a, b = Person(), Person()
# print(Person.name, a.name, b.name)
# a.name = 'Jago'
# Person.name = 'Aladdin'
# print(Person.name, a.name, b.name)
#
# setattr(Person, 'new_name', 'Pasha')                #всегда возвращает None и меняет атрибуты иои создаёт
# print(getattr(Person, 'new_name'))
#
# del Person.name
# #print(getattr(Person, 'name'))                     #атрибут удалился при помощи del
#
# delattr(Person, 'new_name')                                         #удаление атрибута из класса, если атрибута нет вызывается ошибка
# print(getattr(Person, 'new_name', "такого атрибута нет"))

                                                    #
# class Robot:
#     material = 'steel'
#
# print('can_speak' in Robot.__dict__)
# print('material' in Robot.__dict__)

                                                    #
#
# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#
#
# print(getattr(Book, 'writer'), getattr(Book, 'name'), sep='\n')

                                                    #

# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#
#
# print(*[getattr(Book, i) for i in ('writer', 'pages')], sep='\n')

                                                    #

# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#
#
# # a = [setattr(Book, i, lambda i=i: 155 if i == 'pages' else "Скотный двор") for i in ("name", "pages")]
# a = (setattr(Book, "name", "Скотный двор"), setattr(Book, "pages", 155))
#
# print(type(Book.name))
# for i in Book.__dict__.values():
#     print(i)

                                                    #
#
# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#
# # a = (setattr(Book, 'genre', 'dystopian'), setattr(Book, 'rating', 8.7))
# Book.rating = 8.7
# setattr(Book, 'genre', 'dystopian')
#
# for i in Book.__dict__.items():
#     print(i)

                                                    #

# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#     rating = 8.7
#     genre = 'dystopian'
#
#
# del (Book.pages, Book.rating)
# delattr(Book, 'writer')
#
# for i in Book.__dict__.items():
#     print(i)

                                                    #

# class Empty:
#     pass
#
#
# my_list = [
#     ('apple', 23),
#     ('banana', 80),
#     ('cherry', 13),
#     ('date', 10),
#     ('elderberry', 4),
#     ('fig', 65),
#     ('grape', 5),
#     ('honeydew', 7),
#     ('kiwi', 1),
#     ('lemon', 10),
# ]

# for i in my_list:
#     setattr(Empty, i[0], i[1])

# for item, value in my_list:
#     setattr(Empty, item, value)


# for i in Empty.__dict__.items():
#     print(i)


                                                    #

# def is_obj_has_attr(item, value):
#     return hasattr(item, value)
#
#
# class Duck:
#     weight = 5
#     height = 10
#
#
# print(is_obj_has_attr(Duck, 'weight'))
# print(is_obj_has_attr(Duck, 'name'))
# print(is_obj_has_attr(Duck, 'height'))
#
# print()
#
# class House:
#     color = 'white'
#     rooms = 4
#
# print(is_obj_has_attr(House, 'color'))
# print(is_obj_has_attr(House, 'rooms'))
# print(is_obj_has_attr(House, 'room'))

                                                    #

# class Person:
#     name = "John Smith"
#     age = 30
#     gender = "male"
#     address = "123 Main St"
#     phone_number = "555-555-5555"
#     email = "johnsmith@example.com"
#     is_employed = True
#
#
# user = input().split()
# for i in user:
#     if i.lower() in Person.__dict__.keys():
#         print(f"{i}-YES")
#     else:
#         print(f"{i}-NO")

                                                    #

# class Car:
#     model = "BMW"
#     engine = 1.6
#
#
#
# a1 = Car()
# a1.model = "Lada", "2.0"
# Car.model_japan = "mazda"
# print(Car.__dict__)
# print(a1.__dict__)
#
# del a1.model
# print(a1.model)

                                                    #

# class SuperHero:
#     pass
#
#
# batman = SuperHero()
# batman.can_fly = False
# batman.damage = 175
#
#
# superman = SuperHero()
# superman.can_fly = True
# superman.damage = 285
# superman.alter_ego = "Кларк Кент"
#
#
#
# print(superman.__dict__)
# print(batman.__dict__)


                                                    #

# class Config:
#     pass
#
# def create_instance(n: int) -> Config:
#     obj = Config()
#     for i in range(n):
#         setattr(obj , f'attribute{i+1}', f'value{i+1}')
#     return obj
#
#
# config_4 = create_instance(4)
# config_3 = create_instance(3)
# config_2 = create_instance(2)
# print(config_4.__dict__)
# print(config_3.__dict__)
# print(config_2.__dict__)

                                                    #

# class Car:
#     model = 'BMW'
#     engine = 1.6
#
#     @staticmethod
#     def drive():
#         print("drive")
#
#     @staticmethod
#     def wheel():
#         return 'wheel'
#
#
# Car.drive()
#
# b = Car()
# b.drive()
# b.wheel()
# print(f'b.wheel - {b.wheel()}')


                                                    #3.1 Методы экземпляра. Параметр self

# class Cat:
#     breed = 'pers'
#     def hello(*args):
#         print("Hello, world from Cat!", *args)
#\
#     def show_bread(self):
#         print(f'my breed is {self.breed}')
#
#     def show_name(self):
#         if hasattr(self, 'name'):
#             print(f'my name is {self.name}')
#         else:
#             print(f'nothing')
#
#     def set_value(self, value, age=0):
#         self.name = value
#         self.age = age
#
#     def show_age(self):
#         print(f'{self.name} is {self.age} years old')
#
# # Cat().hello()
# bob = Cat()
# jim = Cat()
#
# bob.hello()
# jim.hello()
#
# walt = Cat()
#
#
# bob.show_bread()
# bob.set_value('BOB', age=40)
# bob.show_age()
#
# mary = Cat()
# mary.name = 'MARY'
# mary.show_name()
#
# tom = Cat()
# tom.set_value('TOM')
# tom.show_name()
#
# jerry = Cat()
# jerry.set_value('JERRY', age=12)
# jerry.show_name()
# jerry.show_age()


# class Student:
#     def set_data(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)
#
# student_1 = Student()
# student_2 = Student()
#
# student_1.set_data("Kelly", 15)
# student_2.set_data("Rita", 19)
#
# student_1.show()
# Student.show(student_2)

                                                    #

# class Lion:
#     def roar(self):
#         print("Rrrrrrr!!!")
#
#
# s = Lion()
# s.roar()

                                                    #

# class Robot():
#     def say_hello(self):
#         print('Hello, human! My name is C-3PO')
#
#     def say_bye(self):
#         print('See u later alligator')
#
#
# c3po = Robot()
# r2d2 = Robot()
#
# c3po.say_hello()
# c3po.say_bye()
#
# r2d2.say_hello()
# r2d2.say_bye()

                                                    #

# class Robot:
#     def set_name(self, name):
#         self.name = name
#
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f'Hello, human! My name is {self.name}')
#         else:
#             print(f'У робота нет имени')
#
#     def say_bye(self):
#         print(f'See u later alligator')
#
#
# c3po = Robot()
# c3po.say_hello()
# c3po.set_name('R2D2')
# c3po.say_hello()
# c3po.say_bye()


# class Name:
#     def set_name(self, name):
#         self.name = name
#
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f'Hello {self.name}')
#         else:
#             print(f'Такого имени нет')
#
#     def say_goodbye(self):
#         print(f'Goodbye {self.name}')
#
#
# Sergey = Name()
# Sergey.set_name('Sergey')
# Sergey.say_hello()
# Sergey.say_goodbye()

                                                    #

# class Counter:
#     def start_from(self, counter=0):
#         self.counter = counter
#
#     def increment(self):
#         self.counter += 1
#
#     def display(self):
#         print(f'Текущее значение счетчика = {self.counter}')
#
#     def reset(self):
#         self.counter = 0
#
#
# c1 = Counter()
# c2 = Counter()
# c1.start_from(10)
# c2.start_from(20)
# c1.increment()
# c2.increment()
# c1.display()
# c2.display()
# c1.reset()
# c1.display()
# c2.display()

                                                    #

# class Constructor:
#     def add_atribute(self, key, value):
#         setattr(self, key, value)
#
#     def display(self):
#         return print(self.__dict__)
#
#
# obj2 = Constructor()
# obj3 = Constructor()
#
# obj2.display()
# obj3.display()
#
# obj2.add_atribute('height', 100)
#
# obj3.add_atribute('a', 100)
# obj3.add_atribute('b', 300)
# obj3.add_atribute('c', 200)
# obj3.add_atribute('b', 1)
#
# obj2.display()
# obj3.display()

                                                    #

# class Point:
#     def set_coordinates(self, x , y):
#         self.x = x
#         self.y = y
#
#     def get_distance_to_origin(self):
#         if hasattr(self, 'y') and hasattr(self, 'x'):
#             return (self.x**2 + self.y**2) ** 0.5
#
#     def display(self):
#         if hasattr(self, 'y') and hasattr(self, 'x'):
#             print(f"Point({self.x}, {self.y})")
#         else:
#             print('Координаты не заданы')
#
#
# p3 = Point()
# p3.display()
# print(p3.get_distance_to_origin())
# p3.x = 4
# p3.display()
# print(p3.get_distance_to_origin())
# p3.y = 3
# p3.display()
# print(p3.get_distance_to_origin())

                                                    #

# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance_to_origin(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             return (self.x ** 2 + self.y ** 2) ** 0.5
#         return None
#
#     def display(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             print(f"Point({self.x}, {self.y})")
#         else:
#             print('Координаты не заданы')
#
#     def get_distance(self, other):
#         if not isinstance(other, Point):
#             print("Передана не точка")
#             return None
#         if hasattr(self, 'x') and hasattr(self, 'y') and hasattr(other, 'x') and hasattr(other, 'y'):
#             return (((self.x - other.x)**2) + ((self.y - other.y) ** 2)) ** 0.5
#
#         else:
#             print('Координаты не заданы')
#
#
#
# p1 = Point()
# p2 = Point()
# print(p1.get_distance(p2))
# p1.set_coordinates(1, 2)
# print(p1.get_distance(p2))
# p2.set_coordinates(4, 6)
# print(p1.get_distance(p2))


                                                    #3.2 Инициализация экземпляра. Метод __init__

# class Cat:
#     def __init__(self, name=None, breed='pers', age=1, color='white'):
#         print(f'hello new object: ссылка на новый объект -> {self}, -> параметры {name}, {breed, age, color}')
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.color = color
#
#
#
# Cat('Tom', 'siam', 12, 'black')
# Cat('Walt')
# Kally = Cat('Kally', age=10)
                                                    #

# class Name:
#     def __init__(self, name):
#         print(f'{name}')
#         self.name = name
#         self.breed = 'pers'
#         self.age = 1
#         self.color = 'white'
#
# Name('lol', "d")            #упадёт ошибка так как нет такого параметра

                                                    #

# class Calculate:
#     def __init__(self, w, l):
#         self.w = w
#         self.l = l
#         self.per = (self.w * self.l) * 2
#
#
# rect = Calculate(10, 10)
# print(rect.per)

                                                    #

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# bmw = Vehicle(240, 18)
# audi = Vehicle(123, 43)
# print(bmw.__dict__)
# print(audi.__dict__)
# model_x = Vehicle(200, 18000)
# print(model_x.max_speed)
# print(model_x.mileage)

                                                    #

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name}, and I am {self.age} years old"
#
#
# # Ниже расположен код для проверок, его не нужно удалять
# bro = Person('Nikolay', 34)
# assert bro.age == 34
# assert bro.name == 'Nikolay'
# assert bro.greet() == 'Hello, my name is Nikolay, and I am 34 years old'
#
# sister = Person('Elena', 21)
# assert sister.age == 21
# assert sister.name == 'Elena'
# assert sister.greet() == 'Hello, my name is Elena, and I am 21 years old'
# print('Good')

                                                    #

# class Laptop:
#     def __init__(self, brand=None, model=None, price=None):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{self.brand} {self.model}'
#
#     def laptop1(self, price, a, d):
#         pass
#
#     def laptop2(self, price, a, d):
#         pass
#
#
# laptop1 = Laptop()
# laptop2 = Laptop()
#
#
# assert isinstance(laptop1, Laptop)
# assert isinstance(laptop2, Laptop)
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# assert hp.laptop_name == 'hp 15-bw0xx'
# assert hp.price == 57000
# assert isinstance(hp, Laptop)
#
#
# lenovo = Laptop('lenovo', 'z-570-dx', 61000)
# assert lenovo.brand == 'lenovo'
# assert lenovo.model == 'z-570-dx'
# assert lenovo.price == 61000
# assert lenovo.laptop_name == 'lenovo z-570-dx'
# assert isinstance(lenovo, Laptop)
# print('Good')

                                                    #

# class Article:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
##         return None                                       #НЕЛЬЗЯ ВОЗВРАЩАТЬ В МЕТОДЕ __init__ что-то кроме None он сам возвращает None
#
# article = Article('Как надуть грелку', "Пяточок")
# print(article.__dict__)

                                                    #

# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, count_goals=1):
#         self.goals = self.goals + count_goals
#
#     def make_assist(self, count_assists=1):
#         self.assists = self.assists + count_assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# assert isinstance(leo, SoccerPlayer)
# assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
# leo.score(700)
# assert leo.goals == 700
# leo.make_assist(500)
# assert leo.assists == 500
#
# leo.statistics()
#
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# assert isinstance(kokorin, SoccerPlayer)
# assert kokorin.name == 'Alex'
# assert kokorin.surname == 'Kokorin'
# assert kokorin.assists == 0
# assert kokorin.goals == 0
# kokorin.score()
# assert kokorin.goals == 1
# kokorin.score(5)
# assert kokorin.goals == 6
# kokorin.make_assist()
# assert kokorin.assists == 1
# kokorin.make_assist(10)
# assert kokorin.assists == 11
#
# kokorin.statistics()
#
#
# obi = SoccerPlayer('Оби-Ван', 'Кеноби')
# obi.make_assist()
# assert obi.name == 'Оби-Ван'
# assert obi.surname == 'Кеноби'
# assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
# obi.statistics()
#
# mila = SoccerPlayer('Mila', 'Kunis')
# mila.make_assist()
# mila.statistics()

                                                    #

# class Zebra:
#     count = 0
#     def which_stripe(self):
#         if self.count == 0:
#             self.count += 1
#             print('Полоска белая')
#         else:
#             self.count -= 1
#             print('Полоска черная')
#
#     def run_away(self):
#         print('Oh, Sugar Honey Ice Tea')
#
#
# zebra = Zebra()
# zebra.run_away()
# zebra.which_stripe()
# zebra.which_stripe()
# zebra.which_stripe()
# zebra.which_stripe()
# zebra.which_stripe()
# zebra.run_away()

                                                    #

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f"{self.last_name} {self.first_name}"
#
#     def is_adult(self):
#         return self.age >= 18
#
#
# p1 = Person('Ash', 'Ketchum', 20)
# assert isinstance(p1, Person)
# assert p1.full_name() == 'Ketchum Ash'
# assert p1.age == 20
# assert p1.first_name == 'Ash'
# assert p1.last_name == 'Ketchum'
# assert p1.is_adult() is True
#
# p2 = Person('Hermione', 'Granger', 16)
# assert isinstance(p2, Person)
# assert p2.age == 16
# assert p2.first_name == 'Hermione'
# assert p2.last_name == 'Granger'
# assert p2.full_name() == 'Granger Hermione'
# assert p2.is_adult() is False
# print('Good')


                                                    #3.3 Практика "Создание класса и его методов"

# class Point:
#
#     list_points = []
#
#     def __init__(self, coord_x=0, coord_y=0):
#         self.move_to(coord_x, coord_y)
#         Point.list_points.append(self)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def star_coord(self):
#         self.move_to(0,0 )
#
#     def get_coord(self):
#         print(f'X = {self.x}, Y = {self.y}')
#
#     def calc_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             raise ValueError(f"Аргумент должен принадлежать классу {Point}")
#
#         print(((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5)
#
#
# p1 = Point(3, 4)
# p1.star_coord()
# p1.get_coord()
#
# p2 = Point(-54, 32)
# p2.get_coord()
#
# p3 = Point(54, -32)
# p3.move_to(4,5)
# p3.get_coord()
#
# p4 = Point(4)
# p4.move_to(2323,32)
# p4.get_coord()
#
# p5 = Point(6,0)
# p6 = Point(0,8)
# p5.calc_distance(p6)
# Point.calc_distance(p5,p6)
#
#
# p10 = Point()
# p11 = Point(4,5)
#
# #можно смотреть списки в классе чрез сам класс Point.список
# print(f'Point[0].y = {Point.list_points[0].y}')
# print(f'Point[2].x = {Point.list_points[2].x}')
# print(f'Point[4].x = {Point.list_points[4].x}')

                                                    #

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
#
# curt = Dog("Curt", 4)
# assert isinstance(curt, Dog)
# assert curt.name == 'Curt'
# assert curt.age == 4
# assert curt.description() == 'Curt is 4 years old'
# assert curt.speak("Wo") == 'Curt says Wo'
# assert curt.speak("Bow") == 'Curt says Bow'
#
# jack = Dog("Jack", 12)
# assert isinstance(curt, Dog)
# assert jack.name == 'Jack'
# assert jack.age == 12
# assert jack.description() == 'Jack is 12 years old'
# assert jack.speak("Woof Woof") == 'Jack says Woof Woof'
# assert jack.speak("Bow Wow") == 'Jack says Bow Wow'
#
# assert Dog('Karl', 6).description() == 'Karl is 6 years old'
# print('Good')

                                                    #

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# r1 = Rectangle(2, 3)
# assert r1.width == 2
# assert r1.height == 3
# assert r1.perimeter() == 10
# assert r1.area() == 6
#
# r2 = Rectangle(10, 0.5)
# assert r2.width == 10
# assert r2.height == 0.5
# assert r2.perimeter() == 21.0
# assert r2.area() == 5.0
# print('Good')

                                                    #

# class Numbers:
#     def __init__(self, *args):
#         self.numbers = list(args)
#
#     def add_number(self, number):
#         self.numbers.append(number)
#
#     def get_positive(self):
#         result = []
#         for i in self.numbers:
#             if i > 0:
#                 result.append(i)
#         return result
#
#     def get_negative(self):
#         result = []
#         for i in self.numbers:
#             if i < 0:
#                 result.append(i)
#         return result
#
#     def get_zeroes(self):
#         result = []
#         for i in self.numbers:
#             if i == 0:
#                 result.append(i)
#         return result
#
#
# nums = Numbers(10, 20, 30, 0, 0, 5)
#
# print(nums.get_positive())
# print(nums.get_zeroes())
# nums.add_number(100)
# nums.add_number(0)
# nums.add_number(7)
# print(nums.get_positive())
# print(nums.get_zeroes())

                                                    #

# class Stack:
#     def __init__(self):
#         self.values = list()
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if len(self.values) > 0:
#             return self.values.pop(-1)
#         print('Empty Stack')
#         return None
#
#     def peek(self):
#         if self.values:
#             return self.values[-1]
#         print('Empty Stack')
#         return None
#
#     def is_empty(self):
#         return len(self.values) == 0
#
#     def size(self):
#         return len(self.values)
#
#
# # Ниже код для проверки класса Stack
#
# s = Stack()
# assert s.values == []
# assert isinstance(s, Stack)
#
# s.peek()  # распечатает 'Empty Stack'
# assert s.is_empty() is True
# s.push('cat')
# assert s.size() == 1
# assert s.peek() == 'cat'
#
# s.push('dog')
# assert s.size() == 2
# assert s.peek() == 'dog'
#
# s.push(True)
# assert s.size() == 3
# assert s.is_empty() is False
#
# s.push(777)
# assert s.size() == 4
#
# assert s.pop() == 777
# assert s.size() == 3
#
# assert s.pop() is True
# assert s.size() == 2
#
# s.push(123)
# s.push(123456)
# assert s.peek() == 123456
# assert s.size() == 4
#
# assert s.pop() == 123456
# assert s.pop() == 123
# assert s.pop() == 'dog'
# assert s.is_empty() is False
# assert s.pop() == 'cat'
# assert s.is_empty() is True
#
#
# d = Stack()
# assert d.peek() is None  # Печатает "Empty Stack"
# assert d.pop() is None  # Печатает "Empty Stack"
# d.push('hello')
# assert d.size() == 1
# d.push('world')
# assert d.size() == 2
# assert d.peek() == 'world'
# assert d.pop() == 'world'
# assert d.peek() == 'hello'

                                                    #

# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         return f'Worker {self.name}; passport-{self.passport}'
#
#
# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# worker_objects = []
#
# for i in persons:
#     w = Worker(i[0], i[1], i[2], i[3])
#     worker_objects.append(w)
#     w.get_info()
#
# for worker in worker_objects:
#     print(worker.get_info())
#
#
# worker_objects = [Worker(*i) for i in persons]
#
# for worker in worker_objects:
#     print(worker.get_info())
#
#
# worker_objects = []
#
# for i in persons:
#     worker_objects.append(Worker(i[0], i[1], i[2], i[3]))
#     if len(worker_objects)  == len(persons):
#         for j in worker_objects:
#             print(j.get_info())

                                                    #

# Напишите определение класса CustomLabel
# class CustomLabel:
#     def __init__(self, text, **kwargs):
#         self.text = text
#         self.config(**kwargs)
#
#     def config(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#
#
#
#
# # Ниже код для проверки методов класса CustomLabel
# label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
# label2 = CustomLabel(text="Username")
# label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
# label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)
#
# assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
# assert label2.__dict__ == {'text': 'Username'}
# assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
# assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}
#
# print(label1.__dict__)
# print(label2.__dict__)
# print(label3.__dict__)
# print(label4.__dict__)
# print(label5.__dict__)
#
# label4.config(color='red', bd=100)
# label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)
#
# assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
#                            'color': 'red', 'bd': 100, 'z': 432}

                                                        #

#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee:
#     def __init__(self, name, age, company_name, location):
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)
#
#
# ivan = Person('Ivan', 32)
# assert ivan.name == 'Ivan'
# assert ivan.age == 32
# ivan.display_person_info()
#
# zara = Company('Zara', 'Prague')
# assert zara.company_name == 'Zara'
# assert zara.location == 'Prague'
# zara.display_company_info()
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# assert isinstance(emp.personal_data, Person)
# assert isinstance(emp.work, Company)
#
# assert emp.personal_data.name == 'Jessica'
# assert emp.personal_data.age == 28
# emp.personal_data.display_person_info()
#
# assert emp.work.company_name == 'Google'
# assert emp.work.location == 'Atlanta'
# emp.work.display_company_info()
#
# emp2 = Employee('Kolya', 11, 'Facebook', 'Seattle')
# assert isinstance(emp2.personal_data, Person)
# assert isinstance(emp2.work, Company)
#
# assert emp2.personal_data.name == 'Kolya'
# assert emp2.personal_data.age == 11
# emp2.personal_data.display_person_info()
#
# assert emp2.work.company_name == 'Facebook'
# assert emp2.work.location == 'Seattle'
# emp2.work.display_company_info()

                                                    #

# class Task:
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         return print(f'{self.name} ({("Сделана" if self.status else "Не сделана")})')
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         self.tasks.remove(task)
#
#
# class TaskManager:
#     def __init__(self, tasklist):
#         self.task_list = tasklist
#
#     def mark_done(self, status_instance):
#         status_instance.status = True
#
#     def mark_undone(self, status_instance):
#         status_instance.status = False
#
#     def show_tasks(self):
#         for task in self.task_list.tasks:
#             Task.display(task)
#
#



                                                    #

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_exists(self):
#         return (self.a + self.b > self.c and
#                 self.a + self.c > self.b and
#                 self.b + self.a > self.a)
#
#     def is_equilateral(self):
#         return self.a == self.b == self.c
#
#     def is_isosceles(self):
#         if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
#             return self.a == self.b or self.b == self.c or self.c == self.a
#         return False

# triangle = Triangle(3, 4, 5)
# print(f"Is Triangle exist: {triangle.is_exists()}")
# print(f"Is Equilateral: {triangle.is_equilateral()}")
# print(f"Is Isosceles: {triangle.is_isosceles()}")

                                                    #

# class Point:
#     dictory = list()
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.dictory.append(self)
#
#     def get_distance_to_origin(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def get_point_with_max_distance(self):
#         # lists = sorted(Point.dictory.keys() ,key=lambda p: p.get_distance_to_origin())                    #вывод наибольшего из всех
#         # lists[-1].display()
#
#         result = max(Point.dictory, key=lambda x: (x.get_distance_to_origin(), x.y))
#
#         result.display()
#
#
#
#     def get_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             print('Передана не точка')
#             return None
#         return ((self.x - another_point.x) ** 2
#                 + (self.y - another_point.y) ** 2) ** 0.5
#
#     def display(self):
#         print(f"Point({self.x}, {self.y})")


# p1 = Point(6, 8)
# p2 = Point(8, 6)
# p2.get_point_with_max_distance()

# Point.get_point_with_max_distance(p1)

                                                    #3.4 Моносостояние для экземпляров класса

# class Cat:
#     __shared_attr = {
#         'breed': 'pers',
#         'color': 'black'
#     }
#
#     def __init__(self):
#         self.__dict__ = Cat.__shared_attr
#
#
# a = Cat()
# g = Cat()
#
#
# g.breed = 'SIAM'
# g.name = 'FRANKLIN'
#
#
# print(a.__dict__)
# print(g.__dict__)

                                                    #

# class MyClass:
#     __my_attrs = {}
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.__dict__ = MyClass._my_attrs
#
#
# m = MyClass(10, True)
# r = MyClass(50, False)
# print(MyClass.__dict__)
# print(r.__dict__)

                                                    #

#  напишите определение класса WeatherStation
# class WeatherStation:
#     __weather_sensor = {
#         'temperature': 0,
#         'humidity': 0,
#         'pressure': 0
#         }
#
#     def __init__(self):
#         self.__dict__ = WeatherStation.__weather_sensor
#
#     def update_data(self, temperature, humidity, pressure):
#         self.temperature = temperature
#         self.humidity = humidity
#         self.pressure = pressure
#
#     def get_current_data(self):
#         return tuple(WeatherStation.__weather_sensor.values())
#
#
# # код для проверки
# sensor1 = WeatherStation()
# assert sensor1.temperature == 0
# assert sensor1.humidity == 0
# assert sensor1.pressure == 0
# sensor2 = WeatherStation()
# assert sensor2.get_current_data() == (0, 0, 0)
# sensor1.update_data(25, 60, 103)
# assert sensor1.get_current_data() == (25, 60, 103)
# assert sensor2.get_current_data() == (25, 60, 103)
# sensor3 = WeatherStation()
# assert sensor3.get_current_data() == (25, 60, 103)
# sensor3.update_data(50, 20, 10)
# assert sensor1.get_current_data() == (50, 20, 10)
# assert sensor2.get_current_data() == (50, 20, 10)
# print('Good')

                                                    #

# class Settings:
#     _shared_state = {}
#
#     def __init__(self, **kwargs):
#         self.__dict__ = self._shared_state
#         self.__dict__.update(kwargs)
#
#
# s1 = Settings(ver=1)
# s2 = Settings()
#
# s1.__dict__ = {'status': 'broken'}
#
# print(s2.__dict__)
# print(s1.__dict__)
                                                    #3.5 Публичные, приватные, защищенные атрибуты и методы

# class Phone:
#     def __init__(self):
#         self._serial_number = "123-ABC"
#
#
# s1 = Phone()
# print(s1._serial_number)

                                                    #

# class Card:
#     def __init__(self):
#         self.__pin = 1234
#         self._pin2 = "0000"
#
#
# s1 = Card()
# print(dir(s1))
# print(s1._pin2)
# print(s1._Card__pin)

                                                    #

# class Bank:
#     def __calculate_commision(self, amount):
#         return amount * 0.05
#
#     def send_money(self, amount):
#         return print(f'Коммичия составила: {self.__calculate_commision(amount)}')
#
#
# s1 = Bank()
# s1.send_money(100)

                                                    #
# public, private, guard
# class BankAccount:
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     #вызов приватного метода
#     def print_data(self):
#         self.__print_private_data()
#
#     #защищённый метод
#     def print_guard_data(self):
#         print(self._name, self._balance, self._passport)
#
#     #приватный метод
#     def __print_private_data(self):
#      print(self.__name, self.__balance, self.__passport)
#
#
# account1 = BankAccount("Bank Account 1", 1000, 3423423423)

# account1.print_data()
# account1.print_guard_data()
# account1.print_private_data()
# account1.print_data()
# print(dir(account1))
#вызов приватного метода
# account1._BankAccount__print_private_data()

# print(account1._name)
# print(account1._balance)
# print(account1._passport)

                                                        #

# class Student:
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f'Имя: {self.__name}')
#         print(f'Возраст: {self.__age}')
#         print(f'Направление: {self.__branch}')
#
#     def access_private_method(self):
#         self.__display_details()
#
#
# adam = Student("Adam Smith", 25, "Information Technology")
# adam.access_private_method()

                                        #

# class BankDeposit:
#     def __init__(self, name, balance, rate):
#         self.name = name
#         self.balance = balance
#         self.rate = rate
#
#     def __calculate_profit(self):
#         return  self.balance * (self.rate / 100)
#
#     def get_balance_with_profit(self):
#         return self.balance + (self.balance  * self.rate/ 100)
#
#
# account_2 = BankDeposit("Sarah Connor", 200, 27)
# print(account_2.name)
# print(account_2.balance)
# print(account_2.rate)
# print(account_2._BankDeposit__calculate_profit())
# print(account_2.get_balance_with_profit())

                                                #

# class Library:
#
#     def __init__(self, books: list[str]) -> None:
#         self.__books = list(books)
#
#     def __check_availability(self, name) -> bool:
#         """принимает название книги и возращает bool"""
#
#         if name in self.__books:
#             return True
#         return False
#
#     def search_book(self, name) -> bool:
#         """ищет книгу в self.set_books при помощи __check_availability"""
#
#         if self.__check_availability(name):
#             return True
#         return False
#
#     def return_book(self, name) -> None:
#         """принимает название книги которую нужно вернуть в библиотеку"""
#         self.__books.append(name)
#
#     def _checkout_book(self, name) -> bool:
#         """принимает название книги если книга в наличие
#         уберает из списка и возврщает True"""
#
#         if self.search_book(name):
#             self.__books.remove(name)
#             return True
#         return False
# #
#
#
# # Напишите определение класса Library
#
#
# # Ниже код для проверки методов класса Library
# library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
#
# assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
# assert library.search_book("Moby-Dick") == True
# assert library.search_book("Jane Air") == False
#
# assert library._Library__check_availability("War and Peace") == True
# assert library._checkout_book("Moby-Dick") == True
# assert library._Library__books == ["War and Peace", "Pride and Prejudice"]
#
# assert library.search_book("Moby-Dick") == False
# assert library.return_book("Moby-Dick") is None
# assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
# assert library.search_book("Moby-Dick") == True
# print('Good')


                                                #

# class Employee:
#     def __init__(self, name: str, position: str, hours_worked: int, hourly_rate: int) -> None:
#         self.name = name
#         self.__position = position
#         self.__hours_worked = hours_worked
#         self.__hourly_rate = hourly_rate
#
#     def __calculate_salary(self) -> int:
#         """считает зарплату сотрудника, умножая отработанные часы на часовую оплату"""
#         return self.__hours_worked * self.__hourly_rate
#
#     def _set_position(self, position: str) -> None:
#         """принимает название должности и изменяет пользователю значение атрибута __position"""
#         self.__position = position
#
#     def get_position(self) -> str:
#         """возвращает атрибут __position"""
#         return self.__position
#
#     def get_salary(self) -> int:
#         """возвращает результат вызова приватного метода calculate_salary"""
#         return self.__calculate_salary()
#
#     def get_employee_details(self) -> str:
#         return f'Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}'
#
#
# employee = Employee("Джеки Чан", 'manager', 20, 40)
# assert employee.name == 'Джеки Чан'
# assert employee._Employee__hours_worked == 20
# assert employee._Employee__hourly_rate == 40
# assert employee._Employee__position == 'manager'
# assert employee.get_position() == 'manager'
# assert employee.get_salary() == 800
# assert employee._Employee__calculate_salary() == 800
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
# employee._set_position('Director')
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'
#
# employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
# assert employee_2._Employee__calculate_salary() == 1050
# assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'
#
# print('Good')



#                                                 #3.6 Геттеры, сеттеры, делитеры, свойства
#
# class BankAccount:
#     def __init__(self, name: str, balance: int) -> None:
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self) -> int:
#         return self.__balance
#
#     def set_balance(self, value) -> None:
#         if not isinstance(value, (int, float)):
#             raise ValueError('Баланс должен быть числом')
#         self.__balance = value
#
#     def delete_balance(self) -> None:
#         del self.__balance
#
#     balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
#
#
#
# a = BankAccount("Vasya", 100)
# a.name = 'Ivan'
#
# a.balance = 550
#
# del a.balance
#
# print(a.__dict__)

                                                #

# class BankAccount:
#     def __init__(self, account_number: int, balance: int):
#         self._account_number = account_number
#         self._balance = balance
#
#     def get_account_number(self) -> int:
#         return self._account_number
#
#     def get_balance(self) -> int:
#         return self._balance
#
#     def set_balance(self, balance) -> None:
#         if isinstance(balance, (int, float)):
#             self._balance = balance

                                                #

# class Employee:
#     def __init__(self, name: str, salary: int) -> None :
#         self.__name = name
#         self.__salary = salary
#
#     def __get_name(self) -> str:
#         """приватный геттер метод для атрибута __name"""
#         return self.__name
#
#     def __get_salary(self) -> int:
#         """приватный геттер метод для атрибута __salary"""
#         return self.__salary
#
#     def __set_salary(self, value) -> None:
#         """__salary: он должен позволять сохранять в атрибут __salary только положительные числа"""
#         if not isinstance(value, (int, float)):
#             print(f'ErrorValue:{value}')
#
#         if isinstance(value, (int, float)):
#             if value <= 0:
#                 print(f"ErrorValue:{value}")
#                 return
#
#             self.__salary = value
#
#
#     title = property(fget=__get_name)
#     reward = property(fget=__get_salary,fset=__set_salary)
#
#
# # Ниже код для проверки методов класса Employee
# employee = Employee("John Doe", 50000)
# assert employee.title == "John Doe"
# assert employee._Employee__name == "John Doe"
# assert isinstance(employee, Employee)
# assert isinstance(type(employee).title, property), 'Вы не создали property title'
# assert isinstance(type(employee).reward, property), 'Вы не создали property reward'
#
# assert employee.reward == 50000
# employee.reward = -100  # ErrorValue:-100
#
# employee.reward = 1.5
# assert employee.reward == 1.5
#
# employee.reward = 70000
# assert employee.reward == 70000
# employee.reward = 'hello'  # Печатает ErrorValue:hello
# employee.reward = '777'  # Печатает ErrorValue:777
# employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
# assert employee.reward == 70000
# employee._Employee__set_salary(55000)
# assert employee._Employee__get_salary() == 55000

                                                        #

# class UserMail:
#     def __init__(self, login: str, email: str):
#         self.login = login
#         self.email = email
#
#     def get_email(self) -> str:
#         return self.__email
#
#     def set_email(self, new_email) -> None:
#         if isinstance(new_email, str):
#             if (new_email.count('@')) == 1 and '.' in new_email.split('@')[1] and new_email.count('.') == 1:
#                 self.__email = new_email
#
#             else:
#                 print(f'ErrorMail:{new_email}')
#         else:
#             print(f'ErrorMail:{new_email}')
#
#     email = property(get_email, set_email)
#
#
# jim = UserMail("aka47", 'hello@com.org')
# print(jim.login)
# print(jim._UserMail__email)
# print(isinstance(type(jim).email, property))
# print(jim.email)
# try:
#     jim.email = [1, 2, 3]
# except ValueError as e:
#     print(e)
# try:
#     jim.email = 'hello@@re.ee'
# except ValueError as e:
#     print(e)
# jim.email = 'hello@re.w3'
# print(jim.email)

                                                #

# class UserMail:
#     storage_user_mail = {}
#
#     def __init__(self, login: str, email: str) -> None:
#         self.login = login
#         self.email = email
#
#     def get_email(self) -> str:
#         return self.__email
#
#     def set_email(self, new_email) -> None:
#         if not isinstance(new_email, str):
#             raise TypeError(f"ErrorMail: {new_email} не является строкой")
#         if (new_email.count('@')) == 1 and '.' in new_email.split('@')[1] and new_email.count('.') == 1:
#             self.__email = new_email
#             UserMail.storage_user_mail[self.login] = new_email
#
#         else:
#             raise ValueError(f'ErrorMail:{new_email}')
#
#     def get_login(self) -> str:
#         return self.__login
#
#     def set_login(self, new_login) -> None:
#         if not isinstance(new_login, str):
#             raise TypeError(f'{new_login} не является строкой')
#
#         if new_login in UserMail.storage_user_mail:
#             if hasattr(self, '_UserMail__login') and self.__login == new_login:
#                 return
#             raise ValueError(f'Логин {new_login} уже имеется в системе')
#
#         if hasattr(self, '_UserMail__login'):
#             UserMail.storage_user_mail.pop(self.__login)
#
#         self.__login = new_login
#         UserMail.storage_user_mail[new_login] = getattr(self, 'email', None)
#
#
#     email = property(get_email, set_email)
#     login = property(get_login, set_login)
#
#
#
# jim = UserMail("aka47", 'hello@com.org')
# print(isinstance(type(jim).login, property)) # Проверка на наличие свойства login
# print(f'Jim login is {jim.login}')
# try:
#     bim = UserMail("aka47", 'world@com.org') # Попытка создать экземпляр с занятым логином
# except ValueError as e:
#     print(e)
# jim.login = 'aka48'
# print(f'Jim login is {jim.login}')
# bim = UserMail("aka47", 'world@com.org')
# print(f'Bim login is {bim.login}')
#
# for value in [True, [1, 2, 3], 5, {'a': 'b'}]:
#     try:
#         UserMail(value, 'world@com.org')
#     except TypeError as e:
#         print(e)
#
# users = [
#     UserMail("person", 'hello@com.org'),
#     UserMail("person1", 'hello1@com.org'),
#     UserMail("person2", 'hello2@com.org'),
# ]
#
# try:
#     UserMail("person1", 'hello3@com.org')
# except ValueError as e:
#     print(e)
#
# try:
#     UserMail("person2", 'hello4@com.org')
# except ValueError as e:
#     print(e)
#
# r = UserMail("person3", 'hello5@com.org')
# print(r.login)
#
# print(UserMail.storage_user_mail)


                                                #3.7 Декоратор Property

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def my_balance(self):
#         print('get_balance')
#         return self.__balance
#
#     @my_balance.setter
#     def my_balance(self, value):
#         print('set_balance')
#         if not isinstance(value, (int, float)):
#             raise ValueError('Баланс должен быть числом')
#         self.__balance = value
#
#     @my_balance.deleter
#     def my_balance(self):
#         print('delete_balance')
#         del self.__balance
#
#     # my_balance = property(my_balance)                     #декоратор getter
#     # my_balance = my_property_balance.setter(my_balance)   #декоратор setter
#     # my_balance = my_balance.deleter(delete_balance)       #декоратор deliter
#
#
#
# a = BankAccount('Ivan', 100)
# a.my_balance = 34343
# x = a.my_balance = 100
#
# a._BankAccount__balance = 232399
#
#
# print(a.my_balance)
# print(a.__dict__)

                                                #

# class MagicalBox:
#     def __init__(self, contents=None):
#         self._contents = contents
#
#     @property
#     def contents(self):
#         if self._contents == "rabbit":
#             return "🐇 A magical rabbit!"
#         else:
#             return self._contents
#
#     @contents.setter
#     def entity(self, new_contents): # вот тут поменялось название
#         if new_contents == "wishes":
#             print("🌟 Your wishes are granted!")
#             self._contents = new_contents
#         else:
#             print("✨ The magic didn't work this time.")
#             self._contents = new_contents
#
#
# box = MagicalBox("rubies")
#
# box.contents = "32"
# print(box.contents)

                                                #

# class Celsius:
#     def __init__(self, celsius: int) -> None:
#         self._celsius = celsius
#
#     def to_fahrenheit(self) -> float:
#         return (self._celsius * 9 / 5) + 32
#
#     @property
#     def temperature(self) -> float:
#         return self._celsius
#
#     @temperature.setter
#     def temperature(self, new_value: int) -> None:
#         if new_value < -273.15:
#             raise ValueError('Temperature must be greater than or equal to 273.15')
#         self._celsius = new_value
#
#
#
#
# celsius = Celsius(25)
# assert celsius.temperature == 25
# assert celsius.to_fahrenheit() == 77.0
#
# celsius.temperature = 30
# assert celsius.temperature == 30
# assert celsius.to_fahrenheit() == 86.0
#
# print('Good')

                                                    #

# class File:
#     def __init__(self, size_in_bytes) -> None:
#         self._size_in_bytes = size_in_bytes
#
#     @property
#     def size(self) -> str:
#         b = self._size_in_bytes
#         if b < 1024:
#             return f'{b} B'
#         if b < 1024**2:
#             return f'{b / 1024:.2f} KB'
#         if b < 1024**3:
#             return f'{b / 1024**2:.2f} MB'
#         if b < 1024**4:
#             return f'{b / 1024**3:.2f} GB'
#
#     @size.setter
#     def size(self, new_value) -> None:
#         self._size_in_bytes = new_value
#
#
# file = File(5)
# assert file.size == "5 B"
# file.size = 1023
# assert file.size == "1023 B"
# file.size = 1024
# assert file.size == "1.00 KB"
#
# file_1 = File(1500000)
# assert file_1._size_in_bytes == 1500000
# assert file_1.size == "1.43 MB"
#
# file_2 = File(1500)
# assert file_2.size == "1.46 KB"
#
#
# file_3 = File(2789326322)
# assert file_3.size == "2.60 GB"
# file_3.size = 1073741824
# assert file_3.size == "1.00 GB"
#
# print('Good')

                                                    #

# class Notebook:
#     def __init__(self, notes: list[str]) -> None:
#         self._notes = notes
#
#     @property
#     def notes_list(self) -> None:
#         for index, unit in enumerate(self._notes, 1):
#             print(f'{index}.{unit}')
#
#
#
# #првоерки
# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list
#
# note = Notebook(list(range(10, 20)))
# note.notes_list
# try:
#     note.notes_list = [3, 4, 3] # при попытке сохранить новое значение должна быть ошибка
# except AttributeError:
#     pass

                                                    #

# class Money:
#     def __init__(self, dollar: int, cents: int) -> None:
#         self.total_cents = (dollar * 100) + cents
#
#     @property
#     def dollars(self) -> int:
#         """возвращает количество имеющихся долларов"""
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, new_dollar) -> None:
#         """устанавливает при помощи него новое значение в атрибут экземпляра total_cents"""
#         if isinstance(new_dollar, int) and new_dollar >= 0:
#             self.total_cents = (new_dollar * 100) + (self.total_cents % 100)
#         else:
#             print('Error dollars')
#
#     @property
#     def cents(self) -> int:
#         """возвращает количество имеющихся центов"""
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, new_cents) -> None:
#         if isinstance(new_cents, int) and 0 <= new_cents < 100:
#             self.total_cents = (self.dollars * 100) + new_cents
#         else:
#             print('Error cents')
#
#     def __str__(self) -> str:
#         return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
#
#
# bill = Money(101, 99)
# assert isinstance(bill, Money)
#
# print(bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(bill.dollars, bill.cents)  # 101 99
# bill.dollars = 666
# print(bill)  # Ваше состояние составляет 666 долларов 99 центов
# bill.cents = 12
# print(bill)  # Ваше состояние составляет 666 долларов 12 центов
# assert bill.total_cents == 66612
# assert list(bill.__dict__.keys()) == ['total_cents']
#
# ken = Money(111, 90)
# assert isinstance(ken, Money)
# print(ken)
# ken.dollars = 'hello'  # Error dollars
# ken.dollars = 0
# print(ken)
# ken.cents = [1, 2, 3]  # Error cents
# ken.cents = 100  # Error cents
# ken.cents = 99
# print(ken)

                                                    #

# class TimeZone:
#     def __init__(self, name: str, offset_hours: int, offset_minutes: int) -> None:
#         self.name = name
#         self.offset_hours = offset_hours
#         self.offset_minutes = offset_minutes
#
#     @property
#     def name(self) -> str:
#         return self._name
#
#     @name.setter
#     def name(self, value: str) -> None:
#         """Отбросить все незначимые проблемы .strip()
#          Если входное имя часового пояса не удовлетворяет этим требованиям, выкидывайте исключение"""
#         if not isinstance(value, str) or not value.strip():
#                 raise ValueError(f'Timezone bad name - {value}')
#
#         self._name = value.strip()
#
#     @property
#     def offset_hours(self) -> int:
#         return self._offset_hours
#
#     @offset_hours.setter
#     def offset_hours(self, number: int) -> None:
#         """должно позволять сохранять смещение по часам -
#         допускаются только целые числа от -12 до 14 включительно,
#         Если входное смещение по часам не удовлетворяет этим требованиям, выкидывайте исключение"""
#         if not isinstance(number, int):
#             raise ValueError(f'Hour offset must be an integer.')
#         if not -12 <= number <= 14:
#             raise ValueError('Offset must be between -12:00 and +14:00.')
#
#         self._offset_hours = number
#
#     @property
#     def offset_minutes(self) -> int:
#         return self._offset_minutes
#
#     @offset_minutes.setter
#     def offset_minutes(self, number: int) -> None:
#         """должно позволять сохранять смещение по минутам -
#         допускаются только целые числа от -59 до 59 включительно
#         . Если входное смещение по минутам не удовлетворяет этим требованиям, выкидывайте исключение"""
#         if not isinstance(number, int):
#             raise ValueError('Minutes offset must be an integer.')
#         if not -59 <= number <= 59:
#             raise ValueError('Minutes offset must between -59 and 59.')
#
#         self._offset_minutes = number
#
#
#
# tz1 = TimeZone('ABC', -2, -15)
# print(tz1.name)
# print(tz1.offset_hours)
# print(tz1.offset_minutes)
#
# tz1.name = 'XYZ'
# tz1.offset_hours = 12
# tz1.offset_minutes = 0
#
# try:
#     tz1.offset_hours = 67
# except ValueError as e:
#     print(e)
# print(tz1.name, tz1.offset_hours, tz1.offset_minutes)
#
# for name in ['', None, '    ', 123, (1, 3), True]:
#     try:
#         TimeZone(name, 5, 34)
#     except ValueError as e:
#         print(e)
#
# try:
#     TimeZone(' Abc ', -20.5, 34)
# except ValueError as e:
#     print(e)
#
# try:
#     TimeZone(' Abc ', -15, 34)
# except ValueError as e:
#     print(e)
#
# try:
#     TimeZone(' Abc ', 15, 34)
# except ValueError as e:
#     print(e)
#
# tz = TimeZone(' Abc ', 10, 34)
# print(tz.name)
# print(tz.offset_hours)
# print(tz.offset_minutes)






































