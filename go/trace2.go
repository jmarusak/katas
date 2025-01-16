package main

import (
	"fmt"
)

func main() {
	double(2)
}

func double(x int) (result int) {
	defer func() { fmt.Printf("double(%d) => %d\n", x, result) }()
	return x + x
}
