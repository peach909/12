# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def decorator_function(func):
   def wrapper():
   print('функция-обёртка!')
   print('оборачиваемая функция:{} '. format(func) )
   print('выполняем обёрнутую функцию...')
   func()
   print ('выходим из обёртки' ) 
   return wrapper 