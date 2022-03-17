#!/bin/bash
# Displays all HTTP methods the server will accept.
curl --request OPTIONS "$1"
