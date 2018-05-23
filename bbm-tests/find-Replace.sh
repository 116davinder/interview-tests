#!/bin/bash

# 1. Find all 'foo' in given dir
# 2. Replace 'foo' with 'bar'

# variable
given_dir=/tmp

# 1. Solution using shell
grep -rni 'foo' $given_dir

# 2. Replace word with given word
find $given_dir -type f -exec sed -i 's/foo/bar/g' {} \;