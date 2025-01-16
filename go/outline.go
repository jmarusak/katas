package main

import (
	"fmt"
	"net/http"
	"golang.org/x/net/html"
)

var depth int

func main() {
	url := "https://www.gopl.io/reviews.html"
	outline(url)
}

func outline(url string) error {
	resp, err := http.Get(url)
	if err != nil {
		return fmt.Errorf("getting html of %v failed: %v", url, err)
	}
	defer resp.Body.Close()
	
	doc, err := html.Parse(resp.Body)
	if err != nil {
		return fmt.Errorf("parsing html of %v failed: %v", url, err)
	}

	forEachNode(doc, startElement, endElement)
	return nil
}

func forEachNode(n *html.Node, pre, post func(n *html.Node)) {
	if pre != nil {
		pre(n)
	}

	for c := n.FirstChild; c != nil; c = c.NextSibling {
		forEachNode(c, pre, post)
	}

	if post != nil {
		post(n)
	}
}

func startElement(n *html.Node) {
	if n.Type == html.ElementNode {
		fmt.Printf("%*s<%s>\n", depth*2, " ",  n.Data)
		depth++
	}
}

func endElement(n *html.Node) {
	if n.Type == html.ElementNode {
		fmt.Printf("%*s</%s>\n", depth*2, " ",  n.Data)
		depth--
	}
}
