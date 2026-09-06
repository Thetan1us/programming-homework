package main

import "fmt"

func countFruits(s int32, t int32, a int32, b int32, apples []int32, oranges []int32) (int32, int32) {
	var appleCount int32 = 0
	var orangeCount int32 = 0

	for i := 0; i < len(apples); i++ {
		applePosition := a + apples[i]

		if applePosition >= s && applePosition <= t {
			appleCount++
		}
	}

	for i := 0; i < len(oranges); i++ {
		orangePosition := b + oranges[i]

		if orangePosition >= s && orangePosition <= t {
			orangeCount++
		}
	}

	return appleCount, orangeCount
}

func main() {
	var s, t int32 = 7, 11
	var a, b int32 = 5, 15
	apples := []int32{-2, 2, 1}
	oranges := []int32{5, -6}

	applesOnHouse, orangesOnHouse := countFruits(s, t, a, b, apples, oranges)

	fmt.Println(applesOnHouse)
	fmt.Println(orangesOnHouse)
}
