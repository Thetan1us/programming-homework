package main

import "testing"

func TestMigratoryBirds(t *testing.T) {
	tests := []struct {
		name     string
		arr      []int32
		expected int32
	}{
		{
			name:     "Sample Input 0: чіткий переможець ID 4",
			arr:      []int32{1, 4, 4, 4, 5, 3},
			expected: 4,
		},
		{
			name:     "Sample Input 1: нічия між 3 та 4, обираємо найменший ID (3)",
			arr:      []int32{1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4},
			expected: 3,
		},
		{
			name:     "Example з тексту: нічия між 1 та 2, обираємо 1",
			arr:      []int32{1, 1, 2, 2, 3},
			expected: 1,
		},
		{
			name:     "Всі птахи одного виду",
			arr:      []int32{5, 5, 5, 5},
			expected: 5,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := migratoryBirds(tc.arr)
			if result != tc.expected {
				t.Errorf("Для '%s' очікували %d, але отримали %d", tc.name, tc.expected, result)
			}
		})
	}
}
