const API_URL = "https://6aebcba7ee39618d7bf887f0.mockapi.io/tasks";

const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");
const totalCounter = document.getElementById("totalCounter");
const activeCounter = document.getElementById("activeCounter");
const clearCompletedBtn = document.getElementById("clearCompletedBtn");
const filterBtns = document.querySelectorAll(".filter-btn");
const loadingIndicator = document.getElementById("loadingIndicator");
const errorMessage = document.getElementById("errorMessage");

let tasks = [];
let currentFilter = "all";

// Керування індикатором завантаження
function setLoading(isLoading) {
  if (loadingIndicator) {
    loadingIndicator.style.display = isLoading ? "block" : "none";
  }
}

// Виведення повідомлення про помилку
function showError(message) {
  if (errorMessage) {
    if (message) {
      errorMessage.textContent = message;
      errorMessage.style.display = "block";
    } else {
      errorMessage.textContent = "";
      errorMessage.style.display = "none";
    }
  } else if (message) {
    console.error("API Error:", message);
  }
}

// Оновлення лічильників
function updateCounters() {
  if (totalCounter) {
    totalCounter.textContent = `Усього: ${tasks.length}`;
  }
  if (activeCounter) {
    const activeCount = tasks.filter((task) => !task.state).length;
    activeCounter.textContent = `Не виконано: ${activeCount}`;
  }
}

// Відображення списку в DOM
function renderTasks() {
  if (!taskList) {
    console.error("Елемент #taskList не знайдено в HTML!");
    return;
  }

  taskList.innerHTML = "";

  let filteredTasks = tasks;
  if (currentFilter === "active") {
    filteredTasks = tasks.filter((task) => !task.state);
  } else if (currentFilter === "completed") {
    filteredTasks = tasks.filter((task) => task.state);
  }

  filteredTasks.forEach((task) => {
    const li = document.createElement("li");
    if (task.state) {
      li.classList.add("completed");
    }

    const taskContent = document.createElement("div");
    taskContent.className = "task-content";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = Boolean(task.state);
    checkbox.addEventListener("change", () =>
      toggleTaskStatus(task.id, task.state),
    );

    const span = document.createElement("span");
    span.textContent = task.name || "(без назви)";

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

// 1. GET: Отримання завдань
async function fetchTasks() {
  showError(null);
  setLoading(true);

  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error(`Помилка сервера: HTTP ${response.status}`);
    }
    tasks = await response.json();
    console.log("Отримано завдань:", tasks);
    renderTasks();
  } catch (error) {
    console.error("fetchTasks failed:", error);
    showError(`Помилка завантаження: ${error.message}`);
  } finally {
    setLoading(false);
  }
}

// 2. POST: Додавання завдання
async function addTask() {
  if (!taskInput) return;
  const text = taskInput.value.trim();

  if (!text) {
    alert("Будь ласка, введіть текст завдання!");
    return;
  }

  showError(null);
  if (addTaskBtn) addTaskBtn.disabled = true;
  taskInput.disabled = true;

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: text,
        state: false,
      }),
    });

    if (!response.ok) {
      throw new Error(`Не вдалося створити: HTTP ${response.status}`);
    }

    const newTask = await response.json();
    tasks.push(newTask);
    renderTasks();
    taskInput.value = "";
  } catch (error) {
    console.error("addTask failed:", error);
    showError(error.message);
  } finally {
    if (addTaskBtn) addTaskBtn.disabled = false;
    taskInput.disabled = false;
    taskInput.focus();
  }
}

// 3. PUT: Зміна статусу
async function toggleTaskStatus(id, currentState) {
  showError(null);

  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        state: !currentState,
      }),
    });

    if (!response.ok) {
      throw new Error(`Не вдалося оновити: HTTP ${response.status}`);
    }

    const updatedTask = await response.json();
    tasks = tasks.map((t) => (String(t.id) === String(id) ? updatedTask : t));
    renderTasks();
  } catch (error) {
    console.error("toggleTaskStatus failed:", error);
    showError(error.message);
    renderTasks();
  }
}

// 4. DELETE: Видалення одного завдання
async function deleteTask(id) {
  showError(null);

  try {
    const response = await fetch(`${API_URL}/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error(`Не вдалося видалити: HTTP ${response.status}`);
    }

    tasks = tasks.filter((t) => String(t.id) !== String(id));
    renderTasks();
  } catch (error) {
    console.error("deleteTask failed:", error);
    showError(error.message);
  }
}

// Очищення виконаних
async function clearCompleted() {
  const completedTasks = tasks.filter((t) => t.state);
  if (completedTasks.length === 0) return;

  showError(null);
  if (clearCompletedBtn) clearCompletedBtn.disabled = true;

  try {
    const deletePromises = completedTasks.map((t) =>
      fetch(`${API_URL}/${t.id}`, { method: "DELETE" }),
    );

    const responses = await Promise.all(deletePromises);
    const hasError = responses.some((res) => !res.ok);

    if (hasError) {
      throw new Error("Частину завдань не вдалося видалити з сервера");
    }

    tasks = tasks.filter((t) => !t.state);
    renderTasks();
  } catch (error) {
    console.error("clearCompleted failed:", error);
    showError(error.message);
  } finally {
    if (clearCompletedBtn) clearCompletedBtn.disabled = false;
  }
}

// Фільтри
function setFilter(e) {
  filterBtns.forEach((btn) => btn.classList.remove("active"));
  e.target.classList.add("active");
  currentFilter = e.target.getAttribute("data-filter") || "all";
  renderTasks();
}

// Прив'язка подій з перевіркою
if (addTaskBtn) {
  addTaskBtn.addEventListener("click", addTask);
}
if (clearCompletedBtn) {
  clearCompletedBtn.addEventListener("click", clearCompleted);
}
if (taskInput) {
  taskInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") addTask();
  });
}
filterBtns.forEach((btn) => {
  btn.addEventListener("click", setFilter);
});

// Запуск при завантаженні сторінки
fetchTasks();
