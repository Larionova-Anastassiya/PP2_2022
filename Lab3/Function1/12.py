def histogram(my_list):
  for n in my_list:
    print (n * "*")

my_list = list(map(int, input().split(",")))
histogram(my_list)

"""
input: 3,5,2
output:
***
*****
**
"""