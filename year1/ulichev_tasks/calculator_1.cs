using System;
using System.Windows.Forms;

namespace Calc_AOP1
{
public partial class Form1 : Form
{
	public Form1()
	{
		// Ініціалізація всіх компонентів інтерфейсу
		InitializeComponent();
	}

	private void Calculate(string operation)
	{
		// Перевірка на неправильний ввід
		if (!double.TryParse(txtInput1.Text, out double a) || !double.TryParse(txtInput2.Text, out double b))
		{
			MessageBox.Show("Введіть коректні числа!");
			return;
		}

		// Власне логіка калькулятора
		double result = 0;
		switch (operation)
		{
		case "+":
			result = a + b;
			break;
		case "-":
			result = a - b;
			break;
		case "*":
			result = a * b;
			break;
		case "/":
			if (b != 0) result = a / b;
			else {
				MessageBox.Show("Ділення на 0!");
				return;
			}
			break;
		}
		// Виведення результату обчислень
		txtResult.Text = result.ToString();
	}
	// Event handlers для кнопок інтерфейса, дозволяють викликати Calculate з відповідним аргументом
	private void btnPlus_Click(object sender, EventArgs e) => Calculate("+");
	private void btnMinus_Click(object sender, EventArgs e) => Calculate("-");
	private void btnMult_Click(object sender, EventArgs e) => Calculate("*");
	private void btnDiv_Click(object sender, EventArgs e) => Calculate("/");
}
}
