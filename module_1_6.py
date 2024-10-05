my_dict = {"petya": 1956, "dima": 1996, "egor": 2001,}
print("Dikt", my_dict)
print("Existing value:", my_dict.get("egor"))
print("Not existing value:",my_dict.get("ivan"))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
deleted_value = my_dict.pop("dima", None)
print("deleted_value", deleted_value)
print("modified dictionary:", my_dict)


my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', (5, 6, 1.6)}
print("\nSet:", my_set)
my_set.update({13, (5, 6, 1.6)})
my_set.discard('Яблоко')
print("Modified set:", my_set)
