package main

import "testing"

func TestPageCount(t *testing.T) {
	tests := []struct {
		name     string
		n        int32
		p        int32
		expected int32
	}{
		{
			name:     "Sample Input 0 (n=6, p=2)",
			n:        6,
			p:        2,
			expected: 1,
		},
		{
			name:     "Sample Input 1 (n=5, p=4)",
			n:        5,
			p:        4,
			expected: 0,
		},
		{
			name:     "Example з тексту (n=5, p=3)",
			n:        5,
			p:        3,
			expected: 1,
		},
		{
			name:     "Цільова сторінка — перша (p=1)",
			n:        10,
			p:        1,
			expected: 0,
		},
		{
			name:     "Книга з парною кількістю сторінок, ціль в кінці (n=6, p=5)",
			n:        6,
			p:        5,
			expected: 1,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := pageCount(tc.n, tc.p)
			if result != tc.expected {
				t.Errorf("Для '%s' очікували %d, але отримали %d", tc.name, tc.expected, result)
			}
		})
	}
}