import re

with open("matrix.txt", "r") as f:
    data = f.readlines()

questions = []
for line in data:
    if re.match(r"^Smith:", line):
        for question in [i.group() for i in re.finditer(r"\?(\w+(\s|,)*){2,}\?", line)]:
            if question not in questions:
                questions.append(question)

for i in questions:
    print(i)
