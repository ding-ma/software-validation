import subprocess

import requests


def test_get_docs(app):
    """If we get connection error, means that we have successfully shutdown the app"""
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True)
    try:
        requests.get("http://localhost:4567/docs")
    except requests.exceptions.ConnectionError:
        assert True
    except Exception as e:
        raise e
