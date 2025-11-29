import math


# Still using brute force but its more optimised
def integer_right_triangles_optimised():
    # Max solutions seen so far
    max_sol = 0
    max_p = 0

    # optimisation 1: perimeters can only be even
    for p in range(10, 1200 + 1, 2):
        p_solutions = 0
        # assuming a is always the shortest side of candidate triangles,
        # it can only ever be less than 1/3 of the perimeter
        for a in range(1, p // 3):
            # assuming b is either equal to or greater than a for all candidate triangles
            for b in range(a, (p - a) // 2):
                c = p - a - b
                # we check if its a right angle triangle,
                # avoiding finding square roots and keeping things only in integers
                if (a * a + b * b) == c * c:
                    p_solutions += 1

        # Update max solutions
        if p_solutions > max_sol:
            max_sol = p_solutions
            max_p = p

    return max_p


def integer_right_triangles():

    # Max solutions seen so far
    max_sol = 0
    max_p = 0

    for p in range(10, 1200 + 1):
        p_solutions = 0
        for a in range(1, p // 2):
            for b in range(1, (p - a) // 2):
                if (a + b + math.sqrt(a**2 + b**2)) == p:
                    p_solutions += 1

        # Update max solutions

        if p_solutions > max_sol:
            max_sol = p_solutions
            max_p = p

    return max_p


if __name__ == "__main__":
    print(
        "The value of p for which the number of solutions is maximised: ",
        integer_right_triangles(),
    )
    print("Optimised solution: ", integer_right_triangles_optimised())
