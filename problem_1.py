def solution(s,c):
    lines = s.split("\n")
    cells = lines[0].split(",")
    counter = 0
    target_cell_index = -1
    for counter in range(0,len(cells)):
        if c == cells[counter]:
            target_cell_index = counter
            break
        counter = counter +1
    max = -100000
    for line_index in range(1,len(lines)):
        cells = lines[line_index].split(",")
        if int(cells[target_cell_index]) > max:
            max = int(cells[target_cell_index])
        line_index = line_index +1
    return max

# s = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"
# c = "age"
# s = "area,land,\n3722,CN\n6612,RU\n3855,CA\n3797,USA"
# c = "area"
# print(solution(s,c))