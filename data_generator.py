import numpy as np

def transpose(matrix):
    return np.transpose( matrix )

def array_to_matrix(arr):
    matrix = []
    i = 0
    while i < len( arr ):
        x = mat[i:i + 3]
        matrix.append( x )
        i += 3
    return matrix

def generate_data_as_array(size, length):
    matrix = np.random.rand(size, 3) * 10
    k = 100
    for i in range(1, length):
        matrix = np.concatenate((matrix, np.random.rand(size, 3 ) * k), axis=0)
        matrix = np.concatenate((matrix, np.random.rand(size, 3) * -1 * k), axis=0 )
        k *= 10
    mat = matrix.flatten()
    np.random.shuffle( mat )
    return mat

if __name__ == "__main__":
    size = 100000
    length = 5
    mat = generate_data_as_array(size, length)
    matrix = array_to_matrix( mat )
    matrix = np.array( matrix, dtype=int )
    X = []
    Y = []
    for coefs in matrix:
        a = coefs[0]
        b = coefs[1]
        c = coefs[2]
        d = b ** 2 - 4 * a * c
        if d < 0:
            y = 0
        elif d == 0:
            y = 1
        else:
            y = 2
        X.append(coefs)
        Y.append(y)
    np.save('X.npy', X)
    np.save('Y.npy', Y)