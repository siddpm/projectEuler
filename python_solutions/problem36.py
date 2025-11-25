def doublebase_palindrome_sum():
    sum_val = 0
    for i in range(1_000_000):
        i_str = str(i)
        if i_str == i_str[::-1]:
            # check binary now (cleanup 0b in string format)
            binary_i = bin(i)[2:]
            if binary_i == binary_i[::-1]:
                sum_val += i
    return sum_val


if __name__ == "__main__":
    print("The sum of all double base palindromes are: ", doublebase_palindrome_sum())
