def maximum_element(list_of_integers):
	#LOWERCASE
	a = 0
	b = 0
	c = 0
	d = 0
	e = len(list_of_integers)
	f = len(list_of_integers)
	g = len(list_of_integers)
	h = len(list_of_integers)
	i = 0
	j = len(list_of_integers)
	k = len(list_of_integers)
	l = 0
	p = 0
	#CAPITALS
	A = list_of_integers[0]

	while a < len(list_of_integers):
		a = a + 1
		b = e - f
		f = f - 1
		z = list_of_integers[b]
		if z > d:
			d = z
	# f = f - 1
	if d > 0:
				while l < len(list_of_integers):
					n = g - h
					o = list_of_integers[n]
					if o > p:
						p = o
						h = h - 1
					else:
						o = p
						h = h - 1
					l = l + 1

				return o

	else:
				while p < len(list_of_integers):
					q = j - k
					r = list_of_integers[q]
					if A > r:
						r = A
						k = k - 1
					else:
						A = r
						k = k - 1

					p = p + 1



				return r

B = [-5,-10,-2,-3,0,-5,-6,-9]
y = maximum_element(B)
print(y)
