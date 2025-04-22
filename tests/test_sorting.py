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
    splits = [0] + sample(range(1, n), k-1) + [n]
    splits.sort()
    test_data = [None]*n
    for i in range(len(splits)-1):
        object_list = []
        for j in range(splits[i+1]-splits[i]):
            object_list.append(DataObject(nums[i]))
        test_data[splits[i]:splits[i+1]] = object_list
    return test_data

@pytest.mark.parametrize('data_params_in', [
                (10, 3),
                (100, 5),
                (42342, 234),
                (234211, 23)])  
class TestCreateData:
    
    def test_len_data(self, data_params_in):
        sorted_list = create_test_data(*data_params_in)
        assert len(sorted_list) == data_params_in[0]
        
    def test_num_subsets(self, data_params_in):
        sorted_list = create_test_data(*data_params_in)
        vals = set()
        for elem in sorted_list:
            vals.add(elem.val)
        assert len(vals) == data_params_in[1]