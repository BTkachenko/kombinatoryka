package main

import (
	"fmt"
	"math/rand"
	"time"
)

// FisherYatesShuffle wykonuje losową permutację tablicy używając algorytmu Fisher-Yates.
func FisherYatesShuffle(arr []int) []int {
	n := len(arr)
	result := make([]int, n)
	copy(result, arr)

	rand.Seed(time.Now().UnixNano())

	for i := n - 1; i > 0; i-- {
		j := rand.Intn(i + 1)
		result[i], result[j] = result[j], result[i]
	}

	return result
}

// NoFixedPoints sprawdza, czy permutacja nie ma stałych punktów.
func NoFixedPoints(arr []int) bool {
	for i, val := range arr {
		if i+1 == val {
			return false
		}
	}
	return true
}

// OneFixedPoint sprawdza, czy permutacja ma dokładnie jeden stały punkt.
func OneFixedPoint(arr []int) bool {
	count := 0
	for i, val := range arr {
		if i+1 == val {
			count++
		}
	}
	return count == 1
}

func main() {
	const trials = 1000
	const n = 10

	noFixedPointsCount := 0
	oneFixedPointCount := 0

	for i := 0; i < trials; i++ {
		perm := FisherYatesShuffle(make([]int, n))
		for j := range perm {
			perm[j] = j + 1
		}

		if NoFixedPoints(perm) {
			noFixedPointsCount++
		}

		if OneFixedPoint(perm) {
			oneFixedPointCount++
		}
	}

	avgNoFixedPoints := float64(noFixedPointsCount) / float64(trials)
	avgOneFixedPoint := float64(oneFixedPointCount) / float64(trials)

	fmt.Printf("Średnia liczba permutacji bez stałych punktów: %f\n", avgNoFixedPoints)
	fmt.Printf("Średnia liczba permutacji z jednym punktem stałym: %f\n", avgOneFixedPoint)
}
