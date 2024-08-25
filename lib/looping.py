#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)
        i -= 1

def square_integers(int_list):
    squared_value = []
    for i in range(len(int_list)):
        squared_value.append(int_list[i]**2)
    return squared_value
    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
