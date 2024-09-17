from functional import seq


one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_values_divided_by_two = seq(one_to_ten).filter(lambda n: n % 2 == 0).map(lambda n: int(n/2))

print(even_values_divided_by_two)
