#!/bin/bash
#this script Sends GET request with header variable, displays body of response
curl "$1" -sX GET -H "X-School-User-Id: 98"
