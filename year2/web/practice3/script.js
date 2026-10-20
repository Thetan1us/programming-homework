// Отримуємо посилання на HTML-елементи
const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");
const totalCounter = document.getElementById("totalCounter");
const activeCounter = document.getElementById("activeCounter");
const clearCompletedBtn = document.getElementById("clearCompletedBtn");
const filterBtns = document.querySelectorAll(".filter-btn");

let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
let currentFilter = "all"; // Початковий фільтр

function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function updateCounters() {
  totalCounter.textContent = `Усього: ${tasks.length}`;
  const activeTasksCount = tasks.filter((task) => !task.completed).length;
  activeCounter.textContent = `Не виконано: ${activeTasksCount}`;
}

function renderTasks() {
  // Очищаємо список перед оновленням
  taskList.innerHTML = "";

  let filteredTasks = tasks;
  if (currentFilter === "active") {
    filteredTasks = tasks.filter((task) => !task.completed);
  } else if (currentFilter === "completed") {
    filteredTasks = tasks.filter((task) => task.completed);
  }

  // Створюємо елементи для кожного завдання
  filteredTasks.forEach((task, index) => {
    const li = document.createElement("li");
    if (task.completed) {
      li.classList.add("completed");
    }

    // Вміст завдання (чекбокс і текст)
    const taskContent = document.createElement("div");
    taskContent.className = "task-content";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    // Зміна статусу при кліку на чекбокс
    checkbox.addEventListener("change", () => toggleTaskStatus(task.id));

    const span = document.createElement("span");
    span.textContent = task.text;

    taskContent.appendChild(checkbox);
    taskContent.appendChild(span);

    // Кнопка видалення
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

function addTask() {
  const text = taskInput.value.trim(); // Забираємо зайві пробіли

  if (text !== "") {
    const newTask = {
      id: Date.now(), // Унікальний ідентифікатор на основі часу
      text: text,
      completed: false,
    };

    tasks.push(newTask);
    saveTasks();
    renderTasks();
    taskInput.value = "";
  } else {
    alert("Будь ласка, введіть текст завдання!");
  }
}

function toggleTaskStatus(id) {
  // Знаходимо завдання за id
  const task = tasks.find((t) => t.id === id);
  if (task) {
    task.completed = !task.completed;
    saveTasks();
    renderTasks();
  }
}

function deleteTask(id) {
  tasks = tasks.filter((task) => task.id !== id);
  saveTasks();
  renderTasks();
}

function clearCompleted() {
  tasks = tasks.filter((task) => !task.completed);
  saveTasks();
  renderTasks();
}

// Зміна активного фільтра
function setFilter(e) {
  // Забираємо клас active у всіх кнопок і додаємо натиснутій
  filterBtns.forEach((btn) => btn.classList.remove("active"));
  e.target.classList.add("active");

  // Отримуємо значення фільтра з data-атрибута HTML
  currentFilter = e.target.getAttribute("data-filter");
  renderTasks();
}

addTaskBtn.addEventListener("click", addTask);
clearCompletedBtn.addEventListener("click", clearCompleted);

filterBtns.forEach((btn) => {
  btn.addEventListener("click", setFilter);
});

renderTasks();
