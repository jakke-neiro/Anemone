class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def transcribe(self):
        RNAsequence = ""
        for i in range(0, len(self.sequence)):
            if self.sequence[i] == "T":
                RNAsequence = RNAsequence + "U"
            else:
                RNAsequence = RNAsequence + self.sequence[i]
        return RNAsequence

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

        print("A: " + str(A_count) + " " + "T: " + str(T_count))
