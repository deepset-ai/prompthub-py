import requests
from unittest.mock import MagicMock
from prompthub.prompt import from_json, from_yaml, fetch, MAIN_ENDPOINT


def test_from_json(test_root):
    json_prompt = test_root / "fake_prompts" / "fake_prompt.json"
    p = from_json(str(json_prompt))
    assert p.name == "deepset/question-answering"
    assert p.tags == ["question-answering"]
    assert p.meta == {"authors": ["vblagoje"]}
    assert p.version == "v0.1.1"
    assert (
        p.text
        == "Given the context please answer the question. Context: {join(documents)};\n"
        "Question: {query};\n"
        "Answer:\n"
    )
    assert (
        p.description == "A simple prompt to answer a question given a set of documents"
    )


def test_from_yaml(test_root):
    yaml_prompt = test_root / "fake_prompts" / "fake_prompt.yml"
    p = from_yaml(str(yaml_prompt))
    assert p.name == "deepset/question-answering"
    assert p.tags == ["question-answering"]
    assert p.meta == {"authors": ["vblagoje"]}
    assert p.version == "v0.1.1"
    assert (
        p.text
        == "Given the context please answer the question. Context: {join(documents)};\n"
        "Question: {query};\n"
        "Answer:\n"
    )
    assert (
        p.description == "A simple prompt to answer a question given a set of documents"
    )


def test_fetch():
    p = fetch("deepset/question-answering")
    assert p.name == "deepset/question-answering"
    assert p.tags == ["question-answering"]
    assert p.meta == {"authors": ["vblagoje"]}
    assert p.version == "v0.1.1"
    assert (
        p.text
        == "Given the context please answer the question. Context: {join(documents)};\n"
        "Question: {query};\n"
        "Answer:\n"
    )
    assert (
        p.description == "A simple prompt to answer a question given a set of documents"
    )


def test_fetch_timeout(monkeypatch):
    mock_get = MagicMock()
    monkeypatch.setattr(requests, "get", mock_get)
    fetch("deepset/question-answering", timeout=1)
    mock_get.assert_called_with(f"{MAIN_ENDPOINT}/prompts/deepset/question-answering", timeout=1)
