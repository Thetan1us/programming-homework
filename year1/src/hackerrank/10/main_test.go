package main

import "testing"

func TestDiagonalDifference(t *testing.T) {
	tests := []struct {
		name     string
		matrix   [][]int32
		expected int32
	}{
		{
			name: "Sample Input з умови (3x3)",
			matrix: [][]int32{
				{11, 2, 4},
				{4, 5, 6},
				{10, 8, -12},
			},
			expected: 15,
		},
		{
			name: "Example з тексту (3x3)",
			matrix: [][]int32{
				{1, 2, 3},
				{4, 5, 6},
				{9, 8, 9},
			},
			expected: 2,
		},
		{
			name: "Мінімальна матриця 1x1",
			matrix: [][]int32{
				{42},
			},
			expected: 0,
		},
		{
			name: "Матриця 2x2 з від'ємними числами",
			matrix: [][]int32{
				{-1, 4},
				{2, 3},
			},
			expected: 4,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := diagonalDifference(tc.matrix)
			if result != tc.expected {
				t.Errorf("Для '%s' очікували %d, але отримали %d", tc.name, tc.expected, result)
			}
		})
	}
}
