from Nucleotides import DNA

def main():
    dna1 = DNA.DNA("ATGGG")
    rna1 = dna1.transcribe()
    print(rna1)

if __name__ == "__main__":
    main()
