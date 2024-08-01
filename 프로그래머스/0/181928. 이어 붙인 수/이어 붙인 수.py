def solution(num_list):
	odd_nums = ""
	even_nums = ""

	for num in num_list:
		if num % 2 == 1:
			odd_nums += str(num)
		else:
			even_nums += str(num)

	odd_sum = int(odd_nums) if odd_nums else 0
	even_sum = int(even_nums) if even_nums else 0

	return odd_sum + even_sum