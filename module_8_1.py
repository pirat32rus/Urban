def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return round(a + b, 3)
    elif isinstance(a, str) or isinstance(b, str):
        if isinstance(a, (int, float)):
            a = str(round(a, 3))
        if isinstance(b, (int, float)):
            b = str(round(b, 3))
        return str(a) + str(b)
    else:
        raise TypeError("Unsupported types for add_everything_up")

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
