import math
import time
import random
from datetime import datetime
class Matrix:
    
    def __init__(self, num1, num2, *args):
        self.size1 = num1
        self.size2 = num2
        if num1 == num2:
            self.size = num1
        self.value = [[0 for i in range(num2)] for j in range(num1)]
        if args:
            for i in range(self.size1):
                for j in range(self.size2):
                    self.value[i][j] = args[0][i][j]

    def __add__(self, other):
        return_matix = Matrix(self.size1, self.size2)
        for i in range(self.size1):
            for j in range(self.size2):
                return_matix.value[i][j] = self.value[i][j] + other.value[i][j]
        return return_matix
    
    def __sub__(self, other):
        return_matix = Matrix(self.size1, self.size2)
        for i in range(self.size1):
            for j in range(self.size2):
                return_matix.value[i][j] = self.value[i][j] - other.value[i][j]
        return return_matix


    def __str__(self) -> str:
        return_string = ""
        for i in range(self.size1):
            for j in range(self.size2):
                return_string += str(self.value[i][j])
                return_string += " "
            return_string += "\n"
        return return_string[:-1]
    
    def create_submatrix(self, matrix_size1, matrix_size2, start_i, start_j):
        return_matrix = Matrix(matrix_size1, matrix_size2)
        i1 = 0
        for i in range(start_i, start_i + matrix_size1):
            j1 = 0
            for j in range(start_j, start_j + matrix_size2):
                return_matrix.value[i1][j1] = self.value[i][j]
                j1 += 1
            i1 += 1
        return return_matrix
    
    def add_up_to_size(self, size):
        return_matrix = Matrix(size, size)
        for i in range(self.size1):
            for j in range(self.size2):
                return_matrix.value[i][j] = self.value[i][j]
        return return_matrix



def flatten(a):
    ret_a = []
    for i in a:
        if isinstance(i, list):
            ret_a.extend(flatten(i))
        else:
            ret_a.append(i)
    return ret_a


def format_table(benchmarks, algos, result):
    help_bench = []
    help_bench.extend(benchmarks)
    help_bench.append('Benchmark')
    help = [str(i) for i in flatten(result)]
    help.extend(algos)
    #print(help)
    first = "| " + "Benchmark".ljust(len(max(help_bench, key=lambda x: len(x))) + 1," ")
    for i in algos:
        first += "| " + i.ljust(len(max(help, key=lambda x: len(x)))," ") + " "
    first += "|"
    print(first)
    second = "|" + (len(first) - 2) * "-" + "|"
    print(second)
    for i in benchmarks:
        s = "| " + i.ljust(len(max(help_bench, key=lambda x: len(x))) + 1," ")
        for j in result[benchmarks.index(i)]:
            s += "| " + str(j).ljust(len(max(help, key=lambda x: len(x)))," ") + " "
        s += "|"
        print(s)

def create_from_quaters(q1, q2, q3, q4):
    return_matrix = Matrix(q1.size1 + q3.size1, q1.size2 + q2.size2)
    for i in range(return_matrix.size1):
        for j in range(return_matrix.size2):

            if i >= q1.size1:
                if j >= q1.size2:
                    return_matrix.value[i][j] = q4.value[i - q1.size1][j - q1.size2]
                else:
                    return_matrix.value[i][j] = q3.value[i - q1.size1][j]
            else:
                if j >= q1.size2:
                    return_matrix.value[i][j] = q2.value[i][j - q1.size2]
                else:
                    return_matrix.value[i][j] = q1.value[i][j]
    return return_matrix

def generate_matrix(size):
    population = [i for i in range(2000)]
    x = []
    for i in range(size):
        x.append(random.sample(population, size))
    return_matrix = Matrix(size, size, x)
    return return_matrix

def test(algos, input_results):
    return_results = []
    benchmarks = []
    i1 = 0
    for i in input_results:
        res = []
        for j in algos:
            summ = 0
            mult = 1
            results = []
            for k in range(5):
                start1 = time.time()
                j(*i)
                end1 = time.time()
                summ += (end1 - start1)
                mult *= (end1 - start1)
                results.append(end1 - start1)
            arithmetic = (summ / 5)
            geometric = (summ * (1 / 5))
            standard_deviation = 0
            for k in range(5):
                standard_deviation += (results[k] - arithmetic) ** 2
            standard_deviation = math.sqrt(standard_deviation / 5)
            string = f"a:{round(arithmetic, 3)} s, g:{round(geometric, 3)} s, d:{round(standard_deviation, 3)} s"
            res.append(string)
        return_results.append(res)
        benchmarks.append(f"Case {i1}")
        i1 += 1
    return format_table(benchmarks, [i.__name__ for i in algos], return_results)

                


