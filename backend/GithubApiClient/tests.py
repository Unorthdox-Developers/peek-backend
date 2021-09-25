
import unittest
import api_callers

#unittest's
# SearchRepositories TestCase
class TestSearchRespositories(unittest.TestCase):

    def test_obj_attr_with_kwargs(self):
        pyld = {'q':'kleir'}
        obj = api_callers.SearchRepositories(pyld)
        self.assertTrue(isinstance(obj.payload,dict))

    def test_obj_with_args(self):
        pyld = ['q','kleir']
        obj = api_callers.SearchRepositories(pyld)
        self.assertIsNone(obj.payload)

    def test_validate_pyld_key(self):
        pyld = {'name':'kleir'}
        obj = api_callers.SearchRepositories(pyld)
        self.assertEqual('kleir',obj.payload['q'])

    def test_validate_all_pyld_keys(self):
        pyld = {'name':'kleir','language':'python'}
        obj = api_callers.SearchRepositories(pyld)
        self.assertEqual(2,len(obj.payload))

    def test_validate_requests_method_get(self):
        pyld = {'name':'kleir','language':'python','order':'asc'}
        obj = api_callers.SearchRepositories(pyld)
        data = obj.request_data()
        self.assertEqual(200,data.status_code)

    def test_validate_parser(self):
        pyld = {'name':'kleir','language':'python','order':'asc'}
        obj = api_callers.SearchRepositories(pyld)
        data = obj.parser()
        self.assertTrue(isinstance(data,tuple))


if __name__ == '__main__':
    unittest.main()
