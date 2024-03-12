-- Funkcja obliczająca sumę dzielników wszystkich liczb od 1 do maxN
calculateSigmas :: Int -> [Int]
calculateSigmas maxN = map sigma [1..maxN]
  where
    sigma n = sum [i | i <- [1..n], n `mod` i == 0]

-- Funkcja obliczająca wartości pn dla n = 1 do maxN
calculatePn :: Int -> [Int]
calculatePn maxN = pn
  where
    sigmas = calculateSigmas maxN
    pn = 1 : [sum [(sigmas !! (j - 1)) * (pn !! (n - j)) | j <- [1..n]] `div` n | n <- [1..maxN]]

-- Wywołanie funkcji dla n = 1 do 100
main :: IO ()
main = print $ take 100 $ calculatePn 100
