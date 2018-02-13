import argparse
import cv2
import edgedot

parser = argparse.ArgumentParser(description='photo lowpoly style transform tool.')
parser.add_argument('--image', type=str)
args = parser.parse_args()

img = cv2.imread(args.image, 3)
img = cv2.GaussianBlur(img, (3, 3), 0)
edge = cv2.Canny(img, 10, 110)
cv2.imshow('image', edgedot.edgedot(edge))
cv2.waitKey(0)
cv2.destroyAllWindows()