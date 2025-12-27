def list_contains_value(items:list, value:int) -> bool:
    return value in items
numbers = [1,3,5,8,9]
print(list_contains_value(numbers,7))