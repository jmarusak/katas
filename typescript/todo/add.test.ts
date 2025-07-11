// src/add.test.ts
function add(a: number, b: number): number {
  return a + b;
}

describe('add function', () => {
  test('should add two numbers correctly', () => {
    expect(add(1, 2)).toBe(3);
  });

  test('should handle negative numbers', () => {
    expect(add(-1, 5)).toBe(4);
  });
});
