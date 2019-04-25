import cv2
import numpy as np

img = cv2.imread('joey.jpg')
client = RpcClient()
pred = client(img)

