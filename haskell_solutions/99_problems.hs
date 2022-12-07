myLast [x] = x
myLast (_ : xs) = myLast xs

myButLast [x, _] = x
myButLast (x : xs) = myButLast xs

myButLast' x = last $ init x

myReverse :: [a] -> [a]
myReverse [] = []
myReverse x = reverse x

myReverse' :: [a] -> [a]
myReverse' [] = []
myReverse' (x : xs) = myReverse' xs ++ [x]

-- Creating a reverse funciton using an accumulator
myReverseAcc :: [a] -> [a]
myReverseAcc lst = myReverseAcc' lst []
  where
    myReverseAcc' [] acc = acc
    myReverseAcc' (x : xs) acc = myReverseAcc' xs (x : acc)

isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome [] = True
isPalindrome [_] = True
isPalindrome x = x == reverse x

-- Problem 7
data NestedList a = Elem a | List [NestedList a]

show' :: NestedList a -> a
show' (Elem x) = x
show' _ = error "dont do it"

flatten :: NestedList a -> [a]
flatten (Elem a) = [a]
flatten (List (x : xs)) = flatten x ++ flatten (List xs)
flatten (List []) = []

-- Problem 8
compress :: (Eq a) => [a] -> [a]
compress lst = reverse $ cmprs lst []
  where
    cmprs [] acc = acc
    cmprs (x : xs) [] = cmprs xs [x]
    cmprs (x : xs) acc =
      if (head acc) == x
        then cmprs xs acc
        else cmprs xs (x : acc)

pack :: (Eq a) => [a] -> [[a]]
pack [] = []
pack x =
  let (lst, lstx) = span (== head x) x
   in lst : pack lstx

-- I need a function that gives a list of the consective duplicates

duplicates :: (Eq a) => [a] -> [a]
duplicates x = filter (== head x) x

addfive :: (Eq a, Num a) => Maybe a -> Maybe a
addfive val = do
  x <- val
  case x of
    0 -> return x
    _ -> return (x + 5)

addfive' :: (Eq a, Num a) => Maybe a -> Maybe a
addfive' val = case val of
  Nothing -> Nothing
  (Just x) -> Just $ x + 5

encode :: (Eq a) => [a] -> [(Int, a)]
encode lst = map (\x -> (length x, head x)) $ pack lst

-- A function that given a value returns if the value is a prime
--prime :: Floating a => a -> Bool
prime :: Int -> Bool
prime 1 = False
prime 2 = True
prime p = null [x | x <- 2 : [3, 5 .. p -1], mod p x == 0]

-- Create a data type here of ListItem

data ListItem a = Multiple Int a | Single a
  deriving (Show)

encodeModified :: (Eq a) => [a] -> [ListItem a]
encodeModified lst = map encodehelper $ pack lst
  where
    encodehelper a =
      if length a == 1
        then Single $ head a
        else Multiple (length a) (head a)

decodeModified :: (Eq a) => [ListItem a] -> [a]
decodeModified lst = map decodeSingle lst
  where
    decodeSingle (Single a) = a
    decodeSingle (Multiple rep a) = a

-- concat $ replicate rep a