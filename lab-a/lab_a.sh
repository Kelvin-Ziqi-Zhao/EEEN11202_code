#!/usr/bin/env sh
first_name="ziqi"
last_name="zhao-5"

echo "Hello. My email address is:"
echo "$first_name.$last_name@student.manchester.ac.uk"

for file in *.txt; do
    if [ -e "$file" ]; then
        mv -- "$file" "ziqi_$file"
    fi
done 