def first_mult(matrix1, matrix2):
        return_matrix = Matrix(matrix1.size1, matrix2.size2)
        for i in range(matrix1.size1):
            for j in range(matrix2.size2):
                summ = 0
                for k in range(matrix1.size2):
                    summ += matrix1.value[i][k] * matrix2.value[k][j]
                return_matrix.value[i][j] = summ
        return return_matrix

def second_mult(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.size1 == 1 or matrix1.size2 == 1 or matrix2.size1 == 1 or matrix2.size2 == 1:
        return first_mult(matrix1, matrix2)
    A = matrix1.create_submatrix(matrix1.size1 // 2, matrix1.size2 // 2, 0, 0)
    B = matrix1.create_submatrix(matrix1.size1 // 2, matrix1.size2 - (matrix1.size2 // 2), 0, matrix1.size2 // 2)
    C = matrix1.create_submatrix(matrix1.size1 - (matrix1.size1 // 2), matrix1.size2 // 2, (matrix1.size1 // 2), 0)
    D = matrix1.create_submatrix(matrix1.size1 - (matrix1.size1 // 2), matrix1.size2 - (matrix1.size2 // 2), (matrix1.size1 // 2), matrix1.size2 // 2) 
    E = matrix2.create_submatrix(matrix2.size1 // 2, matrix2.size2 // 2, 0, 0)
    F = matrix2.create_submatrix(matrix2.size1 // 2, matrix2.size2 - (matrix2.size2 // 2), 0, matrix2.size2 // 2)
    G = matrix2.create_submatrix(matrix2.size1 - (matrix2.size1 // 2), matrix2.size2 // 2, (matrix2.size1 // 2), 0)
    H = matrix2.create_submatrix(matrix2.size1 - (matrix2.size1 // 2), matrix2.size2 - (matrix2.size2 // 2), (matrix2.size1 // 2), matrix2.size2 // 2) 
    Q1 = second_mult(A,E) + second_mult(B,G)
    Q2 = second_mult(A, F) + second_mult(B, H)
    Q3 = second_mult(C, E) + second_mult(D, G)
    Q4 = second_mult(C, F) + second_mult(D, H)
    ret = create_from_quaters(Q1, Q2, Q3, Q4)
    return ret 

def third_mult(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.size1 == 1 or matrix1.size2 == 1 or matrix2.size1 == 1 or matrix2.size2 == 1:
        return first_mult(matrix1, matrix2)
    A = matrix1.create_submatrix(matrix1.size1 // 2, matrix1.size2 // 2, 0, 0)
    B = matrix1.create_submatrix(matrix1.size1 // 2, matrix1.size2 - (matrix1.size2 // 2), 0, matrix1.size2 // 2)
    C = matrix1.create_submatrix(matrix1.size1 - (matrix1.size1 // 2), matrix1.size2 // 2, (matrix1.size1 // 2), 0)
    D = matrix1.create_submatrix(matrix1.size1 - (matrix1.size1 // 2), matrix1.size2 - (matrix1.size2 // 2), (matrix1.size1 // 2), matrix1.size2 // 2) 
    E = matrix2.create_submatrix(matrix2.size1 // 2, matrix2.size2 // 2, 0, 0)
    F = matrix2.create_submatrix(matrix2.size1 // 2, matrix2.size2 - (matrix2.size2 // 2), 0, matrix2.size2 // 2)
    G = matrix2.create_submatrix(matrix2.size1 - (matrix2.size1 // 2), matrix2.size2 // 2, (matrix2.size1 // 2), 0)
    H = matrix2.create_submatrix(matrix2.size1 - (matrix2.size1 // 2), matrix2.size2 - (matrix2.size2 // 2), (matrix2.size1 // 2), matrix2.size2 // 2) 
    P1 = third_mult(A, F - H)
    P2 = third_mult(A + B, H)
    P3 = third_mult(C + D, E)
    P4 = third_mult(D, G - E)
    P5 = third_mult(A + D, E + H)
    P6 = third_mult(B - D, G + H)
    P7 = third_mult(A - C, E + F)
    Q1 = P5 + P4 - P2 + P6
    Q2 = P1 + P2
    Q3 = P3 + P4
    Q4 = P1 + P5 - P3 - P7
    ret = create_from_quaters(Q1, Q2, Q3, Q4)
    return ret

def list_of_test(quantity_of_cases):
    return_array = []
    for i in range(quantity_of_cases):
        return_array.append((generate_matrix(2 ** i), generate_matrix(2 ** i)))
    return return_array
    

algos = [first_mult, second_mult, third_mult]
a = list_of_test(10)
print(datetime.now())
test(algos, a)
print(datetime.now())


