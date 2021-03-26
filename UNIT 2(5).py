import re
items = ["abc (.com)", "w3school", "google (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))
