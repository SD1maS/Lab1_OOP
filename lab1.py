import random

class MatrixOperations:

    @staticmethod
    def gen_rnd_matrix(rows: int, cols: int) -> list[list[int]]:
        return [[random.randint(-32768, 32767) for l in range(cols)] for l in range(rows)]
                        # Діапазон значень типу short

    @staticmethod
    def multiply_matrices(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
        if not matrix_a or not matrix_b or not matrix_a[0] or not matrix_b[0]:
            raise ValueError("Матриці не можуть бути порожніми.")

        m = len(matrix_a)
        n = len(matrix_a[0])
        p = len(matrix_b[0])

        if len(matrix_b) != n:
            raise ValueError("Кількість стовпців матриці A повинна дорівнювати кількості рядків матриці B.")

        result = [[0 for l in range(p)] for l in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return result

    @staticmethod
    def calculate_minmax_sum(matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            raise ValueError("Матриця не може бути порожньою.")

        total_sum = 0
        for i in range(len(matrix)):
            if not matrix[i]:
                raise ValueError("Рядок матриці не може бути порожнім.")
            if (i + 1) % 2 == 0:
                total_sum += max(matrix[i])
            else:
                total_sum += min(matrix[i])
        return total_sum

    @staticmethod
    def print_matrix(matrix: list[list[int]]) -> None:
        for row in matrix:
            print("\t".join(str(value) for value in row))
        print()


def main():
    matrix_a = MatrixOperations.gen_rnd_matrix(3, 4)
    matrix_b = MatrixOperations.gen_rnd_matrix(4, 3)

    try:
        print("\n\033[1mДія 1: Матричний добуток (C = A * B)\033[0m")
        matrix_c = MatrixOperations.multiply_matrices(matrix_a, matrix_b)
        MatrixOperations.print_matrix(matrix_c)

        print("\033[1mДія 2: Обчислення суми найбільших (парні рядки) та найменших (непарні рядки) елементів\033[0m")
        total_sum = MatrixOperations.calculate_minmax_sum(matrix_c)
        print(f"Результат обчислення суми: {total_sum}\n\n")

    except ValueError as e:
        print(f"Помилка аргументів: {e}")
    except Exception as e:
        print(f"Непередбачувана помилка: {e}")


if __name__ == "__main__":
    main()