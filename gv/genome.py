# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:40:29 2018

@author: fraz
"""

import allel
import numpy as np
from Bio import SeqIO
from pyfaidx import Fasta, wrap_sequence

STANDARD_GENOME_PATH = "F:/RG/intern/genome_visualizer/"

class Genome():
    fastaFileName = ""

    def __init__(self, fileName):
        self.fastaFileName = fileName
    
    def splitGenome(self):
        fa= Fasta(self.fastaFileName)
        for seq in fa:
            with open('{}{}.fa'.format(STANDARD_GENOME_PATH, seq.name), 'w') as out:
                out.write('>{}\n'.format(seq.name))
                for line in wrap_sequence(70, str(seq)):
                    out.write(line)
        print("<<<<<<<Splitted>>>>>>")
        
class Chromosome():
    def __init__(self, chromosome_name):
        if(chromosome_name in VCF.VCF_CHROMOSOMES): # check valid name
            chromosomeFile = '{}{}.{}'.format(STANDARD_GENOME_PATH, chromosome_name, 'fa')
            with open(chromosomeFile) as chromosomeData:  # Will close handle cleanly
                lengths = []
                for record in SeqIO.parse(chromosomeData, "fasta"):  # (generator)...in this case it is not a multi fasta file
                    lengths.append(record.seq)
            self.recordSequence = record.seq
    def getLength(self):
        return len(str(self.recordSequence))
        
class VCF():
    vcfFileName = ""
    VCF_CHROMOSOMES = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7',
                       'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13',
                       'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19',
                       'chr20', 'chr21', 'chr22', 'chrX', 'chrY']
    
    def __init__(self, fileName):
        self.vcfFileName = fileName;
        self.dataFrame = allel.vcf_to_dataframe(fileName, fields=['CHROM', 'POS', 'REF', 'ALT'], alt_number=1)
    
    def getFileName(self):
        return self.vcfFileName
        
    def getVariation(self, chromosome_name):
        return self.dataFrame.POS[self.dataFrame.CHROM == chromosome_name]


