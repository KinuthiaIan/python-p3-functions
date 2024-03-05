#!/usr/bin/env python3

'''
  You should be able to call this function with no arguments and see its output in the terminal:
  greetProgrammer();
  => "Hello, programmer!"
  '''


def greet_programmer():
    print("Hello, programmer!")


'''
You should be able to call this function with one argument and see its output in the terminal:
  greet("Naureen");
  => "Hello, Naureen!"    
'''


def greet(name):
    print(f"Hello, {name}!")


'''
  You should be able to call this function with no arguments and see its output in the terminal:
  greetWithDefault();
  => "Hello, programmer!"

  You should also be able to call this function with one argument and see its output in the terminal:
  greetWithDefault("Sunny");
  => "Hello, Sunny!"
'''


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


'''
  You should be able to call this function with two arguments and get back its return value:
  const sum = add(1, 2);
  console.log(sum);
  => 3
'''


def add(num1, num2):
    return num1 + num2


'''
  You should be able to call this function with two arguments and get back its return value:
  const result = halve(4);
  console.log(result);
  => 2

  If the function is called with an argument that isn't a number, it should return null:
  const result = halve("two")
  => null
'''


def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
    else:
        return None
