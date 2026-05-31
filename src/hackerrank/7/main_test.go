package main

import (
	"reflect"
	"testing"
)

func TestBreakingRecords(t *testing.T) {
	tests := []struct {
		name     string
		scores   []int32
		expected []int32
	}{
		{
			name:     "Sample Input 0",
			scores:   []int32{10, 5, 20, 20, 4, 5, 2, 25, 1},
			expected: []int32{2, 4},
		},
		{
			name:     "Sample Input 1",
			scores:   []int32{3, 4, 21, 36, 10, 28, 35, 5, 24, 42},
			expected: []int32{4, 0},
		},
		{
			name:     "Лише одна гра у сезоні",
			scores:   []int32{12},
			expected: []int32{0, 0},
		},
		{
			name:     "Всі ігри з однаковим рахунком",
			scores:   []int32{20, 20, 20, 20},
			expected: []int32{0, 0},
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := breakingRecords(tc.scores)

			// reflect.DeepEqual ідеально порівнює вміст двох слайсів
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("Для тесту '%s' очікували %v, але отримали %v", tc.name, tc.expected, result)
			}
		})
	}
}
