import pytest
from random import randint, sample, shuffle
from math import sqrt
from src.modified_counting_sort import mod_count_sort

class DataObject:
    def __init__(self, ID, val):
        self.val = val
        self.ID = ID
    def __repr__(self):
        return f'DataObject(val={self.val}, ID={self.ID})'

def create_test_data(n, k):
    nums = range(0, k)
    splits = [0] + sample(range(1, n), k-1) + [n]
    splits.sort()
    test_data = [None]*n
    ID_count = 0
    for i in range(len(splits)-1):
        object_list = []
        for j in range(splits[i+1]-splits[i]):
            object_list.append(DataObject(ID_count, nums[i]))
            ID_count += 1
        test_data[splits[i]:splits[i+1]] = object_list
    return test_data

@pytest.mark.parametrize('data_params_in', [
                (10, 3),
                (100, 5),
                (42342, 234),
                (234211, 23)])  
class TestCreateData:
    
    def test_len_data(self, data_params_in):
        original_list = create_test_data(*data_params_in)
        assert len(original_list) == data_params_in[0]
        
    def test_num_subsets(self, data_params_in):
        original_list = create_test_data(*data_params_in)
        vals = set()
        for elem in original_list:
            vals.add(elem.val)
        assert len(vals) == data_params_in[1]
        
    def test_IDs(self, data_params_in):
        original_list = create_test_data(*data_params_in)
        IDs = set()
        for elem in original_list:
            IDs.add(elem.ID)
        assert IDs == set(range(0, data_params_in[0]))

@pytest.mark.parametrize('data_params_in', [
                (10, 3),
                (100, 5),
                (42342, 234),
                (234211, 23),
                (132,100),
                (1234234, 1231)])          
class TestSortingFunction:

    def test_sorting(self, data_params_in):
        original_list = create_test_data(*data_params_in)
        shuffled_list = original_list.copy()
        shuffle(shuffled_list)
        my_sorted_list = mod_count_sort(shuffled_list, 'val')
        python_sorted_list = sorted(shuffled_list, key=lambda shuffled_list: shuffled_list.val)
        assert my_sorted_list == python_sorted_list