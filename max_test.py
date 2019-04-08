def maximum_element(list_of_integers):


	i = len(list_of_integers)
	x = len(list_of_integers)
	a = 0
	z = list_of_integers[0]
	while a < len(list_of_integers):
		n = i - x
		b = list_of_integers[n]
		if b > z:
			z = b
		elif z > b:
			b = z
		x = x - 1

		a = a + 1

	return b

l = [-10,-0,-4,-5,-6,-9]
y = maximum_element(l)
print(y)
