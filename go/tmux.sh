#!/bin/bash

# Start a new tmux session
tmux new-session -d -s katas

# Split the window into two horizontal panes with top pane twice as big
tmux split-window -v -p 24 

# Select the top pane
tmux select-pane -t 0

# Send a command to the top pane (optional)
tmux send-keys "vi $1" C-m

# Select the bottom pane
tmux select-pane -t 1

# Send a command to the bottom pane (optional)
tmux send-keys "./watcher.sh $1" C-m

# Attach to the tmux session
tmux attach-session -t katas
