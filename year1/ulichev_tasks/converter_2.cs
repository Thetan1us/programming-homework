using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Encodings.Web;
using System.Text.Json;
using System.Windows.Forms;
namespace UnitConverter_AOP2
{
public partial class Form1 : Form
{

	// Структура для зберігання категорії та її коефіцієнтів відносно
	базової одиниці
	private Dictionary&lt;
	string, Dictionary&lt;
	string, double&gt;
	&gt;
	_categories =
	    new();
	// Шлях до файлу даних (data.json поруч із exe)
	private readonly string _dataFilePath;
	public Form1()
	{
		InitializeComponent();
		_dataFilePath =
		    Path.Combine(AppDomain.CurrentDomain.BaseDirectory, &quot; data.json&quot;);
		LoadData();
		FillCategories();
	}
	// завантаження словників із data.json
	private void LoadData()
	{
		if (!File.Exists(_dataFilePath))
		{
			MessageBox.Show(&quot; Файл data.json не знайдено! Буде створено
			                порожній файл.&quot;,
			                &quot; Увага&quot;, MessageBoxButtons.OK,
			                MessageBoxIcon.Warning);
			_categories = new Dictionary&lt;
			string, Dictionary&lt;
			string, double&gt;
			&gt;
			();
			SaveData();
			return;
		}
		string json = File.ReadAllText(_dataFilePath);
		var loaded = JsonSerializer.Deserialize&lt;
		Dictionary&lt;
		string,
		Dictionary&lt;
		string, double&gt;
		&gt;
		&gt;
		(json);
		_categories = loaded ?? new Dictionary&lt;
		string, Dictionary&lt;
		string,
		double&gt;
		&gt;
		();
	}

	// збереження словників у data.json
	private void SaveData()
	{
		var options = new JsonSerializerOptions
		{
			WriteIndented = true,
			Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping
		};
		string json = JsonSerializer.Serialize(_categories, options);
		File.WriteAllText(_dataFilePath, json);
	}
	private void FillCategories()
	{
		cbCategory.Items.Clear();
		cbCategory.Items.AddRange(_categories.Keys.ToArray());
		if (cbCategory.Items.Count &gt; 0)
			cbCategory.SelectedIndex = 0;
	}
	private void cbCategory_SelectedIndexChanged(object sender, EventArgs
	        e)
	{
		if (cbCategory.SelectedItem == null) return;
		string selectedCat = cbCategory.SelectedItem.ToString()!;
		var units = _categories[selectedCat].Keys.ToArray();
		cbFrom.Items.Clear();
		cbTo.Items.Clear();
		cbFrom.Items.AddRange(units);
		cbTo.Items.AddRange(units);
		if (cbFrom.Items.Count &gt; 0) cbFrom.SelectedIndex = 0;
		if (cbTo.Items.Count &gt; 1) cbTo.SelectedIndex = 1;
		else if (cbTo.Items.Count &gt; 0) cbTo.SelectedIndex = 0;

	}
	private void btnConvert_Click(object sender, EventArgs e)
	{
		// Валідація вводу
		if (!double.TryParse(txtInput.Text, out double value))
		{
			MessageBox.Show(&quot; Будь ласка, введіть числове значення!&quot;,
			                &quot; Помилка валідації&quot;,
			                MessageBoxButtons.OK, MessageBoxIcon.Warning);
			return;
		}
		if (cbCategory.SelectedItem == null || cbFrom.SelectedItem == null ||
		        cbTo.SelectedItem == null)
		{
			MessageBox.Show(&quot; Оберіть категорію та одиниці!&quot;, &quot; Помилка&quot;,
			                MessageBoxButtons.OK, MessageBoxIcon.Warning);
			return;
		}
		string category = cbCategory.SelectedItem.ToString()!;
		string fromUnit = cbFrom.SelectedItem.ToString()!;
		string toUnit = cbTo.SelectedItem.ToString()!;
		// Логіка конвертації:
		// 1. Переводимо в базову одиницю (value * коефіцієнт_з)
		// 2. Переводимо з базової в цільову (/ коефіцієнт_в)
		double baseValue = value * _categories[category][fromUnit];
		double result = baseValue / _categories[category][toUnit];
		lblResult.Text = $&quot;
		{
			value
		} {
			fromUnit
		} = {result:F4} {toUnit}&quot;;
	}
	// ─── Кнопка: Додати нову категорію ───
	private void btnAddCategory_Click(object sender, EventArgs e)
	{

		string? categoryName = PromptDialog(&quot; Нова категорія&quot;,
		                                    &quot; Введіть назву нової категорії\n(наприклад: Температура (база:
		                                            Цельсій)):&quot;);
		if (string.IsNullOrWhiteSpace(categoryName))
			return;
		if (_categories.ContainsKey(categoryName))
		{
			MessageBox.Show(&quot; Така категорія вже існує!&quot;, &quot; Помилка&quot;,
			                MessageBoxButtons.OK, MessageBoxIcon.Warning);
			return;
		}
		// Створюємо категорію з хоча б однією одиницею
		string? unitName = PromptDialog(&quot; Перша одиниця&quot;,
		                                &quot; Введіть назву першої (базової) одиниці для цієї категорії:&quot;);
		if (string.IsNullOrWhiteSpace(unitName))
			return;
		_categories[categoryName] = new Dictionary&lt;
		string, double&gt;
		{
			{
				unitName, 1.0
			} // Базова одиниця завжди має коефіцієнт 1.0
		};
		SaveData();
		FillCategories();
		cbCategory.SelectedItem = categoryName;
		MessageBox.Show($&quot; Категорію \&quot; {
			categoryName
		}\&quot; додано та
		збережено у data.json!&quot;,
		&quot; Успіх&quot;, MessageBoxButtons.OK,
		MessageBoxIcon.Information);
	}
	// ─── Кнопка: Додати нову одиницю до поточної категорії ───

