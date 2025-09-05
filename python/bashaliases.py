#!/usr/bin/env python3

import os

# Define the base directory
base_dir = os.path.expanduser('~/repos')

# Collect all subdirectories inside base_dir
subdirs = [name for name in os.listdir(base_dir)
           if os.path.isdir(os.path.join(base_dir, name))]

# Create alias commands
aliases = [f"alias {name}='cd ~/repos/{name}/'" for name in subdirs]
aliases.sort()

# Print each alias (or write to a file if preferred)
for alias in aliases:
    print(alias)
