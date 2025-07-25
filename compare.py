import hashlib

def calculate_sha512(file_path):
    sha512 = hashlib.sha512()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            sha512.update(block)
    return sha512.hexdigest()

# File to check now
file_to_check = "original.docx"
current_hash = calculate_sha512(file_to_check)

# Load saved hash
with open("original_hash.txt", "r") as f:
    saved_hash = f.read().strip()

# Compare hashes
print("Saved   SHA-512:", saved_hash)
print("Current SHA-512:", current_hash)

if saved_hash == current_hash:
    print("The file is unchanged. Integrity OK.")
else:
    print("The file has been modified. Integrity FAILED.")
