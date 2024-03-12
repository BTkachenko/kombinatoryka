-- Definicja funkcji do obliczenia n!
factorial :: Integer -> Integer
factorial 0 = 1  -- Bazowy przypadek: 0! = 1
factorial n = n * factorial (n-1)  -- Rekurencyjna definicja n!

-- Funkcja do obliczenia n pierwszych elementów formalnej odwrotności szeregu f(n)
inverseSeries :: (Integer -> Double) -> Integer -> [Double]
inverseSeries f n = let a0 = f 0 in  -- Obliczenie f(0)
  if a0 == 0 then error "f(0) must not be zero."  -- Sprawdzenie, czy f(0) nie jest zerem
  else map (b f a0) [0..(n-1)]  -- Obliczenie n pierwszych elementów formalnej odwrotności

-- Pomocnicza funkcja do obliczenia elementu formalnej odwrotności
b :: (Integer -> Double) -> Double -> Integer -> Double
b f a0 n
  | n == 0    = 1 / a0  -- Bazowy przypadek: g(0) = 1 / f(0)
  | otherwise = - (sum [ (f k) * (b f a0 (n-k)) | k <- [1..n]]) / a0  -- Obliczenie g(n)

-- Główna funkcja
main :: IO ()
main = do
  let n = 10  -- Liczba elementów do obliczenia
  -- Wywołanie funkcji inverseSeries dla różnych funkcji f(n) i wydrukowanie wyników
  print $ "First " ++ show n ++ " coefficients of the inverse series for f(n) = 1 are: " ++ show (inverseSeries (\_ -> 1) n)
  print $ "First " ++ show n ++ " coefficients of the inverse series for f(n) = 2^n are: " ++ show (inverseSeries (\n -> 2^n) n)
  print $ "First " ++ show n ++ " coefficients of the inverse series for f(n) = n! are: " ++ show (inverseSeries (\n -> fromIntegral (factorial n)) n)
  print $ "First " ++ show n ++ " coefficients of the inverse series for f(n) = 1/n! are: " ++ show (inverseSeries (\n -> 1 / (fromIntegral (factorial n))) n)
