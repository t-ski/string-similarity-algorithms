def hamming_distance(str1: str, str2: str) -> int:
    dist = abs(len(str1) - len(str2))

    for i in range(0, min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            continue
        dist += 1
    
    return dist


def hamming(str1: str, str2: str) -> float:
    return 1 - (hamming_distance(str1, str2) / max(len(str1), len(str2)))