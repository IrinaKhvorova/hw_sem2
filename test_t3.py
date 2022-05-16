import os
import unittest
import t3_amplicons as t3


class Task3Test(unittest.TestCase):
    tmp_file_name = ".tmp.txt"
    file_content = """>Seq1
AAACCCTTT
>Seq2
sdgAAACCCTTTvcb
>Seq3
34AAACCswCTTTw4
>Seq4
ACACCCTTT"""

    def setUp(self):
        with open(self.tmp_file_name, 'w') as f:
            f.write(self.file_content)

    def test_smth(self):
        amplicons = t3.find_amplicons(self.tmp_file_name, "AAA", "TTT")
        self.assertEqual([
            ("AAACCCTTT", ["CCC"]),
            ("sdgAAACCCTTTvcb", ["CCC"]),
            ("34AAACCswCTTTw4", ["CCswC"]),
            ("ACACCCTTT", [])
        ], amplicons)

    # def tearDown(self):
    #     os.remove(self.tmp_file_name)
