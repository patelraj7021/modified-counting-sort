from collections import defaultdict

def mod_count_sort(list_in, sorting_index):    
    # assuming list_in is an iterable of iterables
    # e.g., of the format
    # [ (sorting_value, other_value, ...), ...]
    # sorting_index indicates which index of the inner iterable to sort by
    indices = defaultdict(list)
    for i, elem in enumerate(list_in):
        indices[elem[sorting_index]].append(i)
    list_out = []
    keys = indices.keys()
    keys.sort(reverse=True)
    for key in keys:
        target_indices = indices[key]
        for target_index in target_indices:
            list_out.append(list_in[target_index])
    return list_out