#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
  size = 0
  try:
    for index in range(x):
      if type(my_list[index]) is not int:
        continue
      else:
        print("{:d}".format(my_list[index]), end="")
        size += 1
      print("")
      return size
  except(TypeError, IndexError, ValueError):
      pass
