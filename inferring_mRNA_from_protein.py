translation = {
        "F" : 2,
        "L" : 6,
        "S" : 6,
        "P" : 4,
        "Y" : 2,
        "H" : 2,
        "Q" : 2,
        "I" : 3,
        "M" : 1,
        "V" : 4,
        "A" : 4,
        "T" : 4,
        "N" : 2,
        "K" : 2,
        "D" : 2,
        "E" : 2,
        "C" : 2,
        "W" : 1,
        "R" : 6,
        "G" : 4,
        "STOP" : 3
}

#Input your protein sequence
protein_seq = input('Please input your protein sequence : ')

#Initialize result
result = translation[protein_seq[0]]

#Computer the possible kind of condons from protein sequence
for i in protein_seq[1:]:
    result *= translation[i]

#Don't forgot the stop condon
result *= 3

print(result % 1000000)
