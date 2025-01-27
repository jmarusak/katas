package main

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"os"
	"strings"

	"cloud.google.com/go/vertexai/genai"
)

func generateContentFromText(w io.Writer, projectID string, question string) error {
	location := "us-central1"
	modelName := "gemini-2.0-flash-exp"
	ctx := context.Background()

	client, err := genai.NewClient(ctx, projectID, location)
	if err != nil {
		return fmt.Errorf("error creating client: %w", err)
	}
	gemini := client.GenerativeModel(modelName)
	prompt := genai.Text(question)

	resp, err := gemini.GenerateContent(ctx, prompt)
	if err != nil {
		return fmt.Errorf("error generating content: %w", err)
	}

	// Extract the response from the API response
	var response bytes.Buffer
	for _, cand := range resp.Candidates {
		if cand.Content != nil {
			for _, part := range cand.Content.Parts {
				if txt, ok := part.(genai.Text); ok {
					response.WriteString(string(txt))
				}
			}
		}
	}

	fmt.Fprintln(w, response.String())
	return nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a question in single quotes as argument.")
		return
	}
	// Remove leading and trailing single quotes and join args
	question := strings.Trim(strings.Join(os.Args[1:], " "), "'")

	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
	if projectID == "" {
		fmt.Println("GOOGLE_CLOUD_PROJECT environment variable is not set")
		return
	}

	if err := generateContentFromText(os.Stdout, projectID, question); err != nil {
		fmt.Printf("Error generating content: %v\n", err)
		return
	}
}
