no_list = [0,2,2,1,2,1,1,0,2,1]
number_of_zeros = 0
number_of_ones = 0
number_of_twos = 0

for no in no_list:
	if no == 0:
		number_of_zeros+=1
	elif no == 1:
		number_of_ones+=1
	else:
		number_of_twos+=1
# print(number_of_zeros,number_of_ones,number_of_twos)

for i in range(number_of_zeros):
	print(0,end=" ")
for i in range(number_of_ones):
	print(1,end=" ")
for i in range(number_of_twos):
	print(2,end=" ")
