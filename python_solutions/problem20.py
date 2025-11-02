def factorial_sum(n: int = 100):
    numbers_to_hundred = [i for i in range(2, 100)]
    # Multiplying by 10 doesnt alter final result
    numbers_to_hundred.remove(10)
    # Remove pairs that multiply to 100
    # (25,4) and (2,50)
    numbers_to_hundred.remove(25)
    numbers_to_hundred.remove(50)
    numbers_to_hundred.remove(2)
    numbers_to_hundred.remove(4)

    factorial_sum = 1

    for num in numbers_to_hundred:
        if num % 10 == 0:
            factorial_sum *= num // 10
        else:
            factorial_sum *= num

    str_nums = str(factorial_sum)

    count = 0
    for str_num in str_nums:
        count += int(str_num)

    return count


if __name__ == "__main__":
    print(factorial_sum())
