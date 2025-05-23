from time  import time

def special_pythagorean_triplet():
    for a in range(1,999):
        for b in range(a, 1000):
            for c in range(b,1000):
                if is_pythagorean_triplet(a,b,c):
                    if (a + b + c) == 1000:
                        return a,b,c 

def is_pythagorean_triplet(a,b,c):
    if (a**2 + b**2) == c**2:
        return True
    return False

def optimised_special_pythagorean_triplet():
    for a in range(333,3,-1):
        for b in range(a, round((1000 - a)/2)):
            c_squared = (1000 - a - b)**2
            if a**2 + b**2 == c_squared:
                return a*b*(1000-a-b)

start = time()
print(special_pythagorean_triplet())

print(f"brute force took: {time() - start}")

start = time()
print(optimised_special_pythagorean_triplet())
print(f"Optimised took: {time() - start}")
