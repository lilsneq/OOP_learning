#импорты




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
































