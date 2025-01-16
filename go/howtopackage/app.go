package main

import (
	"convertor"
	"fmt"
)

func main() {
	t := 100.0

	c := convertor.Celsius(t)
	f := convertor.Fahrenheit(t)

	fmt.Printf("%s = %s, %s = %s\n",
		f, convertor.FToC(f), c, convertor.CToF(c))
}
