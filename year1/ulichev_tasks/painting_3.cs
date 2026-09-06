using System;
using System.Drawing;
using System.Windows.Forms;
namespace WinFormsGraphicsApp
{
public partial class Form1 : Form
{
	public Form1()
	{
		InitializeComponent();
		this.Text = &quot;
		Малюнок&quot;;
		this.Size = new Size(600, 400);
		this.StartPosition = FormStartPosition.CenterScreen;

		this.BackColor = Color.LightSkyBlue;
		this.Paint += new PaintEventHandler(Form1_Paint);
	}
	private void Form1_Paint(object? sender, PaintEventArgs e)
	{
		Graphics g = e.Graphics;
		g.SmoothingMode =
		    System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
		// Сонце
		using (Pen sunPen = new Pen(Color.Gold, 3))
		{
			g.DrawEllipse(sunPen, 450, 40, 60, 60);
		}
		// Земля
		using (Pen groundPen = new Pen(Color.SaddleBrown, 5))
		{
			g.DrawLine(groundPen, 0, 320, 600, 320);
		}
		// Будинок
		using (Pen housePen = new Pen(Color.DarkBlue, 2))
		{
			g.DrawRectangle(housePen, 100, 180, 150, 140);
		}
		// Дах
		using (Pen roofPen = new Pen(Color.Crimson, 4))
		{
			Point[] roofPoints = {
				new Point(80, 180),
				new Point(175, 100),
				new Point(270, 180)
			};

			g.DrawPolygon(roofPen, roofPoints);
		}
	}
}
}