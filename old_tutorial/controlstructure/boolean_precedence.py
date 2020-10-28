"""
1: not
2: and
3: or
parentheses can be used to change precedence
"""

T, F = True, False

print('"True and False or not True and False or not True" is',
      T and F or not T and F or not T)

print('"True or (False or not True) and (False or True)" is',
      T or (F or not T) and (F or T))
