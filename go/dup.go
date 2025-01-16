package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counters := make(map[string]int)
	inputs := bufio.NewScanner(os.Stdin)
	for inputs.Scan() {
		line := inputs.Text()
		counters[line]++
	}
	for key, value := range counters {
		fmt.Printf("%d: %s\n", value, key)
	}
}
