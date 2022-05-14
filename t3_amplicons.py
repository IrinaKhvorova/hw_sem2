import re


def transform(primer):
    comp_primer = ''
    comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in primer:
        comp_primer += comp[i]
    return comp_primer[::-1]


def find_amplicons(path, first, second):
    pattern = first + "\w*" + second
    #pattern = pattern.replace('N', '\w')
    pattern = pattern.replace('[^ATGC]', '\w')
    re_pattern = re.compile(pattern)
    amplicons = []
    with open(path) as f:
        idx = 0
        for line in f:
            line = line.strip()
            idx += 1
            if idx % 2 == 1:
                seq_name = line
                continue
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
    return amplicons


if __name__ == '__main__':
    first_primer = input()
    second_primer = input()
    second_primer = transform(second_primer)
    find_amplicons("test.fasta", first_primer, second_primer)