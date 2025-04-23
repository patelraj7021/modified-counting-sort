from collections import defaultdict

def mod_count_sort(list_in, sorting_attribute):    
    # assuming list_in is an iterable of objects
    # sorting_attribute indicates which attribute of the object to sort by
    indices = defaultdict(list)
    for i, elem in enumerate(list_in):
        indices[getattr(elem, sorting_attribute)].append(i)
    list_out = []
    keys = list(indices.keys())
    keys.sort()
    for key in keys:
        target_indices = indices[key]
        for target_index in target_indices:
            list_out.append(list_in[target_index])
    return list_out