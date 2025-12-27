
def merge_lists_and_cube(list1: list, list2: list) -> list:  
    unique_elements = set(list1 + list2)
    result = [element **3 for element in unique_elements]
    return result
a=[1,4,5]
b=[2,7,9]
print(merge_lists_and_cube(a,b))

