import numpy as np 

def solution(a: list[list[int]],
             b: list[int]) -> list[int]:
    # for row in rows do vector multiplication or return -1 if cant
    res = []
    for i in range(len(a)):
        if len(a[i]) != len(b):
            return -1
        res.append(vector_product(a[i], b))   
    return res
        

def vector_product(v_1: list[int], v_2: list[int]) -> int:
        return sum([v_1[i] * v_2[i] for i in range(len(v_1))])

if __name__=="__main__":
    pass