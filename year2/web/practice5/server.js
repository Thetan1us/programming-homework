const path = require("path");
const express = require("express");
const Database = require("better-sqlite3");

const app = express();
const PORT = 3000;

const db = new Database("tasks.db");

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0
  )
`);

app.use(express.json());
app.use(express.static(path.join(__dirname, "app")));

app.get("/api/tasks", (req, res) => {
  const rows = db.prepare("SELECT * FROM tasks ORDER BY id DESC").all();
  res.json(
    rows.map((row) => ({
      id: row.id,
      title: row.title,
      completed: Boolean(row.completed),
    })),
  );
});

app.post("/api/tasks", (req, res) => {
  const title = req.body.title.trim();
  if (!title) {
    return res.status(400).json({ error: "Порожня назва" });
  }

  const info = db
    .prepare("INSERT INTO tasks (title, completed) VALUES (?, 0)")
    .run(title);

  res.status(201).json({
    id: info.lastInsertRowid,
    title,
    completed: false,
  });
});

app.patch("/api/tasks/:id", (req, res) => {
  const id = req.params.id;
  const task = db.prepare("SELECT * FROM tasks WHERE id = ?").get(id);
  if (!task) {
    return res.status(404).json({ error: "Не знайдено" });
  }

  const nextCompleted = task.completed ? 0 : 1;
  db.prepare("UPDATE tasks SET completed = ? WHERE id = ?").run(
    nextCompleted,
    id,
  );

  res.json({
    id: task.id,
    title: task.title,
    completed: Boolean(nextCompleted),
  });
});

app.delete("/api/tasks/:id", (req, res) => {
  db.prepare("DELETE FROM tasks WHERE id = ?").run(req.params.id);
  res.json({ ok: true });
});

app.listen(PORT, () => {
  console.log(`Сервер запущено: http://localhost:${PORT}`);
});
