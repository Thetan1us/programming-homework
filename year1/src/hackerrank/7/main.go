package main

import "fmt"

func breakingRecords(scores []int32) []int32 {
	if len(scores) == 0 {
		return []int32{0, 0}
	}

	minRecord := scores[0]
	maxRecord := scores[0]

	var countMax int32 = 0
	var countMin int32 = 0

	for i := 1; i < len(scores); i++ {
		currentScore := scores[i]

		if currentScore > maxRecord {
			maxRecord = currentScore
			countMax++
		} else if currentScore < minRecord {
			minRecord = currentScore
			countMin++
		}
	}

	return []int32{countMax, countMin}
}

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Помилка зчитування кількості ігор:", err)
		return
	}

	scores := make([]int32, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&scores[i])
	}

	result := breakingRecords(scores)

	fmt.Printf("%d %d\n", result[0], result[1])
}
