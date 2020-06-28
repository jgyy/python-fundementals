def is_prime(num):
    return not True in [num % i == 0 and num / i != 1.0 for i in range(2, num + 1)]

for i in range(1,999):
	if is_prime(i + 1):
			print(i+1,end=" ")
