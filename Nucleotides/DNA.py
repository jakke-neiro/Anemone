class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def transcribe(self):
        RNAsequence = ""
        for i in range(0, len(self.sequence)):
            if DNAsequence[i] == "T":
                RNAsequence = RNAsequence + "U"
            else:
                RNAsequence = RNAsequence + DNAsequence[i]
        return RNAsequence