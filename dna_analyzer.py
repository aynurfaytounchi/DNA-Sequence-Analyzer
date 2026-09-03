valid_bases = {"A", "T", "C", "G"}

DNA = input("Enter your DNA: ").upper()

while not DNA or not set(DNA).issubset(valid_bases):
    print("Invalid DNA!")
    DNA = input("Enter your DNA again: ").upper()

print("Valid DNA")

A = 0
G = 0
C = 0
T = 0

for base in DNA:

    if base == "A":
        A += 1

    elif base == "G":
        G += 1

    elif base == "C":
        C += 1

    elif base == "T":
        T += 1


complement = ""

for base in DNA:

    if base == "A":
        complement += "T"

    elif base == "T":
        complement += "A"

    elif base == "G":
        complement += "C"

    elif base == "C":
        complement += "G"


length = len(DNA)

print(f"Your DNA is: {DNA}")
print(f"DNA complement: {complement}")
print(f"Length of DNA: {length}")
print(f"A: {A}")
print(f"G: {G}")
print(f"C: {C}")
print(f"T: {T}")
print(f"GC: {(G + C) / length * 100}%")
