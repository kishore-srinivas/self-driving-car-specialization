import cv2
import numpy as np

og = cv2.imread('C:\\Users\\kisho\\Documents\\git\\projects\\image-processing\\images\\line.jpg')
im = cv2.cvtColor(og, cv2.COLOR_BGR2GRAY)
# cv2.imshow('im', im)

dst = cv2.cornerHarris(im, 2, 3, 0.04)
# cv2.imshow('kp', dst)

dst_norm = np.empty(dst.shape, dtype=np.float32)
cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
print(dst_norm_scaled.shape)
# print(np.max(dst_norm_scaled), np.where(dst_norm_scaled == np.max(dst_norm_scaled)))
# print(np.min(dst_norm_scaled), np.where(dst_norm_scaled == np.min(dst_norm_scaled)))

threshold = 195
feats = np.zeros_like(im)
kp = []
points = np.where(dst_norm_scaled > threshold)
for i in range(len(points[0])):
    kp.append(cv2.KeyPoint(points[1][i], points[0][i], 5))
cv2.imshow('feats', cv2.drawKeypoints(im, kp, None))

arr = np.linspace(0, 10, 12).reshape(4, 3)
points = np.where(arr > 5)
for i in range(len(points[0])):
    arr[points[0][i], points[1][i]] = 100
print(arr)

cv2.waitKey()