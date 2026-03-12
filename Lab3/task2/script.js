// Get DOM elements
const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');
const boxTitle = document.getElementById('boxTitle');
const mainBody = document.getElementById('body');

const viewActiveBtn = document.getElementById('view-active-task');
const viewCompletedBtn = document.getElementById('view-completed-task');

let tasks = JSON.parse(localStorage.getItem('tasks')) || []; // Toggles json synchronizer

function init() {
    renderTasks();
    // Add event listeners
    addBtn.addEventListener('click', addTask);
    taskInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            addTask();
        }
        if(e.key === 'Escape') {
            changeBoxTitle();
        }
    });

    viewActiveBtn.addEventListener('click', () => {
        const activeTasks = tasks.filter(task => !task.completed);
        renderFilteredTasks(activeTasks);
    });
    
    viewCompletedBtn.addEventListener('click', () => {
        const completedTasks = tasks.filter(task => task.completed);
        renderFilteredTasks(completedTasks);
    });
}

function addTask() {
    const taskText = taskInput.value.trim();
    
    // Validate empty input
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }
    
    const task = {
        id: Date.now(),
        text: taskText,
        completed: false
    };
    
    tasks.push(task);
    saveTasks();
    renderTasks();
    
    // Clear input
    taskInput.value = '';
    taskInput.focus();
}

function toggleTask(id) {
    tasks = tasks.map(task => 
        task.id === id ? { ...task, completed: !task.completed } : task
    );
    saveTasks();
    renderTasks();
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    renderTasks();
}

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function renderTasks() {
    taskList.innerHTML = '';
    
    if (tasks.length === 0) {
        taskList.innerHTML = '<div class="empty-message">No tasks yet. Add one above!</div>';
        return;
    }
    
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = `task-item ${task.completed ? 'completed' : ''}`;
        
        li.innerHTML = `
            <input 
                type="checkbox" 
                class="task-checkbox" 
                ${task.completed ? 'checked' : ''}
                onchange="toggleTask(${task.id})"
            />
            <span class="task-text">${task.text}</span>
            <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
        `;
        
        taskList.appendChild(li);
    });
}

function resetTasks() {
    if (confirm('Are you sure you want to reset all tasks?')) {
        tasks = [];
        saveTasks();
        renderTasks();
    }
}

function changeBoxTitle() {
    const newTitle = prompt('Enter new box title:');
    if (newTitle) {
        boxTitle.textContent = newTitle;
    }
}

function renderFilteredTasks(filteredTasks) {
    taskList.innerHTML = '';
    
    if (filteredTasks.length === 0) {
        taskList.innerHTML = '<div class="empty-message">No tasks to display!</div>';
        return;
    }
    
    filteredTasks.forEach(task => {
        const li = document.createElement('li');
        li.className = `task-item ${task.completed ? 'completed' : ''}`;
        
        li.innerHTML = `
            <input 
                type="checkbox"           
                class="task-checkbox" 
                ${task.completed ? 'checked' : ''}
                onchange="toggleTask(${task.id})"
            />
            <span class="task-text">${task.text}</span>
            <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
        `;
        
        taskList.appendChild(li);
    });
}

init();