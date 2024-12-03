def calc_struct(data_structure):
    sum = 0
    if isinstance(data_structure, str):
        sum += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calc_struct(key)
            sum += calc_struct(value)
    elif isinstance(data_structure, (list, set, tuple)):
        for item in data_structure:
            sum += calc_struct(item)
    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calc_struct(data_structure)
print(result)