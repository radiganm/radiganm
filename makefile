#!/usr/bin/make -sf
## makefile
## Mac Radigan
##
## Copyright 2016 Mac Radigan
## All Rights Reserved

.PHONY: publish clean init
.DEFAULT_GOAL := all

all: publish

root     = ../dox
output   = ./content
template = ./template
include  = ./include

clean:
	rm -Rf $(output)

publish: init
	env PYTHONPATH=$(root)/library       \
	  python3 $(root)/dox.py             \
	    -v                               \
	    -f                               \
	    -e                               \
	    -g ./generator/pi.py             \
	    -I $(include)                    \
	    -t $(template)                   \
	    -o $(output)

init:
	mkdir -p $(output)

## *EOF*
