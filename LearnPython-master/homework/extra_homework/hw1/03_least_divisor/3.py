def find_smallest_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def main():
    n = int(input("Введите число: "))
    print(f"Наименьший делитель, отличный от единицы: {find_smallest_divisor(n)}")

if __name__ == '__main__':
    main()
