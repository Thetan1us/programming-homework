package main

import "fmt"

func gradingStudents(grades []int32) []int32 {
	result := make([]int32, len(grades))

	for i := 0; i < len(grades); i++ {
		grade := grades[i]

		if grade < 38 {
			result[i] = grade
		} else {
			nextMultipleOfFive := ((grade / 5) + 1) * 5

			if nextMultipleOfFive-grade < 3 {
				result[i] = nextMultipleOfFive
			} else {
				result[i] = grade
			}
		}
	}

	return result
}

func main() {
	sampleGrades := []int32{73, 67, 38, 33}
	roundedGrades := gradingStudents(sampleGrades)

	fmt.Println("Початкові оцінки:", sampleGrades)
	fmt.Println("Округлені оцінки:", roundedGrades)
}
