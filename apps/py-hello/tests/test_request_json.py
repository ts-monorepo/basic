import pytest
import json


def test_request_json(client, app):
    response = client.post('/json_example', data=json.dumps(
        {'name': 'hi', 'age': 23}), headers={"Content-Type": "application/json"})
    assert response.status_code == 200
