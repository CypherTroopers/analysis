import os
import tarfile
import shutil

# 1. Create the /tar directory and extract the archive
tar_file = "block_data.tar"
extract_dir = "tartxt"

if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

# Extract the tar file
with tarfile.open(tar_file, "r") as tar:
    tar.extractall(path=extract_dir)

# 2. Group blocks into sets of 50,000
block_dir = os.path.join(extract_dir, "block_data")
output_dir = os.path.join(extract_dir, "grouped_blocks")
os.makedirs(output_dir, exist_ok=True)

block_size = 50000
counter = 1
group_index = 1
output_file = None

# Ensure the block files are sorted numerically
block_files = sorted(os.listdir(block_dir), key=lambda x: int(x.split("_")[1].split(".")[0]))

for file in block_files:
    file_path = os.path.join(block_dir, file)

    # Create a new group file for each batch of 50,000 blocks
    if (counter - 1) % block_size == 0:
        if output_file:
            output_file.close()
        output_file_path = os.path.join(output_dir, f"blocks_{counter}-{counter + block_size - 1}.txt")
        print(f"Creating: {output_file_path}")
        output_file = open(output_file_path, "w")

    # Append block data to the current group file
    with open(file_path, "r") as f:
        output_file.write(f.read())

    counter += 1

# Close the last opened output file
if output_file:
    output_file.close()

print("Grouping complete. Check the /tar/grouped_blocks directory.")
