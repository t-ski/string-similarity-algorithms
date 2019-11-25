from szymkiewicz_simpson import szymkiewicz_simpson

def test_similarity_1():
    assert szymkiewicz_simpson("test", "") == 0.0

def test_similarity_2():
    assert szymkiewicz_simpson("test", "test") == 1.0

def test_similarity_3():
    assert szymkiewicz_simpson("test", "tester") == 1.0

def test_similarity_4():
    assert szymkiewicz_simpson("test", "tets") == 0.5