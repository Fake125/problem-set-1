# problem-set-1
my python code solutions to solve a set of defined problems

## Probem_1
You are given strings S and C. String S repersents a table in CSV(comma-seperated values) format, where rows are seperated by new line characters('\n') and each row consists of one or more fields sperated by commmas(',').

The first row contains the names of the columns. The following rows contain values.

id | name | age | act | room | dep. |
---|------|-----|----|------|-------|
1  | jack | 68  | T  | 13   | 8     |
17  | betty | 28  | F  | 15   | 7   |

For example, the table below is presented by the following string: S="id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7" 
String C is the name of column in the table described by S that contains only integers. Your task is to find maximum value in that column. in the example above, for c = "age", the maximum value is 68.

Write a function:
def solution(S,C) 

Examples:

1. Given S="id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7" C="age" your function should return 68 since 68 is the maximum of 68 and 28.

2. Given S= "area,land,\n3722,CN\n6612,RU\n3855,CA\n3797,USA" C="area" your function should return 6612.

area | land
-----|-----|
3722 | CN  |
6612 | RU  |
3855 | CA  |
3797 | USA |


## Problem_2
You are given an array of integers, where positive numbers represent revenues and negative numbers represent expenses, all in chronological order. In one move you can relocate any expense(negative number) to the end of the array. What is the minimum number of such relocations to make sure that the company never falls into debt(in other words: you need to ensure that there is no consecturive sequence of elements starting from the beginning of the array, that sums up to a negative number)?

you can assume that the sum of all elements in A is nonnegative.

write a function:

def solution(A)
that, given an array A of N integers, returns the minimum number of relocations, so that company never falls into debt.

Examples:

1. Given A= [10,-10,-1,-1,10], the function should return 1. it is enough to move -10 to the end of the array.

2. Given A= [5,-2,-3,1], the answer is 0. The company balance is always nonnegative.


## Problem_3
There is a cleaning robot which is cleaning a rectangular grid of size N*M, represented by array R consisting of N strings. Rows are numbered from 0 to N-1(from top to bottom) and columns are numbered from 0 to M-1(from left to right).

The robot starts cleaning in the top-left corner, facing rightwards . it moves in a straight line for as long as it can, i.e. while there is an unoccupied grid square ahead of it. When it cannot move forward, it rotates 90 degrees clockwise and tries to move forward again until it encounters another obstacle, and so on. Dots in the array (".") represents empty squaeres and "X"s represent occupied squares (ones the robot cannot move through). Each square that the robot occupied at least once is considered clean. The robot moves indefinitely. 

write a function: 

def solution(R)
that, given an array R consisting of N strings, each of length M, representing the grid, returns the number of clean squares.

Examples:

1. Given A = ["...X..","....XX","..X..."] , your function should return 6.
![5](https://user-images.githubusercontent.com/77664485/138788103-77bb13a1-4aed-4d61-a440-ea77c515ca46.png)

2. Given A = ["....X..","X......",".....X.","......."] , your function should return 15.

