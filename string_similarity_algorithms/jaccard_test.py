from jaccard import jaccard

def test_similarity_1():
    assert jaccard("test", "") == 0.0

def test_similarity_2():
    assert jaccard("test", "test") == 1.0

def test_similarity_3():
    assert round(jaccard("test", "tester"), 2) == 0.67

def test_similarity_4():
    assert round(jaccard("test", "tets"), 2) == 0.33