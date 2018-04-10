#!/usr/bin/env python3
import random


class MatrixException(Exception):
    """Класс для исключений класса Matrix."""

    pass


class Matrix:
    def __init__(self, *args):
        """Конструктор класса. Может принимать либо два числа - количество строк и столбцов,
        либо список строк матрицы.

        :param *args: Либо два числа, либо список.
        :type tuple.
        """

        if len(args) is 2 and all(filter(lambda x: int(x) is True, args)):
            self.rows = args[0]
            self.columns = args[1]
            self.matrix = []
            for i in range(self.rows):
                self.matrix.append([])
                for j in range(self.columns):
                    self.matrix[i].append(random.random())
        else:
            self.matrix = args[0]
            self.rows = len(args[0])
            self.columns = len(args[0][0])

    def __add__(self, other):
        """Сложение двух матриц. Возвращает матрицу, где элементы являются результатом сложения элементов
         из двух матриц, или бросает исключение, если ранги матриц не совпадают.

         :param self: Первая матрица.
         :type self: Matrix.
         :param other: Вторая матрица.
         :type other: Matrix.
         :rtype Matrix
         :raise MatrixException
         """

        if self.rows == other.rows and self.columns == other.columns:
            sum_matrix = []
            for i in range(self.rows):
                sum_row = [sum(item) for item in zip(self.matrix[i], other.matrix[i])]
                sum_matrix.append(sum_row)
            return Matrix(sum_matrix)
        else:
            raise MatrixException("This is impossible because of ranks mismatch!")

    def __sub__(self, other):
        """Вычитание матриц. Возвращает матрицу, где элементы являются результатом вычитания элементов
        одной матрицы из элементов другой, или бросает исключение, если ранги матриц не совпадают.

        :param self: Первая матрица, из которой вычитают вторую матрицу.
        :type self: Matrix.
        :param other: Вторая матрица, которую вычитают.
        :type other: Matrix.
        :rtype Matrix
        :raise MatrixException
        """

        if self.rows == other.rows and self.columns == other.columns:
            sub_matrix = []
            for i in range(self.rows):
                sub_row = [item[0] - item[1] for item in zip(self.matrix[i], other.matrix[i])]
                sub_matrix.append(sub_row)
            return Matrix(sub_matrix)
        else:
            raise MatrixException("This is impossible because of ranks mismatch!")

    def __mul__(self, other):
        """Умножение матриц. Бросает исключение, если количество столбцов
        первой матрицы не совпадает с количеством строк второй.

        :param self: Первая матрица.
        :type self: Matrix.
        :param other: Вторая матрица.
        :type other: Matrix.
        :rtype Matrix
        :raise MatrixException
        """

        if self.columns == other.rows:
            mul_matrix = Matrix(self.rows, other.columns)
            for i in range(mul_matrix.rows):
                for j in range(mul_matrix.columns):
                    mul_matrix.matrix[i][j] = sum(
                        [item[0] * item[1] for item in zip(self.matrix[i], other.transpose().matrix[j])])
            return mul_matrix
        else:
            raise MatrixException("Dimensions mismatch!")

    def __eq__(self, other):
        """Проверяет равнство двух матриц.

        :param self: Первая матрица.
        :type self: Matrix.
        :param other: Вторая матрица.
        :type other: Matrix.
        :rtype Bool.
        """

        return self.matrix == other.matrix

    def constant_multiplication(self, number):
        """Умножение матрицы на число.

        :param self: Матрица для умножения.
        :type self: Matrix.
        :param number: Число, на которое умножают.
        :type number: int.
        :rtype Matrix.
        """

        const_mul_matrix = [list(map(lambda x: number * x, item)) for item in [row for row in self.matrix]]
        return Matrix(const_mul_matrix)

    def transpose(self):
        """Возвращает транспонированную матрицу.

        :param self: Матрица для транспонирования.
        :type self: Matrix.
        :returns transposed: Транспонированная матрица.
        :rtype Matrix.
        """

        rows, columns = self.columns, self.rows
        transposed = Matrix(rows, columns)
        transposed.matrix = [list(item) for item in zip(*self.matrix)]
        return transposed

    def show(self):
        """Отображает элементы матрицы.

        :param self: Матрица.
        :type self: Matrix.
        """

        printed_matrix = '\n'.join([' '.join([str(item) for item in row]) for row in self.matrix])
        print(printed_matrix + '\n')

    def is_squared(self):
        """Проверяет, является ли матрица квадратной.

        :param self: Матрица.
        :type self: Matrix.
        :rtype Bool.
        """

        return self.rows == self.columns

    def is_symmetric_main_diag(self):
        """Проверяет, является ли матрица симметричной относительно главной диагонали.
        Бросает исключение, если матрица не является квадратной.

        :param self: Матрица.
        :type self: Matrix.
        :rtype Bool.
        """

        if not self.is_squared():
            raise MatrixException("Matrix is not squared! This method can't be called!")
        else:
            return self == self.transpose()

    def is_symmetric_secondary_diag(self):
        """Проверяет, является ли матрица симметричной относительно побочной диагонали.
        Бросает исключение, если матрица не является квадратной.

        :param self: Матрица.
        :type self: Matrix.
        :rtype Bool.
        """

        if not self.is_squared():
            raise MatrixException("Matrix is not squared! This method can't be called!")
        else:
            mirrored_matrix = Matrix(self.matrix[::-1])
            return mirrored_matrix.is_symmetric_main_diag()


if __name__ == '__main__':
    m = Matrix(2, 3)
    m.show()
    m.transpose().show()

    m1 = Matrix([[1, 2, 0], [3, 4, 2], [0, 3, 1]])
    print(m1.is_symmetric_main_diag())
    m1.transpose().show()
