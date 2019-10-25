class Alignment:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

    def hamming(self):
        seq1 = self.seq1
        seq2 = self.seq2
        if len(seq1) != len(seq2):
            return "Sequences should be of equal length"
        else:
            hamming_dist = 0
            for base in range(0, len(seq1)):
                if seq1[base] != seq2[base]:
                    hamming_dist += 1
            return hamming_dist