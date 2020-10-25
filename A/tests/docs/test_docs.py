import requests


def test_get_docs(app):
    r = requests.get("http://localhost:4567/docs")
    assert r.status_code == 200 and "<html><head><meta http-equiv='content-language' content='en-us'>" in r.text
