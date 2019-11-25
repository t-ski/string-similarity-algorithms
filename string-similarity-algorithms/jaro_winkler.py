from jaro import jaro

def jaro_winkler(str1: str, str2: str, p: float = 0.1) -> float:
    sim = jaro(str1, str2)

    l = 0
    for l in range(0, min(len(str1), len(str2))):
        if str1[l] != str2[l]:
            break
    
    jaro_winkler_sim = sim + (l * p * (1 - sim))

    return jaro_winkler_sim