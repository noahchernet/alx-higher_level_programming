#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -s --request OPTIONS "$1"
