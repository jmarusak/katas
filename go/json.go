package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type Movie struct {
	Title string
	Year  int
}

func main() {
	movies := []Movie{
		{"Godfather", 1978},
		{"Matrix", 1980},
	}
	b, err := json.Marshal(movies)
	if err != nil {
		log.Fatalf("JSON marshalling failed: %s", err)
	}
	fmt.Printf("%[1]p : %#[1]s\n", b)
}
