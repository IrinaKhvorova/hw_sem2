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

    def complement(self):
        comp_seq = ''
        comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq #возвращает комплементарную последовательность

    def transcription(self):
        rna_seq = ''
        comp = {'A': 'Y', 'T': 'A', 'G': 'C', 'C': 'G'} #ДНК как матричная
        for i in self.seq:
            rna_seq += comp[i]
        return rna_seq #возвращает последовательность РНК


def read_fasta(file_name):
    with open(file_name, "r") as file:
        seqs, max_name, max_len, max_stat = [], 0, 0, 0
        for record in SeqIO.parse(file, 'fasta'):  # итерация по строкам
            cur_seq = DNA(str(record.id), str(record.seq))
            comp_seq = DNA(cur_seq.name, cur_seq.complement()[::-1])
            print(cur_seq.seq, comp_seq.seq, sep='\n')
            seqs.append(cur_seq.transcription())
            seqs.append(comp_seq.transcription())
    return seqs

test = read_fasta('test.fasta')