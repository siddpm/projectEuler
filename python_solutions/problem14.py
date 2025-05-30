'''
Longest collatz sequence below 1000000
'''
from time import time

def longest_collatz_sequence():

    collatz_dict = {}
    longest_sequence_number = 1
    longest_sequence_count = 0

    for i in range(1000000):
        sequence = i 
        count = 1

        while sequence > 1:
            if sequence % 2 == 0:
                sequence = sequence // 2
            else:
                sequence = sequence*3 + 1
            
            count += 1

            if sequence in  collatz_dict:
                count += collatz_dict[sequence]
                break
        
        # Remember the sequence length for starting value i 
        collatz_dict[i] = count

        # check if this is the longest sequence seen so far
        if count > longest_sequence_count:
            longest_sequence_count = count
            longest_sequence_number = i

    return longest_sequence_number, longest_sequence_count
    

if __name__ == "__main__":
    start = time()
    print(longest_collatz_sequence())
    print("Total time:", time() - start)
    