from holographicMicroscope.mathematical_algorithms import *
from numpy import *
import numpy as np


def off_axis(image, lamda = 650e-9):
	I = double(image)
	r, c = 600, 600
	M, N = r, c
	deltapsi, deltanu = 5.2e-6, 5.2e-6
	Mag = 1
	deltapsi, deltanu = (5.2e-6)/Mag, (5.2e-6)/Mag
	k = (2*pi)/lamda
	z, ref = 0.0, 0
	ker = np.zeros((M, N))

	for m in range(0, M):
		for n in range(0, N):
			ker[m, n] = sqrt(1-(((lamda*(m-(M/2)))/(M*deltanu))**2)-(((lamda*(n-(N/2)))/(N*deltapsi))**2))

	Ho = ((np.fft.fftshift(np.fft.fft2(I)))) # Para usar dezplazamiento en espectro de frecuencias
	radio, despx, despy = 80, 474-(N/2), 287-(N/2)
	Mas = np.zeros((N, N))

	for r in range(0, N):
		for c in range(0, N):
			ra = sqrt((r-(N/2)-despy)**2+(c-(N/2)-despx)**2)
			if ra < radio:
				Mas[r,c] = 1

	Hog = Ho*Mas

	# numpy.roll = circshift
	Hog = np.roll(np.roll(Hog, 14, 1), (N/2)-476,2) # Ajusta la aberración de tilt +13 en reng 

	return Hog, ker, lamda

def reconstruction(Hog, ker, lamda):
	z = 0.0
	# Python maneja los números imaginarios con " j "
	OBJr = (((Hog)*np.exp((1j*2*np.pi*z*ker)/lamda)))
	objectrecr = ((np.fft.ifft2(np.fft.ifftshift(OBJr))))
	intr = np.absolute(objectrecr)
	phar = np.angle(objectrecr)
	ref = 10

	return intr, phar, ref

def slider(valor_slider, Hog, ker, lamda):
	z = valor_slider
	OBJ = (((Hog*np.exp((1j*2*pi*z*ker)/lamda))))
	objectrec = ((np.fft.ifft2(np.fft.ifftshift(OBJ))))
	int = np.absolute(objectrec)
	OBJ = (((Hog*np.exp((1j*2*pi*(z**2)*ker)/lamda))))


# data = np.array([[800],[950]])
# Ho,ker, lamda = off_axis(data)
# print(Ho)