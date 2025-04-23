from src.modified_counting_sort import mod_count_sort
from tests.test_sorting import create_test_data
from random import shuffle
from time import perf_counter_ns
import pandas as pd


n_s = [10**i for i in range(2, 7)]
k_s = [i/100 for i in range(1, 41, 4)]

results = []
for n in n_s:
    for k_frac in k_s:
        for _ in range(20):
            k = int(k_frac * n) 
            test_data = create_test_data(n, k)
            shuffled_data = test_data.copy()
            shuffle(shuffled_data)
            
            tic = perf_counter_ns()
            my_sorted_data = mod_count_sort(shuffled_data, 'val')
            toc = perf_counter_ns()
            my_time = toc - tic
            
            tic = perf_counter_ns()
            python_sorted_data = sorted(shuffled_data, key=lambda shuffled_data: shuffled_data.val)
            toc = perf_counter_ns()
            python_time = toc - tic
            
            results.append((n, k_frac, k, my_time, python_time))
results_df = pd.DataFrame(results, columns=['n', 'k_frac', 'k', 'my_time', 'python_time'])
results_df.to_csv('figures/figure_data.csv', index=False)