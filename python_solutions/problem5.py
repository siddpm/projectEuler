# Possible approach:
# Start from largest numbers and delete all the smaller numbers
# For example, if a number is divisible by 20, it is also divisible by 10,2,5 and etc.
# So we dont need to check for those numbers divisibilty.
# So keep deleting those numbers, it will be a list of [11,12,13,14,15,16,17,18,19,20]
# Now you can iterate from 21 and see which number divides all these!