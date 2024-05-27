from jaro_winkler import jaro_winkler

def test_similarity_1():
    assert jaro_winkler("test", "") == 0.0

def test_similarity_2():
    assert jaro_winkler("test", "test") == 1.0

def test_similarity_3():
    assert round(jaro_winkler("test", "tester"), 2) == 0.92

def test_similarity_4():
    assert round(jaro_winkler("test", "tets"), 2) == 0.93