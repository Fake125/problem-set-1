A = [10,-10,-1,-1,10]
#A = [5,-2,-3,1]
#A = [-1,-1,-1,1,1,1,1]

def shift(arr,base,alt):
    temp = arr[base]
    arr[base] = arr[alt]
    arr[alt] = temp

def find_shifter(arr,sum):
    c = len(arr)-1
    while c > -1:
        if sum + arr[c] > 0:
            return c
        c = c - 1

def solution(arr):
    sum = 0
    counter = 0
    output = 0
    while counter < len(arr):
        sum = sum + arr[counter]
        if sum < 0:
            sum = sum - arr[counter]
            shift(arr,counter,find_shifter(arr,sum))
            output = output +1
            counter = 0
            sum = 0
            continue
        counter = counter + 1
    return output

print(solution(A))
