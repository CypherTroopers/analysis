#!/bin/bash

# Define the directory containing the split files
UPLOAD_DIR="tartxt/grouped_blocks_50MB"

# Navigate to the directory
cd "$UPLOAD_DIR"

# Loop through each file in sorted order
for file in $(ls *.txt | sort -V); do
    echo "🚀 Uploading $file..."

    # Add the file to git
    git add "$file"

    # Commit the file
    git commit -m "Added $file"

    # Push the file
    git push origin main

    # Wait to avoid GitHub rate limits
    sleep 5
done

echo "✅ All files uploaded successfully!"
