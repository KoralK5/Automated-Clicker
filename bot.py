import numpy as np
from os import system
from PIL import Image, ImageGrab
from win32api import GetSystemMetrics
from keyboard import press_and_release

x, y = GetSystemMetrics(0), GetSystemMetrics(1)
b, o, r = 0, 0, 0
prev = ('', 1)
change = False
while True:
	color = Image.fromarray(np.array(ImageGrab.grab(bbox=(x//2-1, y-171, x//2+1, y-170)))).getcolors()

	if (2, (26, 141, 199)) in color:
		press_and_release('z')
		b += 1
		prev = ('blue', prev[1]+1) if prev[0] == 'blue' else ('blue', 1)
		change = True
		
	elif (2, (237, 121, 12)) in color:
		press_and_release('x')
		o += 1
		prev = ('orange', prev[1]+1) if prev[0] == 'orange' else ('orange', 1)
		change = True

	elif (2, (199, 43, 22)) in color:
		press_and_release('c')
		r += 1
		prev = ('red', prev[1]+1) if prev[0] == 'red' else ('red', 1)
		change = True
	
	else: change = False

	if change:
		system('cls')
		print('STATS\n')
		print(f'{prev[0]} x{prev[1]}' if prev[1] != 1 else prev[0])
		print('\nred    :', r)
		print('blue   :', b)
		print('orange :', o)
