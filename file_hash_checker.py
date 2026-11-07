
import hashlib
import os

def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return "Error: File not found."


filename = input("Enter file path: ")

if os.path.isfile(filename):
    file_hash = calculate_sha256(filename)
    print("\nSHA-256 Hash:")
    print(file_hash)
else:
    print("Invalid file path.")
