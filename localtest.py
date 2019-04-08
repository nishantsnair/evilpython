_l=dir()
def _lox():
	print("---")
	for k in _l:
		if k[0] != '_':
			print(f"{k}: {_l[k]}")
	print("---")

x = 5
y = 2

_l=vars()
_lox()
