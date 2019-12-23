N# Task description
#
# Given an 2D board (represented by array) - can you find a battleship on it?
# Battleship length is always 3 elements.
# Battleship can be either horizontal either vertical
# Battleship can be in any part of array
# Only one Battleship per array
# Size of array can vary
# function should return array of arrays with battleship coordintates.
#
# The battleship is represented with '1' and empty slots are represented with 0s.
# 
# Examples for 5x5 arrays:
# Input:
# 
# 0 0 0 0 0
# 1 0 0 0 0
# 1 0 0 0 0
# 1 0 0 0 0
# 0 0 0 0 0
#

# Output:
# [[1,0],[2,0],[3,0]]
# 
# Input:
# 
# 0 0 0 0 0
# 0 1 1 1 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 
# same input represented as a two dimension array:
# a = [[0,0,0,0,0], [0,1,1,1,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
# Output:
# [[1,1],[1,2],[1,3]]

# is it 0 or 1
# find element in each list - 0 or 1
# find element - take index
# if element in general list - 1 = first element - first sublist - [1,xxx]
# second element result list - position (find) 

a = [[0,0,0,0,0], [0,1,1,1,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

result_list = []

count = 0
for sub_list in a:
    for i in range(len(sub_list)):
        if sub_list[i] == 1:
            sub_result_list = []
            sub_result_list.append(count)
            sub_result_list.append(i)
            result_list.append(sub_result_list)
    count +=1
print(result_list)











            
            
        








