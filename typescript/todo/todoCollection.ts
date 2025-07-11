import { TodoItem } from "./todoItem.js";

type ItemCounts = {
  total: number,
  incomplete: number
};

export class TodoCollection {
  private nextId: number = 1;
  protected itemMap = new Map<number, TodoItem>();

  constructor( public todoItems: TodoItem[] = []) {
    todoItems.forEach(item => this.itemMap.set(item.id, item));
  }

  addTodo(task: string): number {
    while (this.getTodoItemById(this.nextId)) {
      this.nextId++;
    }
    this.itemMap.set(this.nextId, new TodoItem(this.nextId, task));
    return this.nextId;
  }

  getTodoItemById(id: number): TodoItem {
    return this.itemMap.get(id);
  }

  getTodoItems(includeComplete: boolean): TodoItem[] {
    return [...this.itemMap.values()].filter(item => includeComplete || !item.complete);
  }

  markComplete(id: number, complete: boolean): void {
    const todoItem = this.getTodoItemById(id);
    if (todoItem) {
      todoItem.complete = complete;
    }
  }

  removeComplete(): void {
    this.itemMap.forEach(item => {
      if (item.complete) {
        this.itemMap.delete(item.id);
      }
    });
  }

  getItemCounts(): ItemCounts {
    return {
      total: this.itemMap.size,
      incomplete: this.getTodoItems(false).length
    };
  }
}
