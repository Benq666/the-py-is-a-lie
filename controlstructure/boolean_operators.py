"""
AND
True and True   True
True and False  False
False and True  False
False and False False
---
OR
True or True    True
True or False   True
False or True   True
False or False  False
---
NOT
Not True    False
Not False   True
"""

T, F = True, False

print('AND:'
      '\nTrue and True is\t', T and T,
      '\nTrue and False is\t', T and F,
      '\nFalse and True is\t', F and T,
      '\nFalse and False is\t', F and F,
      '\n\nOR:'
      '\nTrue or True is\t\t', T or T,
      '\nTrue or False is\t', T or F,
      '\nFalse or True is\t', F or T,
      '\nFalse or False is\t', F or F,
      '\n\nNOT:'
      '\nNot True is\t\t\t', not T,
      '\nNot False is\t\t', not F, sep='')
