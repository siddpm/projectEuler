import Control.Monad (guard)

-- Warmup problems 

-- Problem 1, unnecessarily using do-noation while a list comprehension would "do" 
-- https://projecteuler.net/problem=1

problem001 :: Int  -> Int 
problem001 a = let lstgen = do 
                              val <- [1..a]
                              guard $ (mod val 3 == 0) || (mod val 5 == 0) 
                              return val
                in sum lstgen


-- Problem 432