#Olivia De Liberty
#DNA to Protein
#Original Work(I did not use a tutorial)

#http://www.bioinformatics.org/sms2/random_dna.html
#This is just a website that gives random sequences that is helpful for testing

original_sequence = input("DNA Nucleotide Sequence: ")

import tkinter
import random

#The list of proteins made by combinations of nucleotides
phenylalanine = ['uuu', 'uuc']
leucine = ['uua', 'uug', 'cuu', 'cuc', 'cua', 'cug']
serine = ['ucu', 'ucc', 'uca', 'ucg','agu', 'agc']
tyrosine = ['uau', 'uac']
termination = ['uaa', 'uag', 'uga']
cysteine = ['ugu', 'ugc']
tryptophan = ['ugg']
proline = ['ccu', 'ccc', 'cca', 'ccg']
histidine = ['cau', 'cac']
glutamine = ['caa', 'cag']
arginine = ['cgu', 'cgc', 'cga', 'cgg', 'aga', 'agg']
isoleucine = ['auu', 'auc', 'aua']
methionine = 'aug'
threonine = ['acu', 'acc', 'aca', 'acg']
asparagine = ['aau', 'aac']
lysine = ['aaa', 'aag']
valine = ['guu', 'guc', 'gua', 'gug']
alanine = ['gcu', 'gcc', 'gca', 'gcg']
aspartate = ['gau', 'gac']
glutamate = ['gaa', 'gag']
glycine = ['ggu', 'ggc', 'gga', 'ggg']

#list of protein(I had to make a second list for the string version of all of these proteins because it won't let me print the name of the list inside a different list :<)
proteins = [phenylalanine, leucine, serine, proline, isoleucine, methionine, threonine, valine, alanine, cysteine, tryptophan, tyrosine, termination, arginine, histidine, glutamine, asparagine, lysine, glycine, aspartate, glutamate]
str_proteins = ['phenylalanine', 'leucine', 'serine', 'proline', 'isoleucine', 'methionine', 'threonine', 'valine', 'alanine', 'cysteine', 'tryptophan', 'tyrosine', 'termination', 'arginine', 'histidine', 'glutamine', 'asparagine', 'lysine', 'glycine', 'aspartate', 'glutamate']

#proteins produced list:
products = []

#Creates a new list of the base pairs
def polymerase(dna):
    print("Original DNA Neucleotide Sequence:", dna)
    coding_strand = ""
    for nucleotide in dna:
        if nucleotide == "a":
            coding_strand = coding_strand + "t"
        if nucleotide == "t":
            coding_strand = coding_strand + "a"
        if nucleotide == "g":
            coding_strand = coding_strand + "c"
        if nucleotide == "c":
            coding_strand = coding_strand + "g"
    print("Translated DNA Sequence:", coding_strand)
    rna_strand(coding_strand)

#Translates the new nucleotides into the next RNA
def rna_strand(dna):
    rna = ""
    for nucleotide in dna:
        if nucleotide == "a":
            rna = rna + "u"
        if nucleotide == "t":
            rna = rna + "a"
        if nucleotide == "g":
            rna = rna + "c"
        if nucleotide == "c":
            rna = rna + "g"
    print("RNA Transcription Sequence: ", rna)
    start_codon(rna)

#Finding the start codon sequence(aug) also makes methionine
def start_codon(rna):
    for n in range(len(rna)-1):
        codon = rna[n:n + 3]
        if codon == methionine:
            products.append('methionine')
            print("START Located")
            sequence = rna[n:]
            codon_seperator(sequence)
    print(products)
    product_analysis()

def codon_seperator(strand):
    codons = int(len(strand) / 3)
    codonList = []
    for i in range(0, codons):
        codon = strand[3*i:3*i+3]
        codonList.append(codon)
    counting = 0
    for codon in codonList:
        counting = counting + 1
        for combination in termination:
            if codon == combination:
                codonList = codonList[:counting]
    print(codonList)
    for codon in codonList:
        amino_acid_sorter(codon)

def amino_acid_sorter(codon):
    counter = 0
    for protein in proteins:
        counter = counter + 1
        for combination in protein:
            if codon == combination:
                print(codon, "=", str_proteins[counter - 1])
                products.append(str_proteins[counter - 1])

def product_analysis():
    total = len(products)
    for protein in str_proteins:
        count = 0
        for product in products:
            if product == protein:
                count = count + 1
        print(protein, ":", count)
        percent = (count / total) * 100
        print("+", format(percent, '.2f'), "%")

#tagagcaatgtcgaggttgccccgcgcgcgcgcgcctttcagaggactattccagagaaattgggttcagcggttgcagttctgcagaaacgatcagtataggcctgttgctacgggttggccgtattcaccagactcgtttagacctccgaccagcttgggaagtgtccgatacgatcttcagtcagccaacttgaactcgcgatacccttaaaaggcaatactcgatcctatgcaaggactagagtgccaagcacctttagcccggcatagcagacaagctacgattagccgcacccctcaaaataatacacagtcgcttcagttcctaagtgtacatacctagtctctgaaatacccagtgcctaccctatttgctattccctcctaggactggcttaggttctggacactcggcatccgatttgaggaaacttgcgggagccaaagcacgggttggtttttaaccgtggcattttctaggacagcaacctgggctgtgtcagacgagagcctaacgcccacatagtttacacacgaaacgcaactgattatgactctaggcaaggtttagccattgattgcgacgcgaactagagacgcccccaggtgtgtactatgatgagcaccttctaagatagtcagtaggcttctggcacaaccagtttgaagttagtaacttctggtctttttccctagtatcaattattcttcagactatttgatatggtgtcgctggtcttcgccccagttcggcgcacctgcgtggtgtcctttcctagtcagagagctactggataggtcttaattacaagtacagcagtctacatgaaggatcttctcgtgcagtggcgatttagctgattacaccgaatccattttgcgtaggaagacttcacgataccgatcaggacttcggacagacgagtttatttacctttggatatcactggcaattgtagggtaactcgcattaactcatcttaatgccgaacgtctt
polymerase(original_sequence)