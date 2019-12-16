import math
import os
import random
import re
import sys


# Complete the steadyGene function below.
from collections import Counter

def valid_genes_amt(max_gene_freq, curr_gene_amts):
        ret = True
        for key, val in curr_gene_amts.items():
                if val > max_gene_freq:
                        ret = False
                        break
        return ret

# Complete the steadyGene function below.
def steadyGene(gene):
        full_genes_len = len(gene)
        max_gene_freq = full_genes_len/4
        curr_gene_amts = Counter(gene)

        min_ans = 10**9
        right = 0
        left = 0
        while right < full_genes_len and left < full_genes_len:
                if not valid_genes_amt(max_gene_freq, curr_gene_amts):
                        curr_gene_amts[gene[right]] -= 1
                        right += 1
                else:
                        min_ans = min(min_ans,  right - left)
                        curr_gene_amts[gene[left]] += 1
                        left += 1

        return min_ans

g = 'GAAATAAA'
# g = 'TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'
print(steadyGene(g))

