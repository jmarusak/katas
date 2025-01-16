package main

import (
	"flag"
	"fmt"
)

type Celsius int

func (c Celsius) String() string {
	return fmt.Sprintf("%vC", int(c))
}

func (c *Celsius) Set(s string) error {
	var value int
	var unit string
	fmt.Sscanf(s, "%d%s", &value, &unit)
	if unit == "C" {
		*c = Celsius(value)
		return nil
	}
	return fmt.Errorf("invalid temperature %q", s)
}

func main() {
	// checking if Celsius satisfies flag.Value interface
	var _ flag.Value = new(Celsius)

	var temp = Celsius(55)
	flag.Var(&temp, "temp", "temperature")
	flag.Parse()
	fmt.Println(temp)

}
