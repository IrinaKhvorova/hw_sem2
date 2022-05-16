import re


def find_orfs(path):
    alphabet = 'ACGT'
    orfs = []
    try:
        with open(path) as f:
            idx = 0
            for line in f:
                idx += 1
                if idx % 2 == 1:
                    continue
                seq = line.strip()
                if not seq.isupper():
                    print(seq)
                    raise ValueError("Sequence is not uppercase")
                if any(c not in alphabet for c in seq):
                    raise ValueError("Sequence contains invalid characters")
                seq = seq.replace('T', 'U')
                starts = list(re.finditer("AUG", seq))
                ends = list(re.finditer("UAA", seq)) + list(re.finditer("UGA", seq)) + list(re.finditer("UAG", seq))
                for start in starts:
                    start_pos = start.regs[0][0]
                    for end in ends:
                        end_pos = end.regs[0][1]
                        if end_pos - start_pos >= 100:
                            orfs.append(seq[start_pos:end_pos].replace('U', 'T'))
            print(orfs)
    except FileNotFoundError:
        print('Файл отсутствует')
    return orfs


if __name__ == '__main__':
    try:
        find_orfs('test.fasta')
    except ValueError as err:
        print(err)