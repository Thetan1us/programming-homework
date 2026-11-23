const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");
const totalCounter = document.getElementById("totalCounter");
const activeCounter = document.getElementById("activeCounter");
const clearCompletedBtn = document.getElementById("clearCompletedBtn");
const filterBtns = document.querySelectorAll(".filter-btn");

let tasks = [];
let currentFilter = "all";

async function loadTasks() {
  const res = await fetch("/api/tasks");
  tasks = await res.json();
  renderTasks();
}

function updateCounters() {
  totalCounter.textContent = `Усього: ${tasks.length}`;
  const activeCount = tasks.filter((task) => !task.completed).length;
  activeCounter.textContent = `Не виконано: ${activeCount}`;
}

function renderTasks() {
  taskList.innerHTML = "";

  let filteredTasks = tasks;
  if (currentFilter === "active") {
    filteredTasks = tasks.filter((task) => !task.completed);
  } else if (currentFilter === "completed") {
    filteredTasks = tasks.filter((task) => task.completed);
  }

  filteredTasks.forEach((task) => {
    const li = document.createElement("li");
    if (task.completed) {
      li.classList.add("completed");
    }

    const taskContent = document.createElement("div");
    taskContent.className = "task-content";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.addEventListener("change", () => toggleTaskStatus(task.id));

    const span = document.createElement("span");
    span.textContent = task.title;

    taskContent.appendChild(checkbox);
    taskContent.appendChild(span);

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Видалити";
    deleteBtn.className = "delete-btn";
    deleteBtn.addEventListener("click", () => deleteTask(task.id));

    li.appendChild(taskContent);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
  });

  updateCounters();
}

async function addTask() {
  const title = taskInput.value.trim();
  if (!title) {
    alert("Будь ласка, введіть текст завдання!");
    return;
  }

  const res = await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });

  if (!res.ok) {
    alert("Не вдалося додати завдання");
    return;
  }

  const created = await res.json();
  tasks.unshift(created);
  taskInput.value = "";
  renderTasks();
}

async function toggleTaskStatus(id) {
  const res = await fetch(`/api/tasks/${id}`, {
    method: "PATCH",
  });

  if (!res.ok) return;

  const updated = await res.json();
  tasks = tasks.map((task) => (task.id === id ? updated : task));
  renderTasks();
}

async function deleteTask(id) {
  const res = await fetch(`/api/tasks/${id}`, {
    method: "DELETE",
  });

  if (!res.ok) return;

  tasks = tasks.filter((task) => task.id !== id);
  renderTasks();
}

async function clearCompleted() {
  const completedTasks = tasks.filter((task) => task.completed);
  for (const task of completedTasks) {
    await fetch(`/api/tasks/${task.id}`, { method: "DELETE" });
  }
  tasks = tasks.filter((task) => !task.completed);
  renderTasks();
}

function setFilter(e) {
  filterBtns.forEach((btn) => btn.classList.remove("active"));
  e.target.classList.add("active");
  currentFilter = e.target.getAttribute("data-filter");
  renderTasks();
}

addTaskBtn.addEventListener("click", addTask);
taskInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") addTask();
});
clearCompletedBtn.addEventListener("click", clearCompleted);

filterBtns.forEach((btn) => {
  btn.addEventListener("click", setFilter);
});

loadTasks();
