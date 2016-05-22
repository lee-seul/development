# coding: utf-8
# caesar.py

def caesar(s, n):
    result = ""
    n %= 26
    for char in s:
        temp = ord(char)
        if temp == 32:
            result += " "
        elif temp >= 65 and temp <= 90:
            temp += n
            if temp  > 90:
                temp -= 26
            result += chr(temp)
        elif temp >= 97 and temp <= 122:
            temp += n
            if temp > 122:
                temp -= 26
            result += chr(temp)
    return result
            

#def caesar(s, n):
#    result = ""
#    for char in s:
#        if ord(char) == 32:
#            result += " "
#        else:   
#            result += chr(ord(temp) + (n%26) - 26)
#    return result
