'''write a python program to get string from a given string where all
 occurence of it's carecture  have been changed to '$', exept the first character it self '''

def change_char(str1):
  char = str1[0:]
  str1 = str1.replace(char, '$')
  str1 = str1 + char [1:]

  return str1

print(change_char('restart'))