	private void btnAddUnit_Click(object sender, EventArgs e)
	{
		if (cbCategory.SelectedItem == null)
		{
			MessageBox.Show(&quot; Спочатку оберіть категорію!&quot;, &quot; Помилка&quot;,
			                MessageBoxButtons.OK, MessageBoxIcon.Warning);
			return;
		}
		string category = cbCategory.SelectedItem.ToString()!;
		string? unitName = PromptDialog(&quot; Нова одиниця&quot;,
		$&quot; Введіть назву нової одиниці для категорії \&quot; {
			category
		}\&quot; :&quot;);
		if (string.IsNullOrWhiteSpace(unitName))
			return;
		if (_categories[category].ContainsKey(unitName))
		{
			MessageBox.Show(&quot; Така одиниця вже існує в цій категорії!&quot;,
			                &quot; Помилка&quot;,
			                MessageBoxButtons.OK, MessageBoxIcon.Warning);
			return;
		}
		string? coefficientStr = PromptDialog(&quot; Коефіцієнт&quot;,
		$&quot; Введіть коефіцієнт для \&quot; {
			unitName
		}\&quot; відносно базової
		одиниці:\n&quot; +
		&quot; (наприклад, якщо база — Метр, то для Кілометра коефіцієнт =
		            1000)&quot;);
		if (string.IsNullOrWhiteSpace(coefficientStr) ||
		        !double.TryParse(coefficientStr, out double coefficient) ||
		        coefficient &lt; = 0)
		{
			MessageBox.Show(&quot; Будь ласка, введіть коректне додатне число!&quot;,
			                &quot; Помилка&quot;,

			                MessageBoxButtons.OK, MessageBoxIcon.Warning);
			return;
		}
		_categories[category][unitName] = coefficient;
		SaveData();
		// Оновлюємо списки одиниць
		cbCategory_SelectedIndexChanged(sender, e);
		MessageBox.Show($&quot; Одиницю \&quot; {
			unitName
		}\&quot; (коефіцієнт:
		          {
		              coefficient
		          }) додано до \&quot; {
			category
		}\&quot; та збережено у data.json!&quot;,
		&quot; Успіх&quot;, MessageBoxButtons.OK,
		MessageBoxIcon.Information);
	}
	// ─── Допоміжний діалог введення тексту ───
	private static string? PromptDialog(string title, string message)
	{
		Form prompt = new Form()
		{
			Width = 420,
			Height = 200,
			FormBorderStyle = FormBorderStyle.FixedDialog,
			Text = title,
			StartPosition = FormStartPosition.CenterParent,
			MaximizeBox = false,
			MinimizeBox = false
		};
		Label lbl = new Label() {
			Left = 15, Top = 15, Width = 370, Height =
			                                 50, Text = message
		};
		TextBox txt = new TextBox() {
			Left = 15, Top = 70, Width = 370
		};
		Button btnOk = new Button() {
			Text = &quot;
			OK&quot;
			, Left = 210, Width = 80,
			  Top = 110, DialogResult = DialogResult.OK
		};
		Button btnCancel = new Button() {
			Text = &quot;
			Скасувати&quot;
			, Left = 300,
			  Width = 80, Top = 110, DialogResult = DialogResult.Cancel
		};

		prompt.Controls.Add(lbl);
		prompt.Controls.Add(txt);
		prompt.Controls.Add(btnOk);
		prompt.Controls.Add(btnCancel);
		prompt.AcceptButton = btnOk;
		prompt.CancelButton = btnCancel;
		return prompt.ShowDialog() == DialogResult.OK ? txt.Text : null;
	}
}
}