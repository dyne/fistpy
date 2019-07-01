LOAD_FATIGUE = 10


def test_insert(client):
    client.index("document_1 Some text that I want to index")
    client.index("document_2 Some other text that I want to index")
    result = client.search("text")

    print(len(result), result)  # 2 ['document_1', 'document_2']

    assert 2 == len(result)
    assert "document_1" in result
    assert "document_2" in result


def test_many_items(client):
    for _ in range(LOAD_FATIGUE):
        client.index(f"doc_{_} {_}")

    for _ in range(LOAD_FATIGUE):
        assert len(client.search(_))

def test_version(client):
    result = client.version()
    print(len(result), result)
    assert(len(result))



