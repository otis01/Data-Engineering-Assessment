import unittest
from data_exporter import functions


class TestDataExporterFunctions(unittest.TestCase):

    dummy_dict_item = {"name": "test", "number": 1}
    dummy_iterator = [
        {"name": "test_1", "number": 1},
        {"name": "test_2", "number": 2},
        {"name": "test_3", "number": 3}
    ]

    def test_convert_row_to_json(self):
        """ Tests whether a Python dict gets correctly converted to a JSON string. """

        converted_json = functions.convert_row_to_json(self.dummy_dict_item)
        self.assertEqual(converted_json, """{"name":"test","number":1}""")

    def test_combine_results_into_a_json_list(self):
        """ Tests whether an iterator of dicts gets correctly converted to a list in JSON format. """

        converted_results = functions.combine_results_into_one_list(self.dummy_iterator)
        self.assertEqual(
            converted_results.__next__(),
            """[{"name":"test_1","number":1},{"name":"test_2","number":2},{"name":"test_3","number":3}]"""
        )

    def test_combine_results_into_individual_jsons(self):
        """ Tests whether an iterator of dicts gets correctly converted into individual JSONs. """

        converted_results = functions.combine_results_into_individual_jsons(self.dummy_iterator)
        self.assertEqual(converted_results.__next__(), """{"name":"test_1","number":1}""")
        self.assertEqual(converted_results.__next__(), """{"name":"test_2","number":2}""")
        self.assertEqual(converted_results.__next__(), """{"name":"test_3","number":3}""")

    def test_combine_results_into_a_json_key_value(self):
        """ Tests whether an iterator of dicts gets correctly converted a single JSON (dictionary). """

        converted_results = functions.combine_results_into_a_json_key_value(self.dummy_iterator)
        self.assertEqual(
            converted_results.__next__(),
            """{"test_1":1,"test_2":2,"test_3":3}"""
        )


if __name__ == '__main__':
    unittest.main()
