import re


def transform(primer):
    comp_primer = ''
    comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in primer:
        if not i.isupper() or not i.isalpha():
            raise TypeError("Wrong data format")
        else:
            if i in comp:
                comp_primer += comp[i]
            else:
                comp_primer += i
    return comp_primer[::-1]


def find_amplicons(path, first, second):
    pattern = first + "\w*" + second
    #pattern = pattern.replace('N', '\w')
    pattern = pattern.replace('[^ATGC]', '\w')
    re_pattern = re.compile(pattern)
    amplicons = []
    try:
        with open(path) as f:
            idx = 0
            for line in f:
                line = line.strip()
                idx += 1
                if idx % 2 == 1:
                    seq_name = line
                    continue
                if not line.isupper() or not line.isalpha():
                    raise TypeError("Wrong data format")
                res = re_pattern.search(line)
                line_amplicons = []
                if res is not None:
                    for reg in res.regs:
                        result = res.string[reg[0] + len(first):reg[1] - len(second)]
                        line_amplicons.append(result)
                        # print(seq_name, result)
                else:
                    raise LookupError("Amplicons not found")

                amplicons.append((seq_name, line_amplicons))
    except FileNotFoundError:
        print('Файл отсутствует')
    return amplicons


if __name__ == '__main__':
    first_primer = input()
    second_primer = input()
    try:
        second_primer = transform(second_primer)
    except TypeError as err:
        print(err)

    try:
        find_amplicons("test.fasta", first_primer, second_primer)
    except TypeError as err:
        print(err)
    except LookupError as err:
        print(err)