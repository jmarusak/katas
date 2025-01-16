package main

import (
	"fmt"
	"time"
)

func spinner(delay time.Duration) {
	for {
		for _, r := range `-\|/` {
			fmt.Printf("\r%c", r)
			time.Sleep(delay)
		}
	}
}

func fib(n int) int {
	if n < 2 {
		return n
	}
	return fib(n-1) + fib(n-2)
}

func fib2(n int) int {
	a, b := 0, 1
	for i := 2; i <=n; i++ {
		a, b = b, a+b
	}
	return b
}

func main() {
	go spinner(100 * time.Millisecond)
	fn := fib(42)
	fmt.Printf("\nFibonacci=%d\n", fn)
}
