#!/bin/bash
#this script Displays all HTTP methods server will accept
curl "$vip" -sI | grep -i "Allow" | cut -d " " -f 2-
