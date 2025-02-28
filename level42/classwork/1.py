def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += '0'
        else:
            result += '1'
    return result

age = 25
binary_age = bin(age)[2:]
print(binary_age)

def dna_to_rna(dna):
    return dna.replace('T', 'U')