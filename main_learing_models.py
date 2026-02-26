#начало учебного проекта по ООП
from os import pread


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

class Car:
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def drive():
        print("drive")

    @staticmethod
    def wheel():
        return 'wheel'


Car.drive()

b = Car()
b.drive()
b.wheel()
print(f'b.wheel - {b.wheel()}')














