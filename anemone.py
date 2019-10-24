import argparse

from nucleotides import DNA

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Gives the message')

    parser.add_argument('--transcribe',
                        metavar='DNAfile',
                        type=str,
                        help='DNA file')

    parser.add_argument('--count',
                        metavar='DNAfile',
                        type=str,
                        help='DNA sequence')

    # Execute the parse_args() method
    args = parser.parse_args()

    DNAseq = args.transcribe
    DNAseqcount = args.count

    dna1 = DNA.DNA(DNAseqcount)
    dna1.count()

if __name__ == "__main__":
    main()
