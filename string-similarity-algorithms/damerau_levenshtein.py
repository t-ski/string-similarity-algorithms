def damerau_levenshtein_distance(str1: str, str2: str) -> int:
    rows = len(str1) + 1
    cols = len(str2) + 1
    dist = [ [ 0 for _ in range(cols) ] for _ in range(rows) ]
    
    if rows == 1 and cols == 1:
        return 1
    
    if rows == 1 or cols == 1:
        return max(rows, cols) - 1

    for i in range(1, rows):
        dist[i][0] = i
    
    for i in range(1, cols):
        dist[0][i] = i

    for row in range(1, rows):
        for col in range(1, cols):
            cost = 0 if(str1[row - 1] == str2[col - 1]) else 1

            dist[row][col] = min(dist[row - 1][col] + 1,
                                dist[row][col - 1] + 1,
                                dist[row - 1][col - 1] + cost)

            if row > 1 and col > 1 \
            and str1[row - 1] == str2[col - 2] \
            and str1[row - 2] == str2[col - 1]:
                dist[row][col] = min(dist[row][col], dist[row - 2][col - 2] + cost)

    return dist[row][col]


def damerau_levenshtein(str1: str, str2: str) -> float:
    return 1 - (damerau_levenshtein_distance(str1, str2) / max(len(str1), len(str2)))