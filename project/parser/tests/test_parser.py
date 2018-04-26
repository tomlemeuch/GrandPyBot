from flask_testing import TestCase

from project import app
from project.parser.models import db
from project.parser.parsers import LegacyParser, StopWordsParser, FrenchWordsParser, NonLettersParser, CitiesParser, \
    CountriesParser
from project.parser.word_files_handler.initial_data_handlers import FiletoDbHandler


class TestLegacyParser:

    def setup_method(self):
        self.in_string = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

    def teardown_method(self):
        pass

    def test_parse_string(self):
        parser = LegacyParser(self.in_string)
        assert isinstance(parser.out_list, list)
        assert parser.out_list == self.in_string.split(" ")
        assert "d'OpenClassrooms" in parser.out_list


class TestNonLettersParser:
    def setup_method(self):
        self.in_string = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

    def teardown_method(self):
        pass

    def test_parse_string(self):
        parser = NonLettersParser(self.in_string)
        assert isinstance(parser.out_list, list)
        assert parser.out_list != self.in_string
        assert len(self.in_string) > len(parser.out_list)
        assert "OpenClassrooms" in parser.out_list


class TestStopWordsParser(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.key = "stop_words"
        db.create_all()
        FiletoDbHandler(db, self.key)()
        self.in_string = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.in_list = NonLettersParser(self.in_string).out_list

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_parse_string(self):
        parser = StopWordsParser(self.in_string)
        assert isinstance(parser.out_list, list)
        assert parser.out_list != self.in_list
        assert len(self.in_list) > len(parser.out_list)
        assert "OpenClassrooms" in parser.out_list


class TestFrenchWordsParser(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.key = "french_words"
        db.create_all()
        FiletoDbHandler(db, self.key)()
        self.in_string = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        self.in_list = NonLettersParser(self.in_string).out_list

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_parse_string(self):
        parser = FrenchWordsParser(self.in_string)
        assert isinstance(parser.out_list, list)
        assert parser.out_list != self.in_list
        assert len(self.in_list) > len(parser.out_list)
        assert "OpenClassrooms" in parser.out_list


class TestCitiesParser(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.key = "cities"
        db.create_all()
        FiletoDbHandler(db, self.key)()
        self.in_string = "Bonjour vieille branche  ! Que peux-tu me dire sur Budapest ?"
        self.in_list = NonLettersParser(self.in_string).out_list

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_parse_string(self):
        parser = CitiesParser(self.in_string)
        assert isinstance(parser.out_list, list)
        assert parser.out_list != self.in_list
        assert len(self.in_list) > len(parser.out_list)
        assert "Budapest" in parser.out_list


class TestCountriesParser(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        self.key = "countries"
        db.create_all()
        FiletoDbHandler(db, self.key)()
        self.in_string = "Ola  ! Que sais-tu du Japon ?"
        self.in_list = NonLettersParser(self.in_string).out_list

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_parse_string(self):
        parser = CountriesParser(self.in_string)
        assert isinstance(parser.out_list, list)
        assert parser.out_list != self.in_list
        assert len(self.in_list) > len(parser.out_list)
        assert "Japon" in parser.out_list

# class TestLastWordParser:
#     pass
