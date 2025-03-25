"""
create list
"""
list1 = [1, 2, 3, 4]

list2 = list1[:]  # copy list

list3 = [*range(10, 60, 10)] # range -> list

list4 = [num for num in range(51)]

list5 = list() # formal name

list6 = [] # literal syntax
"""
list3 faster list4 
list6 faster list5
"""
nested_loop = [(num1, num2) for num1 in range(101) for num2 in range(101)]
matrix = [[col for col in range(5)] for row in range(5)]

condition_loop = [num ** 2 for num in range(51) if num % 2 == 0]

"""
process
"""
del list1[0]  # del element with index 0
