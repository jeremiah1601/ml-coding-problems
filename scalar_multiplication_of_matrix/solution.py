
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return [[item * scalar for item in row]for row in matrix]

if __name__ == "__main__":
    pass