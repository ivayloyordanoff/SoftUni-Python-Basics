import sys

n = int(input())

max_num = -sys.maxsize
total_sum = 0

for i in range(1, n + 1):
    num = int(input())
    total_sum = total_sum + num
    if num > max_num:
        max_num = num

total_sum = total_sum - max_num

if total_sum == max_num:
    print("Yes")
    print(f"Sum = {total_sum}")
else:
    print("No")
    diff = abs(total_sum - max_num)
    print(f"Diff = {diff}")
