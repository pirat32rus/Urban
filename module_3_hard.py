def count_elements(*args):
    total = 0
    for data in args:
        if isinstance(data, dict):
            for key, value in data.items():
                total += count_elements(key, value)
        elif isinstance(data, (list, tuple, set)):
            total += count_elements(*data)
        elif isinstance(data, str):
            total += len(data)
        elif isinstance(data, (int, float)):
            total += data
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]

result = count_elements(*data_structure)
print(result)  # Вывод: 99
