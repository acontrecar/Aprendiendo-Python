# name = input("What is your name? ")

# print("Hello, " + name + "!")

# Fundamental Data Types
# int , float , str , bool, list, tuple, dict, set, None

# print(2+4)
# print(type(2+4.1))

# Classes -> custom types

# Specialized Data Types


#math functions
# print(round(3.1))
# print(abs(-20))

# operator precedence
# print(20-3*4)

# print(bin(5))
# print(int('0b101', 2))

# iq = 190
# user_age = iq/4
# a = user_age
# print(a)

# constants
# PI = 3.14

# long_string = '''
# WOW
# O O
# ---
# '''
# print(long_string)

# username = 'supercoder'
# password = 'supersecret'
# long_string = username + ' ' + password
# print(long_string)

# string concatenation
# first_name = 'John'
# last_name = 'Smith'
# full_name = first_name + ' ' + last_name
# print(full_name)

# Escape Sequence
# weather = "It\'s \"kind of\" sunny"
# print(weather)

# name = 'Johnny'
# age = 55
# print(name + f' is {age} years old')
# print(f'Pi is approximately {22/7:12.50f}')
# print('hi {0}. You are {1} years old'.format('Johnny', 55))

# selfish = '0123456789'
# print(selfish[0:20])
# print(selfish[0:8:1])
# print(selfish[::-1])

# selfish[start:stop:stepover]

# print(len('helloooooo'))
# greet = 'helloooooo'
# print(greet[0:len(greet)])

# quote = 'to be or not to be'
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))
# print(quote)

#booleans
# name = "Antonio"
# is_cool = False

# is_cool = True

# print(bool(1))

# name = "Antonio"
# age = 21
# relationship_status = "Casado"

# birth_year = input('What year were you born? ')
# age = 2023 - int(birth_year)
# print(f'Your age is: {age}')

# password = input('Introduce tu contraseña:')
# tamanio = len(password)
# passwordShow = '*' * tamanio

# print(f'password {passwordShow} is {tamanio} letters long')

# li = [1, 2, 3, 4, 5]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2, 'a', True]
# amazon_cart = ['notebooks', 'sunglasses']
# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)

# basket = ["a", "x", "b", "c", "d", "e", "d"]
# basket.sort()
# basket.reverse()
# print(basket)

# print(list(range(10, 100)))

# sentence = " "
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Antonio'])
# print(new_sentence)

# list unpacking
# a , b , c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# # Dictionary
# dictionary = {
#     'a': [1, 2, 3],
#     'b': 'hello',
#     'x': True,
#     'age': 22
# }

# print(dictionary['a'][1])
# print(dictionary)
# print(dictionary.get('age'))
# user2 = dict(name='JohnJohn')
# print(user2)
# print('age' in dictionary.keys())
# print(dictionary.items())
# print("Paco")
# print(dictionary.update({'age': 55}))

# my_list = [
#     {
#         'a': [1, 2, 3],
#         'b': 'hello',
#         'x': True
#     },
#     {
#         'a': [4, 5, 6],
#         'b': 'hello',
#         'x': True
#     }
# ]
# print(my_list[0]['a'][2])


#Turple
# my_tuple = (1, 2, 3, 4, 5)
# print(5 in my_tuple)
# new_tuple = my_tuple[1:2]
# print(new_tuple)

# SET
# my_set = {1, 2, 3, 4, 5, 5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# your_set = {4, 5, 6, 7, 8, 9, 10}
# print(my_set.difference(your_set))

# my_set.discard(5)
# print(my_set)


# print(my_set.isdisjoint(your_set))
# print(my_set.union(your_set))

# is_old = False
# is_licensed = True

# if is_old and is_licensed:
#     print('You are old enough to drive and you have a license')
# elif is_licensed:
#     print('You can drive now')
# else:
#     print('You are not of age')
    
#     print('okokok')


# Ternary Operator
# condition_if_true if condition else condition_if_else
# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"
# print(can_message)

#Short Circuiting
# is_Friend = True
# is_User = True
# print(is_Friend and is_User)


# for item in [1, 2, 3, 4, 5]:
#     for x in ['a', 'b', 'c']:
#         print(item, x)

# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)

# for item in user.items():
#     key , value = item
#     print(key, value)

# counter
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

# counter = 0
# for item in my_list:
    # counter += item

# print(counter)

# for _ in range(0, 10, 2):
    # print(_)
    
