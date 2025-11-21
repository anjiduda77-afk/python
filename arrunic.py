import numpy as np
arr=np.array([1,2,2,3,4,4,4,5])
print("Original array:",arr)

print("\nusing repr():")
print(repr(arr))

print("\nusing count():")
arr_list=arr.tolist()
print("count of 4 in array:",arr_list.count(4))

print("\nusing np.bincount():")
print("Elements counts (by index):",np.bincount(arr))

print("\nusing np.unique():")
unique_elements,counts=np.unique(arr,return_counts=True)
print("unique elements:",unique_elements)
print("Counts:",counts)