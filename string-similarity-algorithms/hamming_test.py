from hamming import hamming_distance

def test_distance_1():
    assert hamming_distance("test", "test") == 0

def test_distance_2():
    assert hamming_distance("test", "tester") == 2

def test_distance_3():
    assert hamming_distance("test", "sing") == 4

def test_distance_4():
    assert hamming_distance("test", "singer") == 6

def test_distance_5():
    assert hamming_distance("test", "") == 4

def test_distance_6():
    assert hamming_distance("test", "tesst") == 2

def test_distance_7():
    assert hamming_distance("test", "tets") == 2


from hamming import hamming

def test_similarity_1():
    assert hamming("test", "") == 0.0

def test_similarity_2():
    assert hamming("test", "test") == 1.0

def test_similarity_3():
    assert round(hamming("test", "tester"), 2) == 0.67

def test_similarity_4():
    assert hamming("test", "tets") == 0.5