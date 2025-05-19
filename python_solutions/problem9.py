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

print(special_pythagorean_triplet())