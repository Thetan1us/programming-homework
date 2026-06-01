package main

import "fmt"

func sockMerchant(n int32, ar []int32) int32 {
	colorCounts := make([]int32, 101)

	for i := 0; i < len(ar); i++ {
		color := ar[i]
		colorCounts[color]++
	}

	var totalPairs int32 = 0

	for color := 1; color <= 100; color++ {
		totalPairs += colorCounts[color] / 2
	}

	return totalPairs
}

func main() {
	var n int32
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Помилка зчитування кількості шкарпеток:", err)
		return
	}

	ar := make([]int32, n)
	for i := 0; i < int(n); i++ {
		fmt.Scan(&ar[i])
	}

	result := sockMerchant(n, ar)
	fmt.Println(result)
}
