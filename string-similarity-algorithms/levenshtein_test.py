from levenshtein import levenshtein_distance

def test_distance_1():
    assert levenshtein_distance("test", "test") == 0

def test_distance_2():
    assert levenshtein_distance("test", "tester") == 2

def test_distance_3():
    assert levenshtein_distance("test", "sing") == 4

def test_distance_4():
    assert levenshtein_distance("test", "singer") == 6

def test_distance_5():
    assert levenshtein_distance("test", "") == 4

def test_distance_6():
    assert levenshtein_distance("test", "tesst") == 1

def test_distance_7():
    assert levenshtein_distance("test", "tets") == 2


from levenshtein import levenshtein

def test_similarity_1():
    assert levenshtein("test", "") == 0.0

def test_similarity_2():
    assert levenshtein("test", "test") == 1.0

def test_similarity_3():
    assert round(levenshtein("test", "tester"), 2) == 0.67

def test_similarity_4():
    assert levenshtein("test", "tets") == 0.5