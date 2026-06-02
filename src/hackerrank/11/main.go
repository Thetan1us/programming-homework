package main

import "fmt"

func pageCount(n int32, p int32) int32 {
	fromStart := p / 2

	fromEnd := (n / 2) - (p / 2)

	if fromStart < fromEnd {
		return fromStart
	}
	return fromEnd
}

func main() {
	var n, p int32

	_, err := fmt.Scan(&n, &p)
	if err != nil {
		fmt.Println("Помилка зчитування даних:", err)
		return
	}

	result := pageCount(n, p)
	fmt.Println(result)
}