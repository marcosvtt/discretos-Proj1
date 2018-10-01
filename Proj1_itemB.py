
#1
def n_bits(N):  #1
	i = 2048
	if N== 0:
		return 0

	while (N % (pow(2,i))) == N:
		i = i-1
		print('.')

	return i+1


#2
def soma(a, b):
	n_a = n_bits(a)
	n_b = n_bits(b)
	ans = a + b
	n_ans = n_bits(ans)

	if (n_a+n_b) == n_ans or (n_a+n_b) == (n_ans+1):
		return ans

	else:
		return -1


#3
def multiplicacao(a, b):
	n_a = n_bits(a)
	n_b = n_bits(b)

	if (n_a+n_b) > 2048:
		print(n_a+n_b)
		return -1

	else:
		return a*b 

#4
def div_mod(a,b):
	ans = divmod(a,b) # a dividido por b
	print("quociente:",ans[0],"\nresto: ",ans[1])


