#!/bin/bash

# This script can be used to edit the main message at the top of the email.

# 1st arg. surround in single quotes - ''
new_message=$1

# capture old message (6th line of email_part_2.html)
old_message=`sed '6q;d' email_part_2.html`

# replace old message with new one
sed -i -e s/"${old_message}"/"${new_message}"/g email_part_2.html

# print edited html file
echo HTML file with changes:
cat email_part_2.html
