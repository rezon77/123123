def get_sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def get_count_of_digits(n):
    return len(str(n))

def main():
    n = int(input("Введите число: "))
    
    s = get_sum_of_digits(n)
    c = get_count_of_digits(n)
    diff = s - c
    
    print(f"\nСумма чисел: {s}")
    print(f"Количество цифр в числе: {c}")
    print(f"Разность суммы и количества цифр: {diff}")

if __name__ == '__main__':
    main()
