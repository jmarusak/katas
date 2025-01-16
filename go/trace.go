package main

import (
	"log"
	"time"
)

func main() {
	slow()
}

func slow() {
	defer trace("slow()")()
	time.Sleep(2 * time.Second)
}

func trace(msg string) func() {
	start := time.Now()
	log.Printf("enter %s function", msg)
	return func() {
		log.Printf("exit %s function, duration %s", msg, time.Since(start))
	}
}
