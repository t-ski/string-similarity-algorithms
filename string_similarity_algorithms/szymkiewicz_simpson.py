def szymkiewicz_simpson(str1: str, str2: str) -> float:
    intersection = 0
    union = abs(len(str2) - len(str1))
    
    for i in range(0, min(len(str1), len(str2))):
        union += 1
        if str1[i] == str2[i]:
            intersection += 1
        else:
            union += 1
    
    denominator = min(len(str1), len(str2))
    return (intersection / denominator) if (denominator > 0) else 0