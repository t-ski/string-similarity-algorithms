from jaro import jaro

def test_similarity_1():
    assert jaro("test", "") == 0.0

def test_similarity_2():
    assert jaro("test", "test") == 1.0

def test_similarity_3():
    assert round(jaro("test", "tester"), 2) == 0.89

def test_similarity_4():
    assert round(jaro("test", "tets"), 2) == 0.92