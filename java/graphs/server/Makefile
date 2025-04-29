# Makefile for a Maven Java Project

# Variables
MVN=mvn
APP_NAME=graphs-1.0
JAR_FILE=target/$(APP_NAME).jar

# Default target
.PHONY: all
all: clean build

# Clean target
.PHONY: clean
clean:
	$(MVN) clean

# Compile source code 
.PHONY: comp 
comp:
	$(MVN) compile 

# Build target
.PHONY: build
build:
	$(MVN) package

# Run target
.PHONY: run
run:
	$(MVN) exec:java

# Test target
.PHONY: test
test:
	$(MVN) test

# Install target (install into local Maven repository)
.PHONY: install
install:
	$(MVN) install

# Lint target (if using a linter plugin)
.PHONY: lint
lint:
	$(MVN) checkstyle:check

# Dependency tree
.PHONY: deps
deps:
	$(MVN) dependency:tree

# Help
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make all       - Clean and build the project"
	@echo "  make clean     - Clean the project"
	@echo "  make comp      - Compile the source code"
	@echo "  make build     - Build the project"
	@echo "  make run       - Run the application"
	@echo "  make test      - Run tests"
	@echo "  make install   - Install the project to local Maven repo"
	@echo "  make lint      - Run code style checks"
	@echo "  make deps      - Show dependency tree"
