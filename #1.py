"""
take a number n and take its multiples 2n, 3n ...
what is the first multiple of n where all the 10 digits (0-9) are seen:
    154 (0,1,5)
    308 (0,1,3,5,8)
    462 (0,1,2,3,4,5,6,8)
    616 (0,1,2,3,4,5,6,8)
    770 (0,1,2,3,4,5,6,7,8)
    924 (0,1,2,3,4,5,6,7,8,9)

    end

    answer = 924
"""



number = int(input())

num = []

flag = True
i = 1
while flag == True:
    currnumber  = str(number * i)
    for j in currnumber:
        if j not in num:
            num.append(j)

    if len(num) == 10:
        break

    print(num, currnumber)
    
    i += 1

print (int(number) * i)
