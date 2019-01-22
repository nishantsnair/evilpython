from pynput import keyboard

c = keyboard.Controller()
keys = keyboard.Key

c.type("x = 5")

c.press(keys.enter)
c.release(keys.enter)

print("The value of x is {}".format(x))
