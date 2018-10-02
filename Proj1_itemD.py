import random


def sqm3 (x, expoente, n):
	binario = bin(expoente)
	ans = 1
	lengh = len(binario)
	for i in reversed(range(lengh)):
		ans = (ans * ans) % n
		if binario[i] == 1:
			ans = (ans * x) % n
	return ans

def impar(p_1):
	k = 0
	while((p_1 % 2) == 0):
		p_1 = p_1 / 2
		k= k+1
	#print(k, p_1)
	return [k, int(p_1)]


def miller_rabim(p, s):
	p_1 = p - 1
	ans = impar(p_1)

	print(ans)

	for i in range(1, s):
		a = random.randint(2, p-2)
		b = sqm3(a, ans[1], p)
		print("a: ",a, "b: ", b)
		#b = 1
		if b!= 1 and b != (p-1):
			j=1
			while (j < ans[0] and b != p-1):
				b = sqm3(b, 2, p)
				if b==1 :
					return 0
				j = j + 1
			if b != (p-1):
				return 0

	return 1



print(miller_rabim(21, 30))