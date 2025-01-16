// Can't compare slicex except to nil, here ix adhoc function to compare
package main

import "fmt"

func equal(x []int, y []int) bool {
	if len(x) != len(y) {
		return false
	}
	for i := range x {
		if x[i] != y[i] {
			return false
		}
	}
	return true
}

func main() {
	x := []int{1, 2, 3}
	y := []int{1, 2, 4}

	fmt.Println(equal(x, y))
}
