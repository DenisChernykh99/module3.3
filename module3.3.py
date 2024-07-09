def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(14, 'Привет', 25.5)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Пока', 14, False]
values_dict = {'a': 'Denis', 'b': 25.5, 'c': [1, 2]}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [[2, 'Правда'], 'Неправда']
print_params(*values_list2, 42)
