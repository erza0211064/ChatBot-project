'''
Function to check two string is equal or not
if equal:True
if not equal: return a string tells the different part of string 1 and 2
'''

def diff(str1,str2):
  diff1 = ""
  diff2 = ""
  while True:
    if len(str1) > len(str2):
      str2 +=" "
    elif len(str1) < len(str2):
      str1 +=" "
    else:
      break
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      diff1 += str1[i]
      diff2 += str2[i]
      
  if diff1 == "" and diff2 == "":
    return True
  else:
    res ="str1:"+ diff1 + "  " + "str2:"+ diff2
    return res
    
