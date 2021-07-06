import numpy as np
from PIL import Image, ImageGrab
from win32api import GetSystemMetrics
from keyboard import press_and_release

while True:
	x, y = GetSystemMetrics(0),GetSystemMetrics(1)
	img = np.array(ImageGrab.grab(bbox=(x//2-1, y-171, x//2+1, y-170)))
	color = Image.fromarray(img).convert('RGB').getcolors()

	if (2, (26, 141, 199)) in color:
		print('blue')
		press_and_release('z')
	if (2, (237, 121, 12)) in color:
		print('orange')
		press_and_release('x')
	if (2, (199, 43, 22)) in color:
		print('red')
		press_and_release('c')
