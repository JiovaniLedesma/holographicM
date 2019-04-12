#***********************************************************
# 			PRUEBAS DE VISIÓN
#***********************************************************

from cv2 import *
import numpy as np

I = imread("robot.jpg")
Ig = cvtColor(I, COLOR_BGR2GRAY)
Ig = np.uint8(Ig)
M,N = Ig.shape[0], Ig.shape[1]
Copy = np.zeros((M, N))

for i in range(0, M):
	for j in range(0, N):
		Copy[i,j] = Ig[i,j]

Copy = np.uint8(Copy)
m,n = Copy.shape[0], Copy.shape[1]

print("Tamaño de la imagen original:")
print(M, N)
print("Tamaño de la copia imagen:")
print(m, n)

img1 = imshow("my image Original", Ig)
destroyWindow(img1)
imshow("my image Copy", Copy)
waitKey()

#***********************************************************

# import numpy as np
# # import numpy.fft.fft2 as fft2
# # import numpy.fft.fftshift as fftshift

# A = np.mgrid[:5, :5][0]
# # A = np.array([[5], [5]])
# X = np.fft.fft2(A)
# print(X)