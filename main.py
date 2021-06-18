from rpi_temp import rpi_temp
from pylepton import Lepton
import numpy as np
import cv2

with Lepton() as l:
    data,_ = l.capture()

point = (0,0)
thermal_image,temp_str = rpi_temp(data,point=point,palette_switch=True)

print("Temperature at {} is {}".format(point,temp_str))
cv2.imwrite("thermal_img.png",thermal_image)
