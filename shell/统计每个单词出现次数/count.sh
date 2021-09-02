#!/bin/bash

cat words.txt | xargs -n1 | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'