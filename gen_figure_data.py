from src.modified_counting_sort import mod_count_sort
from tests.test_sorting import create_test_data
from random import shuffle

test_data = create_test_data(15, 4)
shuffled_data = test_data.copy()
shuffle(shuffled_data)
my_sorted_data = mod_count_sort(shuffled_data, 'val')
python_sorted_data = sorted(shuffled_data, key=lambda test_data: test_data.val)
for i in range(len(test_data)):
    print(python_sorted_data[i])
    print(my_sorted_data[i])
    print('-------')