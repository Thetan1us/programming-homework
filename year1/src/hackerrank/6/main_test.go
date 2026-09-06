package main

import "testing"

func TestGetTotalX(t *testing.T) {
	tests := []struct {
		name     string
		a        []int32
		b        []int32
		expected int32
	}{
		{
			name:     "Приклад 1 з умови (Sample Input)",
			a:        []int32{2, 4},
			b:        []int32{16, 32, 96},
			expected: 3,
		},
		{
			name:     "Приклад 2 з тексту (Example)",
			a:        []int32{2, 6},
			b:        []int32{24, 36},
			expected: 2,
		},
		{
			name:     "Граничний випадок (по 1 елементу)",
			a:        []int32{2},
			b:        []int32{20},
			expected: 4,
		},
		{
			name:     "Жодного числа не підходить",
			a:        []int32{3, 4},
			b:        []int32{24, 30},
			expected: 0,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := getTotalX(tc.a, tc.b)
			if result != tc.expected {
				t.Errorf("Для '%s' очікували %d, отримали %d", tc.name, tc.expected, result)
			}
		})
	}
}
