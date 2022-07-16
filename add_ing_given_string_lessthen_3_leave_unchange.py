'''write a python progame to add 'ing' at the end of a given string
(lenth should be at least  3). if the given string length of the given
 string is less than 3, leae it unchange'''

string = input()
if len(string) < 3:
  print(string)
elif string[-3:] == 'ing':
  print(string + 'ly')
else:
  print(string + 'ing')