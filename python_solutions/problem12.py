from functools import reduce
from helpers import prime_factors


def brute_force():
    k = 2

    while True:
        # Compute Triangular number values
        # Using formula Tn = n(n+1)/2  (this is the sum of series 1 + 2 + 3 +  4 + ... + n)
        tn = (k*(k + 1))//2

        # Retireve all prime factors of tn 
        prime_factors_dict = prime_factors(tn)
                
        
        # Now that we know the prime factors as well as the exponents of the factors, for example 28 = 2*2*7 = (2^2)*(7^1)
        # we can compute all factors using the formula that uses their exponents
        #  where a and b are exponents of subsequently higher prime factors:
        # total num factors = (a + 1)* (b + 1) =(2 + 1)* (1 + 1) = 6
        prime_factor_exponents = [value + 1 for _,value in prime_factors_dict.items()]
        
        total_factors = reduce(lambda x,y: x*y, prime_factor_exponents)

        # Terminating condition if num factors is 500 or higher
        if total_factors >= 500:
            return tn
        
        k += 1


def highly_divisible_triangular_number():
        k = 2

        while True:
            # Compute Triangular number values
            # Using formula Tn = n(n+1)/2  (this is the sum of series 1 + 2 + 3 +  4 + ... + n)
            tn = (k*(k + 1))//2

            # Retireve all prime factors of tn 
            prime_factors_dict = prime_factors(tn)
                    
            
            # Now that we know the prime factors as well as the exponents of the factors, for example 28 = 2*2*7 = (2^2)*(7^1)
            # we can compute all factors using the formula that uses their exponents
            #  where a and b are exponents of subsequently higher prime factors:
            # total num factors = (a + 1)* (b + 1) =(2 + 1)* (1 + 1) = 6
            prime_factor_exponents = [value + 1 for _,value in prime_factors_dict.items()]
            
            total_factors = reduce(lambda x,y: x*y, prime_factor_exponents)

            # Terminating condition if num factors is 500 or higher
            if total_factors >= 500:
                return tn
            
            k += 1





if __name__ == "__main__":
    print(brute_force())
    # print(highly_divisible_triangular_number())


