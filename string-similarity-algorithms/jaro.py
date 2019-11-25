def jaro(str1: str, str2: str) -> float:
    match_radius = max(len(str1), len(str2))

    str1_matches = [ False for _ in range(len(str1)) ]
    str2_matches = [ False for _ in range(len(str1)) ]
    
    matches = 0
    for i in range(0, len(str1)):
        for j in range(max(0, i - match_radius), min(i + match_radius + 1, len(str2))):
            if str2_matches[j]:
                continue

            if str1[i] == str2[j]:
                str1_matches[i] = True
                str2_matches[j] = True

                matches += 1

                break

    transpositions = 0
    j = 0
    for i in range(0, len(str1)):
        if not str1_matches[i]:
            continue

        while not str2_matches[j]:
            j += 1
        
        if str1[i] != str2[j]:
            transpositions += 1
        
        j += 1

    return 0.0 if matches == 0 else \
           (1 / 3) * ((matches / len(str1)) + (matches / len(str2)) \
                        + ((matches - transpositions / 2) / matches))