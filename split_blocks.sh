#!/bin/bash

# Directory containing the large block files
input_dir="tartxt/grouped_blocks_10k"
output_dir="tartxt/grouped_blocks_50MB"

mkdir -p $output_dir

for file in "$input_dir"/*.txt; do
    base_name=$(basename "$file" .txt)
    split -b 49M -d --additional-suffix=.txt "$file" "$output_dir/${base_name}_part"
done

echo "✅ Files have been split into 50MB chunks in $output_dir"
