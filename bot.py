import numpy as np
from PIL import Image, ImageGrab
from win32api import GetSystemMetrics
from keyboard import press_and_release

x, y = GetSystemMetrics(0),GetSystemMetrics(1)
while True:
	img = np.array(ImageGrab.grab(bbox=(x//2, y-171, x//2+2, y-170)))
	color = Image.fromarray(img).convert('RGB').getcolors()

	if (2, (26, 141, 199)) in color:
		press_and_release('z')
		print('blue')
	if (2, (237, 121, 12)) in color:
		press_and_release('x')
		print('orange')
	if (2, (199, 43, 22)) in color:
		press_and_release('c')
		print('red')
