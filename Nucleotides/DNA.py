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


