LOAD_FATIGUE = 2000


def test_insert(client):
    client.index("document_1 Some text that I want to index")
    client.index("document_2 Some other text that I want to index")
    result = client.search("text")

    assert 2 == len(result)
    assert "document_1" in result
    assert "document_2" in result


def test_many_items(client):
    for _ in range(LOAD_FATIGUE):
        client.index(f"doc_{_} {_}")

    for _ in range(LOAD_FATIGUE):
        assert len(client.search(_)) == 1


def test_long_text(client):
    long_text = (
        LOAD_FATIGUE
        * "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"  # noqa
    )
    client.index(f"INDEX0 {long_text}")

    client.index(f'INDEX1 {long_text.replace("a", "e")}')
    search1 = client.search("perspiciatis")
    search2 = client.search("perspicietis")
    assert len(search1) == 1
    assert len(search2) == 1
    assert "INDEX0" in search1
    assert "INDEX1" in search2


def test_version(client):
    result = client.version()
    assert len(result)
