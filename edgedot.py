import cv2
import math
import random
import numpy as np
import scipy.spatial
from PIL import Image, ImageDraw

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

def lowploy(colors, dots):
    shape = dots.shape
    canvas = Image.new('RGB', (shape[1], shape[0]), 0xFFFFFF)
    lowpoly_drow = ImageDraw.Draw(canvas)
    positions = np.where(dots > 0)
    use_to_delaunary = []
    for i in range(len(positions[0])):
        use_to_delaunary.append((positions[1][i], positions[0][i]))
    tris = scipy.spatial.Delaunay(use_to_delaunary).simplices.copy()
    for t in tris:
        a = use_to_delaunary[t[0]]
        b = use_to_delaunary[t[1]]
        c = use_to_delaunary[t[2]]

        mid = (np.array(a) + np.array(b) + np.array(c)) // 3
        color = colors[mid[1], mid[0]]
        lowpoly_drow.polygon([a, b, c], fill=(color[0], color[1], color[2]))
    return np.array(canvas)
        