import { TodoItem } from "./todoItem.js";
import { TodoCollectionJson } from "./todoCollectionJson.js";
import { select } from "@inquirer/prompts";
import { input } from "@inquirer/prompts";

const todos = [
  new TodoItem(1, "Collect Tickets"),
  new TodoItem(2, "Call Laura")
];

const collection: TodoCollectionJson = new TodoCollectionJson(todos);
collection.markComplete(2, true);

function displayTodoList(): void {
  console.clear();
  console.log();
  console.log(`Todo List ` + `(${ collection.getItemCounts().incomplete } item to do):`);
  collection.getTodoItems(true).forEach(item => item.printDetail());
  console.log();
}

async function promptAddTask() {
  const task = await input({ message: "Task title:" });
  collection.addTodo(task);
}

async function promptCompleteTask() {
  const taskId = await input({ message: "Task ID:" });
  const id = parseInt(taskId);
  collection.markComplete(id, true);
}

async function main() {
  displayTodoList();

  const action = await select({
    message: "What do you want to do?",
    choices: [
      { name: "Add a task", value: "add" },
      { name: "Complete a task", value: "complete" },
      { name: "Delete a task", value: "delete" },
      { name: "Quit", value: "quit" }
    ]
  });

  switch (action) {
    case "add":
      await promptAddTask();
      break;
    case "complete":
      await promptCompleteTask();
      break;
    case "delete":
      // Logic to add a new todo
      break;
    case "quit":
      console.log("Goodbye!");
      return;
  }

  await main();
}

main();
