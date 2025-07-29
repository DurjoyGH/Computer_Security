import hashlib

def calculate_sha512(file_path):
    sha512 = hashlib.sha512()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            sha512.update(block)
    return sha512.hexdigest()

file1 = "original.docx"
file2 = "original_copy.docx"

hash1 = calculate_sha512(file1)
hash2 = calculate_sha512(file2)

with open("file1_hash.txt", "w") as f:
    f.write(hash1)

with open("file2_hash.txt", "w") as f:
    f.write(hash2)

print("SHA-512 hash for file1 saved to file1_hash.txt")
print("SHA-512 hash for file2 saved to file2_hash.txt")
print("Hash of file1:", hash1)
print("Hash of file2:", hash2)

if hash1 == hash2:
    print("The files are identical.")
else:
    print("The files are different.")
