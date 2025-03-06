try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except OSError as e:
    print(f"IO Error: {e}")
