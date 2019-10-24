import argparse

from Nucleotides import DNA

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Gives the message')

    parser.add_argument('--transcribe',
                        metavar='DNAfile',
                        type=str,
                        help='DNA file')

    # Execute the parse_args() method
    args = parser.parse_args()

    DNAseq = args.transcribe

    dna1 = DNA.DNA(DNAseq)
    print(dna1.transcribe())

if __name__ == "__main__":
    main()
