// https://www.hackerrank.com/challenges/staircase/problem

package main

import "fmt"

func staircase(n int32) {
	for i := int32(1); i <= n; i++ {

		for j := int32(0); j < n-i; j++ {
			fmt.Print(" ")
		}

		for k := int32(0); k < i; k++ {
			fmt.Print("#")
		}

		fmt.Println()
	}
}

func main() {
	var n int32 = 6
	staircase(n)
	// Юніт тести не додавав, оскільки функція не повертає значень
}
