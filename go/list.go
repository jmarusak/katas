package main

import "fmt"

type List struct {
	Value int
	Tail *List
}

func (list *List) Sum() int {
	if list == nil {
		return 0
	}
	return list.Value + list.Tail.Sum()
}

func main() {
	l := List{1, &List{2, nil}}
	fmt.Printf("%v\n", l)
	fmt.Println(l.Sum())
}
