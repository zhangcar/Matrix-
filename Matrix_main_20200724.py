#    This is the correct solution
#    x, y = map(float, input().split(' '))
my_matrix1 = []
my_matrix2 = []
my_matrix_result = []
m1 = 0
n1 = 0
m2 = 0
n2 = 0

def print_matrix(matrix, m, n):
    print("The result is:")
    for i in range(m):
        for j in range(n):
            print(round(matrix[i][j],3), end=" ")
        print()
    print()

def input_matrix(name_):
    result_ = []
    print("Enter size of",name_,"matrix:")
    input_ = input()
    input_Split = input_.split()
    m = int(input_Split[0])
    n = int(input_Split[1])
    print("Enter",name_,"matrix:")
    for i in range(m):
        temp_ = input()
        temp_Split = temp_.split()
        result_.append(temp_Split)

    AA = zeros_matrix(m,n)

    for i in range(m):
        for j in range(n):
            AA[i][j] = eval(result_[i][j])
    return AA, m, n

def matrix_t_constant(matrix,m,n,con_):
    result_ = []
    for i in range(m):
        temp_ = []
        for j in range(n):
            temp_.append(matrix[i][j] * con_)
        result_.append(temp_)
    return result_

def matrix_c_product(matrix1, matrix2, m, n, l):
    result_ = []
    for i in range(m):
        line_vector = []
        for k in range(l):
            temp_ = 0
            for j in range(n):
                temp_ += matrix1[i][j] * matrix2[j][k]
            line_vector.append(temp_)
        result_.append(line_vector)
    return result_

def print_manual():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

def print_trans_manual():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

def add_matrix(matrix1, matrix2, m, n):
    result_ = matrix1
    for i in range(m):
        for j in range(n):
            result_[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_

def main_diagonal():

    [my_matrix1, m1, n1] = input_matrix("")

    result_t = [[my_matrix1[j][i] for j in range(len(my_matrix1))] for i in range(len(my_matrix1[0]))]

    print_matrix(result_t, n1, m1)

def side_diagonal():

    [matrix, m1, n1] = input_matrix("")
    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            matrix[i][j], matrix[len(matrix)-1-j][len(matrix)-1-i] = matrix[len(matrix)-1-j][len(matrix)-1-i], matrix[i][j]

    print_matrix(matrix, n1, m1)

def vertical_line():

    [matrix, m1, n1] = input_matrix("")
    if n1 % 2 == 1:
        n_ = int((n1 - 1) /2)
    else:
        n_ = int(n1 / 2)

    for i in range(m1):
        for j in range(n_):
            matrix[i][j], matrix[i][n1 - 1 - j] = matrix[i][n1 - 1 - j], matrix[i][j]


    print_matrix(matrix, m1, n1)

def hori_line():
    [matrix, m1, n1] = input_matrix("")
    if m1 % 2 == 1:
        m_ = int((m1 - 1) /2)
    else:
        m_ = int(m1 / 2)

    for i in range(m_):
        for j in range(n1):
            matrix[i][j], matrix[m1 - 1 - i][j] = matrix[m1 - 1 - i][j], matrix[i][j]

    print_matrix(matrix, m1, n1)

def det_matrix(A1):
    det_value = 0
    m = len(A1)

    if m == 1:
        return A1[0][0]
    elif m == 2:
        return A1[0][0] * A1[1][1] - A1[0][1] * A1[1][0]

    for j in range(m):
        A2 = A1[1:]
        for i in range(m-1):
            A2[i] = A2[i][0:j] + A2[i][j+1:]

        k = (-1) ** (j % 2)
        sub_det = det_matrix(A2)
        det_value += k * A1[0][j] * sub_det
    return det_value

def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A
def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]
    return MC

def rev_matrix(A):
    I= copy_matrix(A)
    # Section 2: Make copies of A & I, AM & IM, to use for row ops
    n = len(A)
    for i in range(n):
        for j in range(n):
            I[i][j] = 0
            if i == j:
                I[i][j] = 1

    AM = copy_matrix(A)
    IM = copy_matrix(I)

    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] = fdScaler * AM[fd][j]
            IM[fd][j] = fdScaler * IM[fd][j]
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]:
            # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n):
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM

while True:
    print_manual()
    choice_ = int(input("Your choice:"))
    if choice_ == 1:
        [my_matrix1, m1, n1] = input_matrix("first")
        [my_matrix2, m2, n2] = input_matrix("second")
        if m1 == m2 and n1 == n2:
            my_matrix_result = add_matrix(my_matrix1, my_matrix2,m1,n1)
            print_matrix(my_matrix_result,m1,n1)
        else:
            print("The operation cannot be performed.")
    elif choice_ == 2:
        [my_matrix1, m1, n1] = input_matrix("")
        cons = float(input("Enter constant:"))
        my_matrix_result = matrix_t_constant(my_matrix1,m1,n1,cons)
        print_matrix(my_matrix_result,m1,n1)
    elif choice_ == 3:
        [my_matrix1, m1, n1] = input_matrix("first")
        [my_matrix2, m2, n2] = input_matrix("second")
        if n1 == m2:
            my_matrix_result = matrix_c_product(my_matrix1,my_matrix2, m1, n1, n2)
            print_matrix(my_matrix_result,m1,n2)
        else:
            print("The operation cannot be performed.")
    elif choice_ == 4:
        print_trans_manual()
        choice_1 = int(input("Your choice:"))
        if choice_1 == 1:
            main_diagonal()
        elif choice_1 == 2:
            side_diagonal()
        elif choice_1 == 3:
            vertical_line()
        elif choice_1 == 4:
            hori_line()
    elif choice_ == 5:
        [my_matrix1, m1, n1] = input_matrix("")
        print(det_matrix(my_matrix1))
        print()
    elif choice_ == 6:
        [my_matrix1, m1, n1] = input_matrix("")
        det_A = det_matrix(my_matrix1)
        if det_A == 0:
            print("This matrix doesn't have an inverse")
            print()
            continue
        else:
            my_matrix2 = rev_matrix(my_matrix1)
            print_matrix(my_matrix2,m1,m1)
            
    elif choice_ == 0:
        break
