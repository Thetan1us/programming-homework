package main

import "testing"

func TestSockMerchant(t *testing.T) {
	tests := []struct {
		name     string
		n        int32
		ar       []int32
		expected int32
	}{
		{
			name:     "Sample Input з умови (9 шкарпеток)",
			n:        9,
			ar:       []int32{10, 20, 20, 10, 10, 30, 50, 10, 20},
			expected: 3, // дві пари кольору 10, одна пара кольору 20
		},
		{
			name:     "Example з тексту (7 шкарпеток)",
			n:        7,
			ar:       []int32{1, 2, 1, 2, 1, 3, 2},
			expected: 2, // одна пара кольору 1, одна пара кольору 2
		},
		{
			name:     "Усі шкарпетки різних кольорів (0 пар)",
			n:        4,
			ar:       []int32{1, 2, 3, 4},
			expected: 0,
		},
		{
			name:     "Усі шкарпетки одного кольору",
			n:        5,
			ar:       []int32{42, 42, 42, 42, 42},
			expected: 2, // 5 / 2 = 2 пари
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := sockMerchant(tc.n, tc.ar)
			if result != tc.expected {
				t.Errorf("Для '%s' очікували %d пар, але отримали %d", tc.name, tc.expected, result)
			}
		})
	}
}
