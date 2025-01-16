package main

import (
	"fmt"
	"math/rand"
)

type tree struct {
	value int
	left *tree
	right *tree
}

func Sort(values []int) {
	var root *tree
	for _, v := range values {
		root = add(root, v)
	}
	traverse(root, values[:0])
}

func add(t *tree, value int) *tree {
	if t == nil {
		t = new(tree)
		t.value = value
		return t
	}

	if value < t.value {
		t.left = add(t.left, value)
	} else {
		t.right = add(t.right, value)
	}
	return t
}

func traverse(t *tree, values []int) []int {
	if t != nil {
		values = traverse(t.left, values)
		values = append(values, t.value)
		values = traverse(t.right, values)
	}
	return values
}

func main() {
	data := make([]int, 10)
	for i := range data {
		data[i] = rand.Int() % 10
	}

	fmt.Println(data)
	Sort(data)
	fmt.Println(data)
}
