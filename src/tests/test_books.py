import unittest
from main import create_app, db


class TestItems(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
        
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])
        
    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

        
    def test_item_index(self):
        app = create_app()
        client = app.test_client()
        response = client.get("/items/")
        
        data = response.get_json()
        
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(data, list)