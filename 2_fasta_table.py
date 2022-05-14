from Bio import SeqIO


class DNA:
    alphabet = ['A', 'T', 'G', 'C']

    def __init__(self, name, seq):
        self.name = name
        self.seq = seq

    def __len__(self):
        return len(self.seq)  # возвращает длину последовательности

    def statistics(self):
        stat = dict.fromkeys(self.alphabet, 0)
        for i in self.seq:
            stat[i] += 1
        return stat  # возвращает статистику по использованию символов


def fasta_table(file_name):
    with open(file_name, "r") as file:
        seqs, max_name, max_len, max_stat = [], 0, 0, 0
        for record in SeqIO.parse(file, 'fasta'):  # итерация по строкам
            cur_seq = DNA(str(record.id), str(record.seq))
            seqs.append(cur_seq)
            if max_name < len(cur_seq.name):
                max_name = len(cur_seq.name)
            if max_len < len(str(len(cur_seq))):
                max_len = len(str(len(cur_seq)))
            for value in cur_seq.statistics().values():
                if max_stat < len(str(value)):
                    max_stat = len(str(value))
    print('Name'.ljust(max_name + 2), 'Length'.center(max_len + 4), 'A'.center(max_stat + 2),
          'T'.center(max_stat + 2), 'G'.center(max_stat + 2), 'C'.center(max_stat + 2), sep='')
    for s in seqs:
        print(s.name.ljust(max_name + 2), end='')
        print(str(len(s)).center(max_len + 4), end='')
        for i in 'ATGC':
            print(str(s.seq.count(i)).center(max_stat + 2), end='')
        print()

test = fasta_table('test.fasta')
