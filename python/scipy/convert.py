import re

def convert_line(string):
    l = [float(x) for x in string.strip().split(" ") if x]
    return l

with open("dataraw.txt", "r") as f:
    dataraw = f.read()
    dataraw = re.sub(r'\$\s*', '', dataraw)
    dataset = convert_line(dataraw)

with open("dataset.txt", "w") as f:
    for i in range(len(dataset)):
        # create new line for each element
        f.write(str(dataset[i]))
        f.write("\n")

print("Rows: ", len(dataset))
print(dataset)
