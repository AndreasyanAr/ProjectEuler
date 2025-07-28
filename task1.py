sum_nums = 0
for i in range(0,100000001):
    if i % 3 == 0 or i % 5 == 0:
        sum_nums += i

print(sum_nums)
# This code calculates the sum of all numbers from 0 to 10000 that are divisible by 3 or 5.
