from flask_testing import TestCase

from project import app
from project.parser.controler import ParsingControler
from project.parser.models import db
from project.parser.word_files_handler.initial_data_handlers import FiletoDbHandler


class TestParsingControler(TestCase):
    def create_app(self):
        app.config.from_object("config.TestConfig")
        return app

    def setUp(self):
        self.in_string = "Salut GrandPy ! Est-ce que tu connais l'adresse d'Openclassrooms à Paris ?"
        db.create_all()
        for key in app.config["DATA_LOAD_CONFIG"].keys():
            FiletoDbHandler(db, key)()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_controler(self):
        controler = ParsingControler(self.in_string)
        result = controler.out_list
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Openclassrooms", result)
        self.assertEqual(result[0], "Openclassrooms")


    def test_second_controller(self):
        self.in_string= "Je paris que tu ne sais pas où se trouve Saint-Étienne"
        controler = ParsingControler(self.in_string)
        result = controler.out_list
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Saint-Étienne", result)
        self.assertEqual(result[0], "Saint-Étienne")