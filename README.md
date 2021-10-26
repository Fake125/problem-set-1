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
