package main

import "testing"

func TestKangaroo_Sample0(t *testing.T) {
	var x1, v1, x2, v2 int32 = 0, 3, 4, 2
	expected := "YES"

	result := kangaroo(x1, v1, x2, v2)

	if result != expected {
		t.Errorf("Тест 0 провалено: очікували %s, отримали %s", expected, result)
	}
}

func TestKangaroo_Sample1(t *testing.T) {
	var x1, v1, x2, v2 int32 = 0, 2, 5, 3
	expected := "NO"

	result := kangaroo(x1, v1, x2, v2)

	if result != expected {
		t.Errorf("Тест 1 провалено: очікували %s, отримали %s", expected, result)
	}
}

func TestKangaroo_TableDriven(t *testing.T) {
	tests := []struct {
		name     string
		x1, v1   int32
		x2, v2   int32
		expected string
	}{
		{
			name: "Однакова швидкість, перший позаду",
			x1:   1, v1: 2,
			x2: 5, v2: 2,
			expected: "NO",
		},
		{
			name: "Перший швидший, але він перестрибне другого (не зустрінуться в одній точці)",
			x1:   0, v1: 3,
			x2: 4, v2: 1,
			expected: "YES",
		},
		{
			name: "Перший швидший, але пролітає повз точку зустрічі",
			x1:   0, v1: 4,
			x2: 4, v2: 1,
			expected: "NO",
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := kangaroo(tc.x1, tc.v1, tc.x2, tc.v2)
			if result != tc.expected {
				t.Errorf("Для сценарію '%s' очікували %s, отримали %s", tc.name, tc.expected, result)
			}
		})
	}
}
