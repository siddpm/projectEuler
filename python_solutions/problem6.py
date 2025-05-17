
def problem006():
    squared_sum = 0
    simple_sum = 0
    for i in range(101):
        squared_sum += i**2
        simple_sum += i
    
    return simple_sum**2 - squared_sum

if __name__ == "__main__":
    print(problem006())

    
