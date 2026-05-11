import unittest

from fastapi.testclient import TestClient

from main import app


class StaticFrontendTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_root_serves_index_html(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("FastAPI Static Frontend", response.text)

    def test_static_css_is_served(self) -> None:
        response = self.client.get("/styles.css")

        self.assertEqual(response.status_code, 200)
        self.assertIn("text/css", response.headers.get("content-type", ""))


if __name__ == "__main__":
    unittest.main()
