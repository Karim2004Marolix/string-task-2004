#6.Write a python program to remove all the blank spaces in a given string.
def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
    
print(remove_spaces("w 3 res ou r ce"))
print(remove_spaces("a b c"))