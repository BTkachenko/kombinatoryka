countSequences :: Int -> (Int, Int, Double)
countSequences n = (seqWithAAA, seqWithABB, avgOccurrencesAAA)
  where
    totalSeq = 2 ^ n

    updateAAA dp = [
        dp !! 0 + dp !! 3,
        dp !! 1 + dp !! 3,
        dp !! 2 + dp !! 3,
        sum dp
        ]
        
    updateABB dp = [
        dp !! 0 + dp !! 3,
        dp !! 1 + dp !! 3,
        dp !! 2 + dp !! 3,
        sum dp
        ]

    dpAAA = iterate updateAAA [1, 0, 0, 0] !! n
    dpABB = iterate updateABB [1, 0, 0, 0] !! n
        
    occurrencesAAA = sum $ map last $ take (n + 1) $ iterate updateAAA [1, 0, 0, 0]
        
    seqWithAAA = totalSeq - sum (take 3 dpAAA)
    seqWithABB = totalSeq - sum (take 3 dpABB)
    avgOccurrencesAAA = fromIntegral occurrencesAAA / fromIntegral totalSeq

main :: IO ()
main = do
    let n = 10  -- You can change this to any value <= 50
    let (seqWithAAA, seqWithABB, avgOccurrencesAAA) = countSequences n
    print (seqWithAAA, seqWithABB, avgOccurrencesAAA)
