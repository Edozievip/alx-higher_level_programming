#!/bin/bash
#this script sends a DELETE request to an URL with curl and display the body of the response
curl "$1" -sX DELETE
