import requests
import json
import unittest

data1 = {
        'nazev2': {
            'id': 2,
            'column1': 'data3'
        }
    }

data = [
    {
        'nazev1': {
            'id': 1,
            'column1': 'data1',
            'column2': 'data2'
        }
    },
    {
        'nazev1': {
            'id': 2,
            'nazev': 'Výprodej 2018',
            'obrazek_id': 4,
            'products_ids': [
                1,
                2,
                3,
                4,
                5
            ],
            'attributes_ids': [
                2,
                4,
                21,
                23
            ]
        }
    },
    data1
]


class TestIntegrationMethods(unittest.TestCase):
    def test_integration(self):
        payload = json.dumps(data)
        # import test
        url = ('http://127.0.0.1:8000/api/import/')
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=payload, headers=headers)

        self.assertEqual(response.status_code, 201)

        # get test1
        url = ('http://127.0.0.1:8000/api/detail/nazev2/')
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url, headers=headers)
        self.assertEqual([data1], response.json())

        # get test2
        url = ('http://127.0.0.1:8000/api/detail/nazev2/2')
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url, headers=headers)
        self.assertEqual([data1], response.json())

        # get test3
        url = ('http://127.0.0.1:8000/api/detail/nazev1/')
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url, headers=headers)
        self.assertEqual([data[0], data[1]], response.json())

        # get no data
        url = ('http://127.0.0.1:8000/api/detail/test1/')
        headers = {'Content-Type': 'application/json'}

        response = requests.get(url, headers=headers)
        self.assertEqual([], response.json())

if __name__ == '__main__':
    unittest.main()
