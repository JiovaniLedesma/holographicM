import numpy as np

def m_mult(*matrices):
    """
    Calculates the matrix resulting from a series of matrix multiplications
    """
    
    f,_ = ( matrices[0] ).shape
    A = np.eye(f)
    for matriz in matrices:
        A = np.dot(A, matriz)
    return A