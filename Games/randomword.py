from random import choice
vows = 'aeiou' #97 through 122
cons = [chr(i) for i in range(97,123) if chr(i) not in vows]
print(" ".join([f"{choice(cons).upper()}{choice(vows)}{choice(cons)}{choice(vows)}" for i in range(0,1000)]))


# import pynput
# c = pynput.keyboard.Controller()
# c.type("python randomword.py")











