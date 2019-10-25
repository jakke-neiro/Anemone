#!/usr/bin/env python
import argparse
import sys

from nucleotides import DNA
from nucleotides import fasta

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Anemone is a multipurpose toolbox for sequence data. ')

    #Listing the arguments of the tool
    parser.add_argument('--count', "-c",
                        metavar='seq',
                        type=str,
                        help='Count the number of each base in the sequence')

    parser.add_argument('--GCcontent', "-gc",
                        metavar='seq',
                        type=str,
                        help='Report the GC content of a sequence')

    parser.add_argument('--transcribe', "-t",
                        metavar='seq',
                        type=str,
                        help='Transcribe your sequence')

    parser.add_argument('--reverse_complement', "-rc",
                        metavar='seq',
                        type=str,
                        help='Reverse complement your sequence')

    # Execute the parse_args() method

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.count:
        count_file = fasta.fa_read(args.count)
        dna1 = DNA.DNA(count_file)
        counts = dna1.count()
        print("A: " + counts[0] + " T: " + counts[1] + " C: " + counts[2] + " G: " + counts[3])

    if args.GCcontent:
        count_file = fasta.fa_read(args.GCcontent)
        dna1 = DNA.DNA(count_file)
        counts = dna1.GC()
        print(counts)

    if args.transcribe:
        transcribe_file = fasta.fa_read(args.transcribe)
        dna1 = DNA.DNA(transcribe_file)
        print(dna1.transcribe())

    if args.reverse_complement:
        complement_file = fasta.fa_read(args.reverse_complement)
        dna1 = DNA.DNA(complement_file)
        print(dna1.reverse_complement())

if __name__ == "__main__":
    main()
