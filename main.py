"""Module with functions."""
from typing import List, Optional, Tuple

def largest_sum(numbers: list[int]) -> Optional[tuple[int, int]]:
    if len(numbers) < 2:
        return None
    """Encontra e retorna os dois números que somados dão o maior valor."""
     
    sorted_numbers = sorted(numbers)
    primeiro = sorted_numbers[-2]
    segundo = sorted_numbers[-1]
    
    return primeiro, segundo

list1 = [1, 2, 3, 4, 5]
result1 = largest_sum(list1)
print(result1)

list2 = [10, -5, 20, 15, -30]
result2 = largest_sum(list2)
print(result2)

list3 = [0, 0, 0, 0]
result3 = largest_sum(list3)
print(result3)

list4 = [-10, -5, -2, -1]
result4 = largest_sum(list4)
print(result4)

list5 = [5]
result5 = largest_sum(list5)
print(result5)

list6 = []
result6 = largest_sum(list6)
print(result6)
