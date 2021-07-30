def steadyGene(gene):
    n = int(len(gene)/4)
    genes = {}
    remove = {}
    minimum = 0
    for g in gene:
        genes[g] = genes.get(g, 0) + 1
        if genes[g] > n:
            remove[g] = remove.get(g, 0) + 1

    minimum = remove.get("A", 0) + remove.get("C", 0) + remove.get("G", 0) + remove.get("T", 0)        
    if not minimum:
        return 0
    
    total = len(gene)+1
    control = {"A": remove.get("A", 0), "C": remove.get("C", 0), "G": remove.get("G", 0), "T": remove.get("T", 0)}
    array = []
    pivot = 0
    for k, v in enumerate(gene):
        control[v] -= 1
        if (not array and remove.get(v)) or array:
            array.append((k, v))

        while control["A"] <= 0 and control["C"] <= 0 and control["G"] <= 0 and control["T"] <= 0:
            total = min(total, k-array[pivot][0]+1)
            if total == minimum:
                return total

            control[array[pivot][1]] += 1
            pivot += 1
        
    return total            

if __name__ == "__main__":
    # string = "GAAATAAA"
    # string = "GATC"
    # string = "AAGTGCCT"
    # string = "ACTGAAAG"
    string = "TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC"
    print(steadyGene(string))