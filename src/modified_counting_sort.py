from collections import defaultdict
from multiprocessing import Pool, cpu_count

def scan_batch(list_in, sorting_attribute):
    indices = defaultdict(list)
    for i, elem in enumerate(list_in):
        indices[getattr(elem, sorting_attribute)].append(i)
    return indices

def mod_count_sort(list_in, sorting_attribute, cpu_count_frac=0.75):    
    # assuming list_in is an iterable of objects
    # sorting_attribute indicates which attribute of the object to sort by
    num_cpus_total = cpu_count()
    num_cpus_to_use = int(num_cpus_total*cpu_count_frac)
    # add errors for cpu_count_frac, sorting_attribute existence (?), list_in size 
    # batching could be done dependent on size of n?
    # batch and scan through list_in for indices of each unique sorting element
    batch_size = int((len(list_in) / num_cpus_to_use)+1)
    # i think this next line could be sped up
    batched_list_in = [(list_in[i:i+batch_size], sorting_attribute) for i in range(0, len(list_in), batch_size)]
    with Pool(num_cpus_to_use) as pool:
        all_indices_dicts = pool.starmap(scan_batch, batched_list_in)
    list_out = []
    # need all uniques elements of list_in to sort and later loop through
    # need to try to speed this up too
    keys = set()
    for indices_dict in all_indices_dicts:
        keys = keys.union(indices_dict.keys())
    keys = list(keys)
    keys.sort()
    # add warning if len(keys) is too high    
    # loop through all keys and all key indices dicts to build list_out
    for key in keys:
        for i, indices_dict in enumerate(all_indices_dicts):
            target_indices = indices_dict[key]
            target_list = batched_list_in[i][0]
            for target_index in target_indices:
                list_out.append(target_list[target_index])
    return list_out