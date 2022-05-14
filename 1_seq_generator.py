def read_file(file_name):
    with open(file_name, "r") as file:
        for line in file:  # итерация по строкам
            yield line.strip()


test = read_file('test.fasta')

for i in test:
    print(i)
