import os
import unittest
import t5_ORF as t5


class Task5Test(unittest.TestCase):
    tmp_file_name = ".tmp.txt"

    def test_empty(self):
        with open(self.tmp_file_name, 'w') as f:
            pass
        orfs = t5.find_orfs(self.tmp_file_name)
        self.assertEqual(0, len(orfs))
        os.remove(self.tmp_file_name)

    def test_small_zero(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            f.write('ATGC\n')
        orfs = t5.find_orfs(self.tmp_file_name)
        self.assertEqual(0, len(orfs))
        os.remove(self.tmp_file_name)

    def test_small_one(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            seq = 'ATG' + 'TAA'
            f.write(seq + '\n')
        orfs = t5.find_orfs(self.tmp_file_name)
        self.assertEqual(0, len(orfs))
        os.remove(self.tmp_file_name)

    def test_big_one(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            seq = 'ATG' + (100*'A') + 'TAA'
            f.write(seq + '\n')
        orfs = t5.find_orfs(self.tmp_file_name)
        self.assertEqual(1, len(orfs))
        self.assertEqual([seq], orfs)
        os.remove(self.tmp_file_name)

    def test_big_one_edge(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            orig_seq = 'ATG' + (100*'A') + 'TAA'
            seq = 'AAGGGG' + orig_seq + 'AAGGGG'
            f.write(seq + '\n')
        orfs = t5.find_orfs(self.tmp_file_name)
        self.assertEqual(1, len(orfs))
        self.assertEqual([orig_seq], orfs)
        os.remove(self.tmp_file_name)

    def test_big_few(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            seq = 'ATG' + (100*'A') + 'TAA' + 'TGA'
            f.write(seq + '\n')
        orfs = t5.find_orfs(self.tmp_file_name)
        self.assertEqual(2, len(orfs))
        self.assertEqual([seq[:-3], seq], orfs)
        os.remove(self.tmp_file_name)

    def test_wrong_symbol(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            f.write('ATBC\n')
        with self.assertRaises(ValueError):
            t5.find_orfs(self.tmp_file_name)
        os.remove(self.tmp_file_name)

    def test_wrong_case(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write('>Seq1\n')
            f.write('atgc\n')
        with self.assertRaises(ValueError):
            t5.find_orfs(self.tmp_file_name)
        os.remove(self.tmp_file_name)
