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



