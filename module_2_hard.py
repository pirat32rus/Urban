def generate_password(n):
    result = ""
    pairs = []

    for i in range(1, (n // 2) + 1):
        for j in range(i + 1, n + 1):
            sum_pairs = i + j
            if n % sum_pairs == 0:
                pairs.append(f"{i}{j}")

    result = ''.join(pairs)
    return result

n = int(input("Введите число (от 3 до 20): "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Нужный пароль: {password}")
else:
    print("Число вне диапазона.")
