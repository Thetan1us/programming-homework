package main

import "testing"

func TestCountFruits(t *testing.T) {
	// Вхідні дані з першого прикладу (Sample Input 0)
	var houseStart, houseEnd int32 = 7, 11
	var a, b int32 = 5, 15
	apples := []int32{-2, 2, 1}
	oranges := []int32{5, -6}

	// Очікуваний результат
	var expectedApples int32 = 1
	var expectedOranges int32 = 1

	// Викликаємо нашу функцію
	gotApples, gotOranges := countFruits(houseStart, houseEnd, a, b, apples, oranges)

	// Перевіряємо яблука
	if gotApples != expectedApples {
		t.Errorf("Помилка з яблуками: очікували %d, отримали %d", expectedApples, gotApples)
	}

	// Перевіряємо апельсини
	if gotOranges != expectedOranges {
		t.Errorf("Помилка з апельсинами: очікували %d, отримали %d", expectedOranges, gotOranges)
	}
}

func TestCountFruits_EdgeCases(t *testing.T) {
	// Додатковий тест: жоден фрукт не потрапляє на будинок
	var houseStart, houseEnd int32 = 10, 20
	var a, b int32 = 5, 25

	// Яблука падають занадто близько, апельсини занадто далеко
	apples := []int32{1, 2, 3}     // координати: 6, 7, 8 (всі < 10)
	oranges := []int32{-1, -2, -3} // координати: 24, 23, 22 (всі > 20)

	gotApples, gotOranges := countFruits(houseStart, houseEnd, a, b, apples, oranges)

	if gotApples != 0 {
		t.Errorf("Очікували 0 яблук, отримали %d", gotApples)
	}
	if gotOranges != 0 {
		t.Errorf("Очікували 0 апельсинів, отримали %d", gotOranges)
	}
}
