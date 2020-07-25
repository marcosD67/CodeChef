#Result: 100/100

for tc in range(int(input())):
	n = int(input())
	arr = [int(x) for x in input().split()]
	diff = 0

	for i in range(1, n):
		diff += abs(arr[i]-arr[i-1])-1
	print(diff)