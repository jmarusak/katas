export class TodoItem {

  constructor(public id: number,
              public task: string,
              public complete: boolean = false) {
  }

  public printDetail(): void {
    console.log(`${this.id}. ${this.task} ${this.complete ? "✅" : ""}`);
  }
}
