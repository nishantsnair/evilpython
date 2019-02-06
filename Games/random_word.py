from random import choice
import pynput
vows = 'aeiou' #97 through 122
cons = [chr(i) for i in range(97,123) if chr(i) not in vows]
print(f"{choice(cons)}{choice(vows)}{choice(cons)}{choice(vows)}")

c = pynput.keyboard.Controller()
c.type("python randomword.py")
