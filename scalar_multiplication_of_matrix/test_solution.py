from solution import scalar_multiply

def test_basic_example():
    assert scalar_multiply(matrix = [[1, 2], [3, 4]], scalar = 2) == [[2, 4], [6, 8]]