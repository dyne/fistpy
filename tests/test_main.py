from fist.client import Fist


def test_insert():
    f = Fist(host="localhost", port=5575)
    f.index("document_1 Some text that I want to index")
    f.index("document_2 Some other text that I want to index")
    result = f.search("text")

    print(len(result), result)  # 2 ['document_1', 'document_2']

    assert 2 == len(result)
    assert "document_1" in result
    assert "document_2" in result
