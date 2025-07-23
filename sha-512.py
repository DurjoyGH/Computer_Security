import hashlib

def calculate_sha512(file_path):
    sha512_hash = hashlib.sha512()
    with open(file_path, 'rb') as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha512_hash.update(byte_block)
    return sha512_hash.hexdigest()

original_file = "original.docx"
original_hash = calculate_sha512(original_file)
# print("Original File Hash:", original_hash)

received_file = "original_copy.docx"
received_hash = calculate_sha512(received_file)
# print("Received File Hash:", received_hash)

if original_hash == received_hash:
    print("The files are identical. Integrity OK.")
else:
    print("The files are different. Integrity FAILED.")
    
#find a algorithm which do same work as sha512 but different method and not using hashing 