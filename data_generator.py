import numpy as np

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

def count_minus(coefs):
    count = 0
    for coef in coefs:
        if coef < 0:
            count+=1
    return count

def generate_more_doublesol():
    # we have delta = b**2 - 4*a*c, this means if we want to generate double solution coefs, delta = 0
    # ====> b = 2 * sqrt(a*c), ===> we just need to generate random a's (or c's) to get b's, thus b = 2a or b = 2c given that a = c
    mat = []
    for a in range(10000):
        b = 2 * a
        c = a
        vec1 = [a, b, c]
        vec2 = [-1*a, b, -1*c]
        #d1 = b ** 2 - 4 * a * c
        #d2 = b ** 2 - 4 * (-1*a) * (-1*c)
        mat.append(vec1)
        mat.append(vec2)
    return mat

if __name__ == "__main__":
    size = 100000
    length = 4
    mat = generate_data_as_array(size, length)
    matrix = array_to_matrix( mat )
    matrix = np.array( matrix, dtype=int )

    mat_double_sol = np.array( generate_more_doublesol() )

    matrix = np.concatenate((matrix, mat_double_sol), axis=0)
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
        arr = [i for i in coefs]
        for i in coefs:
            if i<0:
                arr.append(0)
            else:
                arr.append(1)
        arr.append( count_minus( coefs ) ) # negatives
        arr.append( 3 - count_minus( coefs ) ) # positives
        X.append(arr)
        Y.append(y)
    np.save('X_additional_position_doublesol.npy', X)
    np.save('Y_additional_position_doublesol.npy', Y)
