import math


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
