#!/bin/bash
# This script applies basic formatting to C files

for file in "$@"; do
    echo "Fixing $file..."
    sed -i 's/){/){\n/g' "$file"       # Add newline after function braces
    sed -i 's/,/, /g' "$file"          # Ensure spaces after commas
    sed -i 's/\t/    /g' "$file"       # Replace tabs with 4 spaces
    echo "Formatting complete for $file."
done

