package main

import (
	"os"
	"log"
	"html/template"
)

type Movie struct {
	Title string
	Year int
}

var movies [2]Movie

var html = `
<table>
<tr>
<th>Title</th>
<th>Year</th>
</tr>
{{range .}}
<tr>
<td>{{.Title}}</td>
<td>{{.Year}}</td>
</tr>
{{end}}
</table>`

func main() {
	movies[0] = Movie{"got", 1890}
	movies[1] = Movie{"dev", 1990}

	report := template.Must(template.New("report").Parse(html))
	if err := report.Execute(os.Stdout, movies); err != nil {
		log.Fatal(err)
	}
}
