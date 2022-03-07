#Write a python program to convert snake case string to camel case string.
import re

def camel(ans):
    return ''.join(x.capitalize() or '_' for x in ans.split('_'))
#capitalize - позволяет вернуть копию строки str с первым символом в верхнем регистре, а остальные символы будут в нижнем регистре
#join вместе выполнит
x = input()
print(camel(x))
"""
Example:

python_exercises --> PythonExercises
active_record --> ActiveRecord

"""