def digit_factorials_sum():

    fact = {}
    fact["0"] = 1
    fact["1"] = 1
    fact["2"] = 2
    fact["3"] = 3 * fact["2"]
    fact["4"] = 4 * fact["3"]
    fact["5"] = 5 * fact["4"]
    fact["6"] = 6 * fact["5"]
    fact["7"] = 7 * fact["6"]
    fact["8"] = 8 * fact["7"]
    fact["9"] = 9 * fact["8"]

    digit_fact_sum = 0
    # 2540160 is 9 ! * 7 . We only need to calculate until this number
    # since 9999999 > 9! * 7 , so from above 10000000, no factorial can reach the "raw" number
    # But we can improve that upper bound:- 9! * 7  = 2540160 and no number above this can have its factorial digits sum be larger than the actual number

    for i in range(11, 2540160 + 1):
        temp_val = 0
        si = str(i)

        for digit in si:
            temp_val += fact[digit]

        if temp_val == i:
            print("Number of interest: ", i)
            digit_fact_sum += i

    return digit_fact_sum


if __name__ == "__main__":
    print(
        "The sum of all numbers which are equal to the sum of the factorial of their digits: ",
        digit_factorials_sum(),
    )
