import matplotlib.pyplot as plt
import pandas as pd

figure_data = pd.read_csv('figures/figure_data.csv')

k_frac = 0.01

fig, ax = plt.subplots()
filtered_data = figure_data[figure_data['k_frac'] == k_frac]
agg_data = filtered_data.groupby('n').agg({'my_time': ['mean', 'std'], 'python_time': ['mean', 'std']})
ax.errorbar(x=agg_data.index, y=agg_data['my_time', 'mean'], yerr=agg_data['my_time', 'std'], 
            label='This Algorithm', c='blue', fmt='o')
ax.errorbar(x=agg_data.index, y=agg_data['python_time', 'mean'], yerr=agg_data['python_time', 'std'], 
            label='Python Default', c='red', fmt='o')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('n')
ax.set_ylabel('Time (ns)')
ax.legend(loc='lower right')
ax.set_title('$k_{frac}$ = ' + f'{k_frac}')
fig.savefig('figures/figure_1.png')