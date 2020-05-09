#!/bin/bash

# 1st arg. surround in single quotes - ''
new_message=$1

# capture old message (6th line of email_part_2.html)
old_message=`sed '6q;d' email_part_2.html`

# replace old message with new one
sed -i -e s/"${old_message}"/"${new_message}"/g email_part_2.html
