def problem004() -> int:
    largest_val = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            val = i * j
            str_val = str(val)

            if str_val == str_val[::-1]:
                if val > largest_val:
                    largest_val = val

    return largest_val
