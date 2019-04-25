import cv2
import numpy as np

from rpc_client import RpcClient

img = cv2.imread('joey.jpg')
client = RpcClient()
pred = client(img)

