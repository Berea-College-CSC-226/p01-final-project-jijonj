######################################################################
# Author(s): Dr. Scott Heggen
# Username(s): heggens
#
# Assignment: HW08: It's in Your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Ideas borrowed from j. ben Schafer: https://www.cs.uni.edu/~schafer/
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################



def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence: takes a sequence of nucleotides
    :return isNucleotide:
    """

    # create a list of all possible nucleotides
    nucleotides = ['A', 'C', 'G', 'T']

    # for loop that checks each letter in the passed-in sequence
    for i in sequence:

        # check each letter and see if they are not in nucleotides list
        if i.upper() not in nucleotides:

            # if not in list, end loop early and return False
            return False

    # if loop doesn't end early, return True
    return True


def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence: takes a sequence of nucleotides
    :return complement: the complement of the sequence
    """

    complement = ""

    # dictonary that holds the pairs
    complementpairs = {"A":"T", "C": "G", "T":"A", "G":"C"}

    # for loop checks each letter in the sequence
    for i in sequence:

        # if letter is in dictionary keys, add the key's value to the string
        if i in complementpairs.keys():
            complement = complement + complementpairs[i]

        # else, end loop early and return sequencing error
        else:
             return "Sequencing Error"

    return complement


def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence: takes a sequence of nucleotides
    :return mrna: sequence of mrna (sequence that has T replaced with U)
    """


    mrna = ""

    # make all letters uppercased
    sequence = sequence.upper()

    # replace all T with U
    mrna = sequence.replace("T", "U")

    # returns mrna string
    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence: takes a sequence of nucleotides
    :return list_of_chunks: list that holds the chunks of three nucleotides
    """

    list_of_chunks = []

    # get the remainder of the length of the passed-in sequence modulus 3
    remainder = len(sequence) % 3

    # if remainder is not divisible by three...
    if remainder != 0:

        # slice sequence to make the length of sequence divisible by three // get rid of other characters
        sequence = sequence[:len(sequence) - remainder]

    # while loop that runs the length of the sequence
    i = 0
    while i != len(sequence):

        # append the chunk of the sequence by using slice // i = 0, i + 3 = 3 etc.
        list_of_chunks.append(sequence[i:i+3])

        # add 3 to i to increment i by 3
        i += 3

    return list_of_chunks


def translate_amino_acid(three_char_seq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character amino acid

    :param three_char_seq: a sequence of three characters
    :return: A string representing the amino acid chunk for that sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                  "GAC": "D", "GAU": "D",
                  "AAC": "N", "AAU": "N",
                  "UGC": "C", "UGU": "C",
                  "GAA": "E", "GAG": "E",
                  "CAA": "Q", "CAG": "Q",
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G",
                  "CAC": "H", "CAU": "H",
                  "AUA": "I", "AUC": "I", "AUU": "I",
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                  "AAA": "K", "AAG": "K",
                  "AUG": "M",
                  "UUC": "F", "UUU": "F",
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                  "UGG": "W",
                  "UAC": "Y", "UAU": "Y",
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                  "UAA": "*", "UAG": "*", "UGA": "*"
                 }

    if three_char_seq in translator.keys():
        return translator[three_char_seq]  # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a sequence of nucleotides and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + translate_amino_acid(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code

    :return: None
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #
    print("The original sequence {0} returns {1}".format("CACGT", sequence_gene("CACGT")))
    print("The original sequence {0} returns {1}".format("GCA", sequence_gene("GCA")))
    print("The original sequence {0} returns {1}".format("CACAUU", sequence_gene("CACAUU")))

if __name__ == "__main__":
    main()          # call to main() function
