import test



keyword = "file"

with open("input.txt", "r") as input_file, open("filtered.txt", "w") as output_file:
    for line in input_file:
        if keyword in line:
            output_file.write(line)
            result = output_file
            test.test(result)



