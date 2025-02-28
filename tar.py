import leveldb
import tarfile
import os

# Path to the LevelDB database
db_path = "/root/chaindata/"
db = leveldb.LevelDB(db_path)

# Temporary directory to store extracted data
output_dir = "block_data"
os.makedirs(output_dir, exist_ok=True)

# Dictionary to store blocks before writing to files
block_dict = {}

# Extract block data
for key, value in db.RangeIter():
    if key.startswith(b'cypherium-committee-'):
        # Extract the block number part from the key
        block_number_bytes = key[len(b'cypherium-committee-'):len(b'cypherium-committee-')+8]

        # Convert binary to an integer
        block_number = int.from_bytes(block_number_bytes, byteorder='big')

        # Store block data in dictionary
        block_dict[block_number] = value

# Sort the blocks by block number
sorted_blocks = sorted(block_dict.items())

# Save block data in order
for block_number, value in sorted_blocks:
    file_path = os.path.join(output_dir, f"block_{block_number}.txt")
    with open(file_path, "w") as f:
        f.write(f"Block Number: {block_number}\n")
        f.write(f"Value (Binary): {value}\n")
        f.write(f"Value (HEX): {value.hex()}\n")
        f.write("=" * 80 + "\n")

# Compress the files into a `.tar` archive
tar_file = "block_data.tar"
with tarfile.open(tar_file, "w") as tar:
    tar.add(output_dir, arcname=os.path.basename(output_dir))

# Remove the temporary directory
for file in os.listdir(output_dir):
    os.remove(os.path.join(output_dir, file))
os.rmdir(output_dir)

print(f"All block data has been saved to '{tar_file}' in sorted order.")
