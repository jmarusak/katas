package main

import (
	"os"
	"fmt"
	"text/template"
)

type Movie struct {
	Title string
	Year int
}

var movies [2]Movie

func main() {
	movies[0] = Movie{"got", 1890}
	movies[1] = Movie{"dev", 1990}

	templ := `
	{{range .}}-----------------------
	{{.Title}} {{.Year}}
	{{end}}-----------------------`

	report, err := template.New("report").Parse(templ)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	if err := report.Execute(os.Stdout, movies); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
