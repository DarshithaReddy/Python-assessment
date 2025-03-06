with open("sample.txt", "rb") as file:
    file.seek(10)  # Move to the 10th byte
    data = file.read(5)  # Read 5 bytes from that position
    print("Data at position 10:", data.decode())
