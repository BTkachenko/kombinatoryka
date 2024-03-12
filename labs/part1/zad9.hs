import System.Random (randomRIO)
import Control.Monad (replicateM)
import Data.List (elemIndex)

-- Implementacja algorytmu Fisher-Yates
fisherYates :: [a] -> IO [a]
fisherYates xs = go xs (length xs - 1)
  where
    go acc 0 = return acc
    go acc i = do
      j <- randomRIO (0, i)
      let swapped = swap i j acc
      go swapped (i - 1)

-- Zamiana elementów w liście
swap :: Int -> Int -> [a] -> [a]
swap i j xs = let (xi, xj) = (xs !! i, xs !! j)
              in [if k == i then xj else if k == j then xi else xk | (xk, k) <- zip xs [0..]]

-- Sprawdzenie czy permutacja ma stałe punkty
hasFixedPoint :: Eq a => [a] -> [a] -> Bool
hasFixedPoint original permuted = any (\(a, b) -> a == b) $ zip original permuted

-- Obliczenie liczby cykli w permutacji
countCycles :: Eq a => [a] -> [a] -> Int
countCycles original permuted = go original 0
  where
    go [] n = n
    go (x:xs) n = 
      let cycle = takeWhile (/= x) $ iterate (\y -> permuted !! (maybe 0 id $ elemIndex y original)) (permuted !! (maybe 0 id $ elemIndex x original))
          cycleComplete = x : cycle
      in go (filter (`notElem` cycleComplete) xs) (n + 1)

-- Główna funkcja
main :: IO ()
main = do
  let n = 1000 -- liczba permutacji
      m = 50  -- rozmiar zbioru
  perms <- replicateM n (fisherYates [1..m])
  let noFixedPoints = length $ filter (not . uncurry hasFixedPoint) $ zip (replicate n [1..m]) perms
      singleFixedPoint = length $ filter (\(orig, perm) -> length (filter id $ zipWith (==) orig perm) == 1) $ zip (replicate n [1..m]) perms
      avgCycles = (fromIntegral $ sum $ map (uncurry countCycles) $ zip (replicate n [1..m]) perms) / (fromIntegral n)
  putStrLn $ "Average number of permutations without fixed points: " ++ show (fromIntegral noFixedPoints / fromIntegral n)
  putStrLn $ "Average number of permutations with a single fixed point: " ++ show (fromIntegral singleFixedPoint / fromIntegral n)
  putStrLn $ "Average number of cycles: " ++ show avgCycles
