package main

import "fmt"

func diagonalDifference(arr [][]int32) int32 {
	var primarySum int32 = 0
	var secondarySum int32 = 0
	n := len(arr)

	for i := 0; i < n; i++ {
		primarySum += arr[i][i]
		secondarySum += arr[i][n-1-i]
	}

	difference := primarySum - secondarySum

	if difference < 0 {
		return -difference
	}
	return difference
}

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Помилка зчитування розміру матриці:", err)
		return
	}

	// Ініціалізуємо двовимірний слайс
	matrix := make([][]int32, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int32, n)
		for j := 0; j < n; j++ {
			fmt.Scan(&matrix[i][j])
		}
	}

	result := diagonalDifference(matrix)
	fmt.Println(result)
}
