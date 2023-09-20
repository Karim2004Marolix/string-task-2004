#7.Write a python program to find sum of integers in the string.
str1 = "Hello World 2345"
sum_num = 0
for x in str1:
	if x.isdigit() == True:
		z = int(x)
		sum_num = sum_num + z
print(sum_num)