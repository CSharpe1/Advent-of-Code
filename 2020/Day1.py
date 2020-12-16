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
check = [4,23423 ,54457,786424,3233,2432,3453636,67565,5858,346346,25325,2424,3546,1700,1721, 979,366,299,675,1456]

target = 2020
# Function to find the 2 values that = 2020
a = 0
b = 1
check1 = check[a]
check2 = check[b]
while b < len(check):
    if (check[a] + check[b]) == 2020:
        break
    else:
        b +=1
    if b == len(check):
        a += 1
        b = 0
#   Find result
print("A = ", a)
print("Check a", check[a])
print("B = ", b)
print("Check b", check[b])

print("The total =  ",check[a]*check[b])
