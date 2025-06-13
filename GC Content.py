#DNA sequence as input and calculate GC Content as percentage classify as High GC(>60),Moderate(40 to 60)
#Low GC(<40)
seq = input("Enter Your DNA Sequence: ")
gc_count = 0
for base in seq:
    if base == 'G' or base == 'C':
        gc_count +=1
gc_percent= (gc_count/ len(seq)) * 100
print("GC Content :",gc_percent,"%")
if gc_percent > 60:
    print("High GC Content")
elif gc_percent >= 40:
    print("Moderate GC Content")
else:
    print("Low GC Content")