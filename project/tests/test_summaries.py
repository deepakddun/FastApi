import json
import pytest


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries", data=json.dumps({"url": "https://foo.bar"}))

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_read_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]
    print(f'The summary id is {summary_id}')
    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    print(response)
    assert response.status_code == 200

    response_dict = response.json()
    print(response_dict)
    response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"


def test_get_all_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_dict = response.json()
    print(response_dict)
    y = list(filter(lambda a: a["id"] == summary_id, response_dict))
    print(y)
