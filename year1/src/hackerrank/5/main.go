package main

import "fmt"

func kangaroo(x1 int32, v1 int32, x2 int32, v2 int32) string {
	if v1 <= v2 {
		return "NO"
	}

	for x1 < x2 {
		x1 += v1
		x2 += v2
	}

	if x1 == x2 {
		return "YES"
	}

	return "NO"
}

func main() {
	var x1, v1, x2, v2 int32

	_, err := fmt.Scanf("%d %d %d %d", &x1, &v1, &x2, &v2)
	if err != nil {
		fmt.Println("Помилка зчитування даних:", err)
		return
	}

	fmt.Println(kangaroo(x1, v1, x2, v2))
}
