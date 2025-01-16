#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Error: No filename provided."
    echo "Usage: $0 <filename>"
    exit 1
fi

FILE_TO_WATCH="$1"
COMMAND="go run $FILE_TO_WATCH"

echo "Watching $FILE_TO_WATCH for changes..."

while true; do
    inotifywait -e modify $FILE_TO_WATCH
    if [ $? -eq 1 ]; then
        echo ""
        $COMMAND
	echo ""
    fi
done
