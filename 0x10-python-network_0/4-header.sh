#!/bin/bash
#this script Sends GET request with header variable, displays body of response
curl "$vip" -sX GET -H "X-School-User-Id: 98"
