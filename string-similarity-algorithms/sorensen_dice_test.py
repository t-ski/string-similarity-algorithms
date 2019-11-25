from sorensen_dice import sorensen_dice

def test_similarity_1():
    assert sorensen_dice("test", "") == 0.0

def test_similarity_2():
    assert sorensen_dice("test", "test") == 1.0

def test_similarity_3():
    assert sorensen_dice("test", "tester") == 0.8

def test_similarity_4():
    assert sorensen_dice("test", "tets") == 0.5