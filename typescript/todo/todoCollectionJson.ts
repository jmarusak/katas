import { TodoItem } from './todoItem.js';
import { TodoCollection } from './todoCollection.js';
import { LowSync } from 'lowdb';
import { JSONFileSync } from 'lowdb/node';

type schemaType = {
  tasks: { id: number; task: string; complete: boolean; }[]
};

export class TodoCollectionJson extends TodoCollection {
  private database: LowSync<schemaType>

  constructor(todoItems: TodoItem[] = []) {
    super([]);
    this.database = new LowSync(new JSONFileSync("tododb.json"), { tasks: todoItems });
    this.database.read();

    if (this.database.data == null) {
      this.database.data = { tasks: todoItems };
      this.database.write();
      todoItems.forEach(item => this.itemMap.set(item.id, item));
    } else {
      this.database.data.tasks.forEach(item =>
        this.itemMap.set(item.id, new TodoItem(item.id, item.task, item.complete)));
    }
  }

  addTodo(task: string): number {
    const taskId = super.addTodo(task);
    this.storeTasks();
    return taskId;
  }

  private storeTasks() {
    this.database.data.tasks = [...this.itemMap.values()];
    this.database.write();
  }
}
