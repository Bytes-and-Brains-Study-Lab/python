import re

with open("C:\Games\Why.txt", 'r') as file:
    file_contents = file.readlines()
    n = input("Enter range of numbers")
    pattern = re.compile('\d*-\d*|\d*')
    matches = re.findall(pattern, n)
    if matches == []:
        print("Invalid input")
        exit()
    for i in n:
        if i.isalpha():
            print("Invalid input")
            exit(a)
    output_lines = []
    for match in matches:
        if '-' in match:
            a = match[0:match.index('-')]
            b = match[match.index('-') + 1:]
            for i in range(int(a), int(b)+1):
                output_lines.append(i)
        elif match == '':
            continue
        else:
            output_lines.append(int(match))
    for i in output_lines:
        if i > len(file_contents):
            print("Out of bounds")
            exit()
    number_of_lines = len(file_contents)
    list1 = []  # List to store output lines
    for i in range(0, number_of_lines):
        if i in output_lines:
            print(f"Line {i}: ", file_contents[i-1])
            list1.append(file_contents[i-1])
    countI = countW = countE = 0
    for i in range(0, len(list1)):
        if list1[i].strip().startswith("INFO"):
            countI += 1
        elif list1[i].strip().startswith("WARNING"):
            countW += 1
        elif list1[i].strip().startswith("ERROR"):
            countE += 1
    print("Summary of events")
    print("INFO: ", countI)
    print("WARNING: ", countW)
    print("ERROR: ", countE)

