import pytest
from random import randint, sample
from math import sqrt

class DataObject:
    def __init__(self, val):
        self.val = val
        self.ID = randint(0, 10**9)
    def __repr__(self):
        return f'DataObject(val={self.val}, ID={self.ID})'

def create_test_data(n, k):
    nums = range(0, k)
    splits = [0] + sample(range(1, n-1), k-1) + [n]
    test_data = [None]*n
    for i in range(len(splits)-1):
        object_list = []
        for j in range(splits[i+1]-splits[i]):
            object_list.append(DataObject(nums[i]))
        test_data[splits[i]:splits[i+1]] = object_list
    return test_data

