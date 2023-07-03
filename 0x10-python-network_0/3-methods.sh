#!/bin/bash
#this script Displays all HTTP methods server will accept
curl "$1" -sI | grep -i "Allow" | cut -d " " -f 2-
