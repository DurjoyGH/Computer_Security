import hashlib

def calculate_sha512(file_path):
    sha512 = hashlib.sha512()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            sha512.update(block)
    return sha512.hexdigest()

# Target file
original_file = "original.docx"
original_hash = calculate_sha512(original_file)

# Save to file
with open("original_hash.txt", "w") as f:
    f.write(original_hash)

print("SHA-512 hash saved to original_hash.txt")
print("Hash:", original_hash)
