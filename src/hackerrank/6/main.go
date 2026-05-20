package main

import "fmt"

func getTotalX(a []int32, b []int32) int32 {
	var count int32 = 0

	var maxA int32 = 0
	for _, val := range a {
		if val > maxA {
			maxA = val
		}
	}

	var minB int32 = 100
	for _, val := range b {
		if val < minB {
			minB = val
		}
	}

	for x := maxA; x <= minB; x++ {
		isValid := true

		for _, valA := range a {
			if x%valA != 0 {
				isValid = false
				break
			}
		}

		if !isValid {
			continue
		}

		for _, valB := range b {
			if valB%x != 0 {
				isValid = false
				break
			}
		}

		if isValid {
			count++
		}
	}

	return count
}

func main() {
	var n, m int

	_, err := fmt.Scan(&n, &m)
	if err != nil {
		fmt.Println("Помилка зчитування:", err)
		return
	}

	a := make([]int32, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	b := make([]int32, m)
	for i := 0; i < m; i++ {
		fmt.Scan(&b[i])
	}

	fmt.Println(getTotalX(a, b))
}
