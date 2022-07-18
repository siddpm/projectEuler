import Control.Monad (guard)

-- Warmup problems

-- Problem 1, unnecessarily using do-noation while a list comprehension would "do"
-- Sub-optimal solution, runs in O(n)
-- https://projecteuler.net/problem=1

problem001 :: Int -> Int
problem001 a =
  let lstgen = do
        val <- [1 .. a]
        guard $ (mod val 3 == 0) || (mod val 5 == 0)
        return val
   in sum lstgen

-- Better solution, runs in O(1)
-- Uses number theory
-- the sum of series (1 + 2 + 3 + ..n) = n(n + 1)/2
sumseries :: Int -> Int
sumseries n = n * (n + 1) `div` 2

-- factor multiples of 3 as : 3(1 + 2 + 3 ...)
-- factor multiples of 5 as : 5(1 + 2 + 3 ...)
-- apply above summation
-- Note : we end up double counting multiples of both 3 and 5
-- factor multiples of 15 and minus them from total

problem001' :: Int -> Int
problem001' n =
  let mult3s = 3 * sumseries (n `div` 3)
      mult5s = 5 * sumseries (n `div` 5)
      mult15s = 15 * sumseries (n `div` 15)
   in mult3s + mult5s - mult15s

-- Problem 2 : Even Fibonacci numbers

-- Suboptimal solution, keeps recomputing the same values over
fib :: Int -> Int
fib 1 = 1
fib 2 = 2
fib n = fib (n - 1) + fib (n - 2)

-- Optimal solution that works with infinite lists
-- Its a bit unintuitive but generally the idea is as follows
-- You're trying to generate a new fib number while on the go,
-- using what has already been computed to produce the next numbers

fibs :: [Int]
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

problem002 :: Int
problem002 = sum $ filter even $ takeWhile (< 4000000) fibs

isPrime :: Int -> Bool
isPrime 1 = False
isPrime a = not $ any (\y -> mod a y == 0) oddSqrtLst
  where
    oddSqrtLst = takeWhile (\y -> y * y <= a) [2 ..]

-- Create an infinite prime number generator
primesGen :: [Int]
primesGen = filter isPrime [1 ..]

-- Problem 10 : summation of primes below 2000000
problem003 :: (Num a, Ord a) => [a] -> a -> a
problem003 lst limit = sum $ takeWhile (< limit) lst
