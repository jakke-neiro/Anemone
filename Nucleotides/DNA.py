class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def count(self):
        A_count = 0
        T_count = 0
        C_count = 0
        G_count = 0
        for i in range(0, len(self.sequence)):
            if self.sequence[i] == "A":
                A_count += 1
            if self.sequence[i] == "T":
                T_count += 1
            if self.sequence[i] == "C":
                C_count += 1
            if self.sequence[i] == "G":
                G_count += 1

        return [str(A_count), str(T_count), str(C_count), str(G_count)]

    def GC(self):
        A_count = 0
        T_count = 0
        C_count = 0
        G_count = 0
        for i in range(0, len(self.sequence)):
            if self.sequence[i] == "A":
                A_count += 1
            if self.sequence[i] == "T":
                T_count += 1
            if self.sequence[i] == "C":
                C_count += 1
            if self.sequence[i] == "G":
                G_count += 1
        total_count = float(A_count + T_count + G_count + C_count)
        GC_count = float(G_count + C_count)
        GC_content = (GC_count/total_count)
        return GC_content

    def transcribe(self):
        RNAsequence = ""
        DNAsequence = self.sequence.upper()
        for i in range(0, len(DNAsequence)):
            if self.sequence[i] == "T":
                RNAsequence = RNAsequence + "U"
            else:
                RNAsequence = RNAsequence + DNAsequence[i]
        return RNAsequence

    def reverse_complement(self):
        DNA_sequence = self.sequence.upper()
        reverse = ""
        complement_dictionary = {"A": "T", "C": "G", "T": "A", "G": "C"}
        for base in range(0, len(DNA_sequence)):
            reverse = reverse + complement_dictionary[DNA_sequence[-(base+1)]]
        return reverse

    def translate(self):
        gencode = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
            'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W', "": ""}
        DNA_sequence = self.sequence.upper()
        polypeptide = ""
        if len(DNA_sequence) % 3 == 1:
            DNA_sequence = DNA_sequence[:(len(DNA_sequence) - 1)]
        if len(DNA_sequence) % 3 == 2:
            DNA_sequence = DNA_sequence[:(len(DNA_sequence) - 2)]
        for base in range(0, len(DNA_sequence)):
            codon = DNA_sequence[3 * base:(3 * base + 3)]
            amino_acid = gencode[codon]
            polypeptide = polypeptide + amino_acid
        return polypeptide



