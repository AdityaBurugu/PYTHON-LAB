def shape(matrix):
    row = col = 0
    if matrix is not None:
        row = len(matrix)
        col = len(matrix[0])
    return [row,col]

def Zero_Matrix(size):
    result = []
    z = []
    for row in range(size[0]):
        for col in range(size[1]):
            z.append(0)
        result.append(z)
        z=[]
    return result

def Create_Matrix(size):
    matrix = Zero_Matrix(size)
    for row in range(size[0]):
        for col in range(size[1]):
            try:
                value = int(input(f"Enter {row} row {col} column element: "))
                matrix[row][col] = value
            except ValueError:
                matrix[row][col] = 0
                print("Invalid input! Please enter a valid integer.")
                return None
    return matrix

def Print_Matrix(matrix):
    try:
        for row in matrix:
            for ele in row:
                print(ele, end="\t")
            print()
    except:
        print(None)

def Matrix_Add(matrix_1,matrix_2):
    try:
        size = shape(matrix_1)
        result = Zero_Matrix(size)
        for row in range(size[0]):
            for col in range(size[1]):
                result[row][col] = matrix_1[row][col] + matrix_2[row][col]
        return result
    except ValueError:
        return None

def Matrix_Subtract(matrix_1,matrix_2):
    try:
        size = shape(matrix_1)
        result = Zero_Matrix(size)
        for row in range(size[0]):
            for col in range(size[1]):
                result[row][col] = matrix_1[row][col] - matrix_2[row][col]
        return result
    except ValueError:
        return None

def Matrix_Product(matrix_1,matrix_2):
    try:
        matrix_1_size = shape(matrix_1)
        matrix_2_size = shape(matrix_2)
        size = [matrix_1_size[0],matrix_2_size[1]]
        result = Zero_Matrix(size)
        sum=0
        for row in range(matrix_1_size[0]):
            for col in range(matrix_2_size[1]):
                for row2 in range(matrix_2_size[0]):
                    sum = sum + matrix_1[row][row2] * matrix_2[row2][col]
                result[row][col] = sum
                sum = 0
        return result
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None
def Matrix_Divide(matrix_1,matrix_2):
    try:
        size = shape(matrix_1)
        result = Zero_Matrix(size)
        for row in range(size[0]):
            for col in range(size[1]):
                result[row][col] = matrix_1[row][col] / matrix_2[row][col]
        return result
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None

def Matrix_Transpose(matrix):
    try:
        size=shape(matrix)[::-1]
        result = Zero_Matrix(size)
        for row in range(size[1]):
            for col in range(size[0]):
                result[col][row]=matrix[row][col]
        return result
    except:
        return None

def Matrix_Symmetry_Check(matrix):
    try:
        size = shape(matrix)
        if size[0] == size[1]:
            for row in range(size[0]):
                for col in range(size[1]):
                    if (matrix[row][col] == matrix[col][row]):
                        pass
                    else:
                        return False
            return True
        return False
    except:
        return None

def Matrix_Creation_Validity(row,col):
    if row<1 or col<1:
        return False
    return True
def Matrix_ASD_Validity(matrix1,matrix2):
    try:
        if shape(matrix1) == shape(matrix2):
            return True
        return False
    except:
        return False

def Matrix_Multiplication_Validity(matrix1,matrix2):
    try:
        matrix1_size = shape(matrix1)
        matrix2_size = shape(matrix2)
        if matrix1_size[1] == matrix2_size[0]:
            return True
        return False
    except:
        return False


if __name__ == '__main__':
    s = diff = p = d = t = matrix_1 = matrix_2 = matrix_3 = matrix_4 = None

    print("*"*100)

    try:
        row,col = map(int,input("Enter Size of Matrix 1: ").split())
    except ValueError:
        row=col=0
        print("Invalid input! Please enter a valid integer.")

    if Matrix_Creation_Validity(row,col):
        print("Enter the elements of Matrix 1")
        matrix_1 = Create_Matrix(size=[row,col])  #2x3 Matrix

    try:
        row, col = map(int, input("Enter Size of Matrix 2: ").split())
    except ValueError:
        row = col = 0
        print("Invalid input! Please enter a valid integer.")

    if Matrix_Creation_Validity(row,col):
        print("Enter the elements of Matrix 2")
        matrix_2 = Create_Matrix(size=[row,col])  #2x3 Matrix

    print("*"*100)

    print("Elements of Matrix 1")
    shape(matrix_1)
    Print_Matrix(matrix_1)

    print("Elements of Matrix 2")
    Print_Matrix(matrix_2)

    print("*"*100)

    try:
        row, col = map(int, input("Enter Size of Matrix 3: ").split())
    except ValueError:
        row = col = 0
        print("Invalid input! Please enter a valid integer.")

    if Matrix_Creation_Validity(row,col):
        print("Enter the elements of Matrix 3")
        matrix_3 = Create_Matrix([row,col])  #3x2 Matrix

    try:
        row, col = map(int, input("Enter Size of Matrix 4: ").split())
    except ValueError:
        row = col = 0
        print("Invalid input! Please enter a valid integer.")

    if Matrix_Creation_Validity(row,col):
        print("Enter the elements of Matrix 4")
        matrix_4 = Create_Matrix([row,col])    #2x3 Matrix

    print("*"*100)

    print("Elements of Matrix 3")
    Print_Matrix(matrix_3)

    print("Elements of Matrix 4")
    Print_Matrix(matrix_4)

    print("*"*100)

    if matrix_1 is not None:
        print("Matrix 1 Size:",shape(matrix_1))
    if matrix_2 is not None:
        print("Matrix 2 Size:",shape(matrix_2))
    if matrix_3 is not None:
        print("Matrix 3 Size:",shape(matrix_3))
    if matrix_4 is not None:
        print("Matrix 4 Size:",shape(matrix_4))

    if Matrix_ASD_Validity(matrix_1,matrix_2):
        s = Matrix_Add(matrix_1, matrix_2)
        diff = Matrix_Subtract(matrix_1, matrix_2)
        d = Matrix_Divide(matrix_1,matrix_2)
    if Matrix_Multiplication_Validity(matrix_3,matrix_4):
        p = Matrix_Product(matrix_3,matrix_4)

    try:
        t = Matrix_Transpose(matrix_1)
    except:
        pass

    print("*"*100)

    print("Addition of two Matrices [Matrix1 + Matrix2]")
    Print_Matrix(s)

    print("Subtraction of two Matrices [Matrix1 - Matrix2]")
    Print_Matrix(diff)

    print("Product of two Matrices [Matrix3 * Matrix4]")
    Print_Matrix(p)

    print("Divide of two Matrices [Matrix1 / Matrix2]")
    Print_Matrix(d)

    print("Transpose of a Matrix [Matrix1]")
    Print_Matrix(t)

    print("[Matrix1] Symmetry Check:",Matrix_Symmetry_Check(matrix_1))

    print("*"*100)