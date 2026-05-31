package main

import "fmt"

func migratoryBirds(arr []int32) int32 {
	frequencies := make([]int32, 6)

	for i := 0; i < len(arr); i++ {
		birdID := arr[i]
		frequencies[birdID]++
	}

	var maxFrequency int32 = 0
	var mostFrequentBirdID int32 = 0

	for id := 1; id <= 5; id++ {
		if frequencies[id] > maxFrequency {
			maxFrequency = frequencies[id]
			mostFrequentBirdID = int32(id)
		}
	}

	return mostFrequentBirdID
}

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Помилка зчитування розміру масиву:", err)
		return
	}

	arr := make([]int32, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	result := migratoryBirds(arr)
	fmt.Println(result)
}
