#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double a, b, c;
    cout << "Введіть коефіцієнти a: ";
    cin >> a;     // Передача введених даних в змінну a
    cout << "Введіть коефіцієнти b: ";
    cin >> b;     // Передача введених даних в змінну b
    cout << "Введіть коефіцієнти c: ";
    cin >> c;     // Передача введених даних в змінну c

    // Перевірка на випадок лінійного рівняння
    if (a == 0) {
        if (b == 0) {
            if (c == 0) {
                cout << "Безліч коренів" << endl;
            } else {
                cout << "Коренів немає" << endl;
            }
        } else {
            double x = -c / b;
            cout << "Рівняння лінійне, один корінь: x = " << x << endl;
        }
        return 0;
    }

    double discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        double x1 = (-b + sqrt(discriminant)) / (2 * a);
        double x2 = (-b - sqrt(discriminant)) / (2 * a);
        cout << "Два корені:" << endl;
        cout << "x1 = " << x1 << endl;
        cout << "x2 = " << x2 << endl;
    } else if (discriminant == 0) {
        double x = -b / (2 * a);
        cout << "Один корінь (кратний): x = " << x << endl;
    } else {
        cout << "Дійсних коренів немає" << endl;
    }

    return 0;
}