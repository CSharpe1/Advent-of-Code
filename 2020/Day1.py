'''
--- Day 1: Report Repair ---

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
'''
check = [1721,979,366,299,675,1456]

target = 2020
var1 = 0
var2 = 0
val2020 = False
#print(check[3])
time = 0
#print(len(check))

while time < len(check):
    print(check[time])
    time += 1

## find the 2 values that = 2020

counta = 0
countb = 1
while val2020 != True:
    var1 = check[counta] 
    while countb < len(check):
        if (check[counta] + check[countb]) == 2020:
            val2020 = True 
            vsum = check[counta] + check[countb]  
            print("Sum =", vsum )
        else:
            countb += 1
            print("Count b = ", countb)


print("END")