import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

N_POINTS = 10
TARGET_X_SLOPE = 2
TARGET_y_SLOPE = 3
TARGET_OFFSET  = 5
EXTENTS = 5
NOISE = 5

# [[ 0.81  0.9   0.73  0.52  0.96]
#  [ 0.93 -0.84  0.85 -1.34  2.26]
#  [ 2.47  1.96  2.79  3.47  1.94]]

# create random data
xs = [0.81, 0.9, 0.73, 0.52, 0.96]
ys = [0.93, -0.84,  0.85, -1.34,  2.26]
zs = [2.47,  1.96,  2.79,  3.47,  1.94]
# for i in range(N_POINTS):
#     zs.append(xs[i]*TARGET_X_SLOPE + \
#               ys[i]*TARGET_y_SLOPE + \
#               TARGET_OFFSET + np.random.normal(scale=NOISE))

# plot raw data
plt.figure()
ax = plt.subplot(111, projection='3d')
ax.scatter(xs, ys, zs, color='b')

# do fit
tmp_A = []
tmp_b = []
for i in range(len(xs)):
    tmp_A.append([xs[i], ys[i], zs[i]])
    tmp_b.append(1)
b = np.matrix(tmp_b).T
A = np.matrix(tmp_A)
fit = (A.T * A).I * A.T * b
errors = b - A * fit
residual = np.linalg.norm(errors)

print("solution:")
print("%f x + %f y + %f z = 1" % (fit[0], fit[1], fit[2]))
print("errors:")
print(errors)
print("residual:")
print(residual)

# plot plane
xlim = ax.get_xlim()
ylim = ax.get_ylim()
X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
                  np.arange(ylim[0], ylim[1]))
Z = np.zeros(X.shape)
# for r in range(X.shape[0]):
#     for c in range(X.shape[1]):
#         Z[r,c] = (1 - fit[0] * X[r,c] + fit[1] * Y[r,c]) / fit[2]
ax.plot_wireframe(X,Y,Z, color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()