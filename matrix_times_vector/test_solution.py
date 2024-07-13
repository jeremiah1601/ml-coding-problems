from solution import solution, vector_product


def test_basic_matrix_example():
    matrix: list[list[int]] = [[1,2],[2,4]]
    vector: list[int] = [1,2]

    assert solution(matrix, vector) == [5, 10]

def test_vector_product_basic_1():
    a = [1,2]
    b = [1,2]
    assert vector_product(a, b) == 5


def test_vector_product_basic_2():
    a = [2,4]
    b = [1,2]
    assert vector_product(a, b) == 10

