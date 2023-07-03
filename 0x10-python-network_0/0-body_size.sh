#!/bin/bash
#this script sends a request to an URL with curl, and displays the size of the body of the response
curl -s "$vip" | wc -c
