package main

import (
	"fmt"
	"sort"
)

func main() {
	ages := map[string]int{
		"peter": 67,
		"tom": 45,
		"mario": 56,
	}

	var names []string
	for name := range ages{
		names = append(names, name)
	}

	sort.Strings(names)
	for _, name := range names {
		fmt.Printf("%s\t%d\n", name, ages[name])
	}
}
