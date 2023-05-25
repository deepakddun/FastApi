from app import main


# class TestFoo:
#
#     def test_bar(self):
#         assert "foo" != "bar"
def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": False}
