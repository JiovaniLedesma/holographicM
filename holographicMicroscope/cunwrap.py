import numpy as np
import math as m

def cunwrap(Psi, options):
	a = Psi.shape
	if len(a) > 2:
		print('CUNWRAP: input Psi must be 2D-array')
	else:
		ny, nx = Psi.shape[0], Psi.shape[1]

		if nx < 2 || ny < 2:
			print('CUNWRAP: size of Psi must be langer than 2')
		else:
			if 'roundk' in options:
				roundk = false
			if 'verbose' in options:
				verbose = true

			w1 = np.ones((ny, 1))
			w1[0], w1[-1] = 0.5, 0.5
			w2 = np.ones((1, nx))
			w2[0], w2[-1] = 0.5, 0,5
			weight = w1*w2
			if 'weight' in options:
				weight = weight
			if 'maxblocksize' in options:
				blocksize = 125

			if 'overlap' in options:
				p = 0.25
				p = max(min(p,1),0)

def splitidx(blocksize, n, p):
	if blocksize >= n:
		ilist = [1, n]
		blocksize = n
	else:
		q = 1-p
		# Number of blocks
		k = (n/blocksize-p)/q
		k = np.ceil(k)

		# Readjust the block size, float
		blocksize = n/((k*q) + p)

		# first index
		firstidx = np.round(np.linspace(1, n - np.ceil(blocksize)+1, k))
		lastidx = np.round(firstidx+blocksize-1)
		lastidx[-1] = n

		# Make sure they are overlapped
		lastidx[0:-1] = max(lastidx[0:-1], firstidx[1:])

		# Put the indexes of k blocks into cell array
		ilist = np.ceil(1, len(firstidx))
		for k in range(0,len(ilist)):
			ilist[k] = firstidx[k]:lastidx[k]

		blocksize = np.round(blocksize)

	return ilist, blocksize

def mydisplay(verbose, arg):
	if verbose == "verbose":
		print(arg)
		