# for i,char in enumerate(list(range(100))):
    # print(i,char)
    
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:
#     print('done with all the work')
    
# while True:
#     response = input('Say something: ')
#     if (response == 'bye'):
#         break
    
# my_list = [1, 2, 3]
# i = 0
# while i < len(my_list):
#     print(my_list[i]) 
#     i += 1
   
# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]

# fill = '*'
# empty = ' '
# for row in picture:
#     for pixel in row:
#         if (pixel):
#             print(fill, end='') # Este end es para que no haga un salto de linea
#         else:
#             print(empty, end='')  
#     print('') # Este es para que haga un salto de linea
    
    
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []

# for item in some_list:
#     if some_list.count(item) > 1:
#         # some_list.remove(item)
#         if item not in duplicates:
#             duplicates.append(item)  
    
# print(duplicates)
    

    
    
# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]

# fill = '*'
# empty = ' '

# def show_tree():  
#  for row in picture:
#     for pixel in row:
#         if (pixel):
#             print(fill, end='') # Este end es para que no haga un salto de linea
#         else:
#             print(empty, end='')  
#     print('') # Este es para que haga un salto de linea
    
# show_tree()
    
    
# def say_hello(name = "Jorge", emoji = ":)"):
#     print(f'Hello {name} {emoji}')
    
# say_hello('Antonio', 'paco')

# say_hello(emoji=':)', name='Antonio') # Bad practice

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2)
    # return 5
    # print('hello')

# total = sum(10, 20)
# print(total) 

# def input_age(age=0):
#     age = int(input('What is Your Age:'))
#     if age < 18:
#      return 'sorry, you are too young to drive this car, powering off'
#     elif age > 18:
#      return 'Powering On, Enjoy your ride!!!'
#     else:
#         return 'Congratulations on your first year of driving. Enjoy the ride!!!'

# print(input_age())

# def test(a):
#     '''
#     Info: this function tests and prints param a
#     '''
#     print(a)
    
# print(test.__doc__)

# Clen code

# def is_odd_or_even(num):
#     if num % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
    
# print(is_odd_or_even(51))

# *args **kwargs

# def super_func(name, *args, i='hi', **kwargs):
    #print(args)
    #print(kwargs)
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return sum(args) + total

# print(super_func('Antonio',1,2,3,4,5, num1=5, num2=10))

# Rule : params, *args, default parameters, **kwargs


# def highest_even(li):
#     evens = []
#     for item in li:
#         if item%2 == 0:
#             evens.append(item)
#     return max(evens)
    
# print(highest_even([10,2,3,4,22,8,11]))


# Scope - what variables do I have acces to?\
# def some_function():
#     total = 100

# print(total)

# total = 0

# def count():
#     global total
#     total += 1
#     return total

# count()
# count()
# print(count())

# def outer():
#     x = "local"
    
#     def inner():
#         nonlocal x # Esto es para que tome el valor de la variable x de la funcion outer
#         x = "nonlocal"
#         print("inner:", x)
        
#     inner()
#     print("outer:", x)
    
# outer()

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(list(map(multiply_by2, [1,2,3])))

# my_list = [1,2,3]

# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, my_list)))
# print(my_list)

# my_list = [1,2,3]

# def check_odd(item):
#     return item % 2 != 0

# print(list(filter(check_odd, my_list))) # Filter return only the values that are true
# print(my_list)

# my_list = [1,2,3]
# your_list = [10,20,30,40]

# def check_odd(item):
#     return item % 2 != 0


# print(list(zip(my_list,your_list))) # Filter return only the values that are true
# print(my_list)

# from functools import reduce

# my_list = [1,2,3]

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumulator, my_list , 0)) # Filter return only the values that are true
# print(my_list)


# list, set, dictionary comprehension

# my_list = [char for char in 'hello']
# my_list2 = [num*2 for num in range(0, 100)]
# my_list3 = {num for num in range(0, 100) if num % 2 == 0}


# # for char in 'hello':
# #     my_list.append(char)
    
# print(my_list)
# print(my_list2)
# print(my_list3)

# simple_dict = {
#     'a': 1,
#     'b': 2
# }

# my_dict = {key:value**2 for key,value in simple_dict.items() if value%2 == 0}

# my_dict = {num:num*2 for num in [1,2,3]}

# print(my_dict)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = list(set([item for item in some_list if some_list.count(item)>1]))

# print(duplicates)

import utility
import shopping.shopping_cart

print(shopping.shopping_cart.buy('apple'))