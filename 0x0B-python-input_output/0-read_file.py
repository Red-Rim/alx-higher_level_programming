#!/usr/bin/python3
"""reads a text file"""



def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdou"""
  
  with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')

