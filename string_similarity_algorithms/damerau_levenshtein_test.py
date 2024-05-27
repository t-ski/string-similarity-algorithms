from damerau_levenshtein import damerau_levenshtein_distance

def test_distance_1():
    assert damerau_levenshtein_distance("test", "test") == 0

def test_distance_2():
    assert damerau_levenshtein_distance("test", "tester") == 2

def test_distance_3():
    assert damerau_levenshtein_distance("test", "sing") == 4

def test_distance_4():
    assert damerau_levenshtein_distance("test", "singer") == 6

def test_distance_5():
    assert damerau_levenshtein_distance("test", "") == 4

def test_distance_6():
    assert damerau_levenshtein_distance("test", "tesst") == 1

def test_distance_7():
    assert damerau_levenshtein_distance("test", "tets") == 1 # different from basic Levenshtein


from damerau_levenshtein import damerau_levenshtein

def test_similarity_1():
    assert damerau_levenshtein("test", "") == 0.0

def test_similarity_2():
    assert damerau_levenshtein("test", "test") == 1.0

def test_similarity_3():
    assert round(damerau_levenshtein("test", "tester"), 2) == 0.67

def test_similarity_4():
    assert damerau_levenshtein("test", "tets") == 0.75