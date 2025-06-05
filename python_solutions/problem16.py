# The solution is trivial in Python
def power_digit_sum():
    value = 2
    for i in range(1,1000):
        value *= 2
    
    strigified_value = str(value)

    sum_val = 0
    for digit in strigified_value:
        sum_val += int(digit)
    
    return sum_val

if __name__ == "__main__":
    print(power_digit_sum())