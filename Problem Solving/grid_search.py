# The Grid Search
# Difficulty: Medium


def gridSearch(G, P):
    rows_g = len(G)
    cols_g = len(G[0])
    rows_p = len(P)
    cols_p = len(P[0])
    expected = rows_p * cols_p
    for ig in range(rows_g):
        for jg in range(cols_g):
            
            if G[ig][jg] == P[0][0] and ig + rows_p <= rows_g and jg + cols_p <= cols_g:
                count = 0
                for ip in range(rows_p):
                    found = True
                    for jp in range(cols_p):
                        
                        if P[ip][jp] == G[ig+ip][jg+jp]:
                            count += 1
                        else:
                            found = False
                            break
                        if count == expected:
                            return "YES"
                    
                    if not found:
                        break
    
    return "NO"

if __name__ == "__main__":
    G = [
        "7283455864",
        "6731158619",
        "8988242643",
        "3830589324",
        "2229505813",
        "5633845374",
        "6473530293",
        "7053106601",
        "0834282956",
        "4607924137"]
    P = [
        "9505",
        "3845",
        "3530",
        ]
    print(gridSearch(G, P))