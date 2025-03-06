import re
pattern = r"^Hello"
text = "Hello World"
match = re.match(pattern, text)
print("Match found!" if match else "No match")
