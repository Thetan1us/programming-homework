package main

import (
	"reflect"
	"testing"
)

func TestGradingStudents(t *testing.T) {
	input := []int32{73, 67, 38, 33}
	expected := []int32{75, 67, 40, 33}

	result := gradingStudents(input)

	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Тест провалено! Очікували %v, але отримали %v", expected, result)
	}
}

func TestGradingStudentsEdgeCases(t *testing.T) {
	tests := []struct {
		name     string
		input    []int32
		expected []int32
	}{
		{"Оцінка 29 (не округлюється)", []int32{29}, []int32{29}},
		{"Оцінка 37 (не округлюється)", []int32{37}, []int32{37}},
		{"Оцінка 38 (округлюється до 40)", []int32{38}, []int32{40}},
		{"Оцінка 57 (різниця 3, не округлюється)", []int32{57}, []int32{57}},
		{"Оцінка 84 (округлюється до 85)", []int32{84}, []int32{85}},
		{"Оцінка 100 (кратна 5, не змінюється)", []int32{100}, []int32{100}},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			result := gradingStudents(tc.input)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Errorf("Для тесту '%s' очікували %v, отримали %v", tc.name, tc.expected, result)
			}
		})
	}
}
