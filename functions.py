# 1. Write a function named `sum_to()` that takes a number parameter `n` and returns the sum of the numbers from 1 to n.

# def sum_to(num):
# 	sum = 0
# 	if num == 0:
# 		return sum
# 	else:
# 		sum += num
# 		sum_to(num-1)

# print(sum_to(6))

def sum_to(num):
	sum = 0
	for i in range(num + 1):
		sum += i
	return sum

print(sum_to(6))

# 2. Write a function named `largest()` that takes a list parameter and returns the largest element in that list. You can assume the list contents are all *positive* numbers.

def largest(list):
	list.sort()
	return list[-1]

print(largest([1, 2, 4, 3]))

# 3. Write a function named `occurances()` that takes two string parameters and counts the number of occurrances of the second string inside the first string.

def occurances(string_one, string_two):
	return string_one.count(string_two)

print(occurances('fleep floop', 'e'))

# 4. Write a function named `product()` that takes an *arbitrary* number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on `*args`).

def product(*args):
	result = 1
	for i in args:
		result *= i
	return result
	
print(product(2, 2, 2))

