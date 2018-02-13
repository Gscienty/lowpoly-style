import cv2
import math
import random
import numpy as np

def edgedot(edge, count = 1000):
    dots = np.zeros(edge.shape)
    notzeros = np.where(edge != 0)
    size = len(notzeros[0])
    for i in range(count):
        position = math.floor(random.random() * size)
        while dots[notzeros[0][position], notzeros[1][position]] == 255:
            position = math.floor(random.random() * size)
        dots[notzeros[0][position], notzeros[1][position]] = 255
    return dots