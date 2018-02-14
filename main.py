import argparse
import cv2
import edgedot

parser = argparse.ArgumentParser(description='photo lowpoly style transform tool.')
parser.add_argument('--image', type=str)
args = parser.parse_args()

img = cv2.imread(args.image, 3)
img = cv2.GaussianBlur(img, (3, 3), 0)

dx = cv2.convertScaleAbs(cv2.Sobel(img, cv2.CV_16S, 1, 0))
dy = cv2.convertScaleAbs(cv2.Sobel(img, cv2.CV_16S, 0, 1))

edge = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)[:,:, 2]

dots = edgedot.edgedot(edge, 4000)
cv2.imshow('image(o)', img)
lowpoly = edgedot.lowploy(img, dots)
lowpoly = cv2.GaussianBlur(lowpoly, (3, 3), 0)
cv2.imshow('image', lowpoly)

cv2.waitKey(0)
cv2.destroyAllWindows()