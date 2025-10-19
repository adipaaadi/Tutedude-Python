from pathlib import Path

filename = "sample.txt"
file_path = Path(filename)

if file_path.is_file():
    print("Reading file content:")
    with file_path.open('r') as file:
        for idx, line in enumerate(file, start=1):
            print(f"Line {idx}: {line.strip()}")
else:
    print(f"Error: The file '{filename}' was not found.")
