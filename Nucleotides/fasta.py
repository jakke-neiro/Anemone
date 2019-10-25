def fa_read(fasta):
    f = open(fasta, "r")
    f1 = f.readline().rstrip("\n")
    f.close()
    fasta = ""
    for line in f1:
        fasta = fasta + line
    return fasta