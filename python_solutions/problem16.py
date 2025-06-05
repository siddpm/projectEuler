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

'''
While trying to find a solution to this where
I didnt have to compute each power of 2 until a 1000 (there isn't one)
I came across the neat fact of n mod 9 = sum_digits(n) mod 9
as 9 is the digital root of our base 10 numerical system.
'''

if __name__ == "__main__":
    print(power_digit_sum())