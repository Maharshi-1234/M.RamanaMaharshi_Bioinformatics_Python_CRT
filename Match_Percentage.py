db = {
  "geneA": "ATGT",  # 3/4 = 75%
  "geneB": "ATGC",  # 4/4 = 100%
  "geneC": "TTAC",  # 1/4 = 25%
  "geneD": "ATGG",  # 3/4 = 75%
  "geneE": "ATCC",  # 3/4 = 75%
  "geneF": "AGGC",  # 2/4 = 50%
  "geneG": "GTGC",  # 3/4 = 75%
  "geneH": "TTGC",  # 3/4 = 75%
  "geneI": "GGGG",  # 0/4 = 0%
  "geneJ": "ATGA"   # 3/4 = 75%
}
#Match % >= 80 -> "Good Match"
#50<= % < 80 -> "Moderate match"
#% < 50 -> "Poor Match"
def generate_report(dna,db):
    Count_G=0
    Count_C=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        Count_C=dna.count(i)
        Count_G=dna.count(i)
    GC_Count=(Count_G+Count_C)/len(dna)*100
    if(GC_Count>80):
        Status="Good Match"
    elif(GC_Count>=50 and GC_Count<=80):
        Status="Moderate Match"
    else:
        Status="Poor Match"
    print(f"ID:{ID}| Match:{GC_Count}%| Status:{Status}")
Sequence="ATGT"
generate_report(Sequence,db)