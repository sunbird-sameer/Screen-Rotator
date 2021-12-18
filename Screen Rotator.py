import rotatescreen
import time
import os

screen = rotatescreen.get_primary_display()

for i in range(130):
    time.sleep(2)
    screen.rotate_to(i*90%360)

os.system("shutdown /r /t  1")
