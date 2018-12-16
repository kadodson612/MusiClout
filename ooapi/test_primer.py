import unittest
import requests
import json

class TestCherrypyPrimer(unittest.TestCase):

        SITE_URL = 'http://student04.cse.nd.edu:52052' #Replace this with your port number 52MMM 
        #where MMM is your assigned MID in 3 digits like 091 or 111, only use your MID, no one else's
        
        DICT_URL = SITE_URL + '/dictionary/'

        def reset_data(self):
                r = requests.delete(self.DICT_URL)

        def is_json(self, resp):
                try:
                        json.loads(resp)
                        return True
                except ValueError:
                        return False

        def test_dict_get(self):
                self.reset_data()
                key = 'paradigms'
                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

        def test_dict_put(self):
                self.reset_data()
                key = 'paradigms'

                m = {}
                m['value'] = '2018'
                r = requests.put(self.DICT_URL + key, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['value'], m['value'])

        def test_dict_delete(self):
                self.reset_data()
                key = 'paradigms'

                m = {}
                m['value'] = '2018'
                r = requests.put(self.DICT_URL + key, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.delete(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

        def test_dict_index_get(self):
                self.reset_data()

                key = 'paradigms'
                m = {}
                m['value'] = '2018'
                r = requests.put(self.DICT_URL + key, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                entries = resp['entries']
                mkv = entries[0]
                self.assertEqual(mkv['key'], key)
                self.assertEqual(mkv['value'], m['value'])

        def test_dict_index_post(self):
                self.reset_data()

                m = {}
                m['key'] = 'paradigms'
                m['value'] = '2018'

                r = requests.post(self.DICT_URL, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                entries = resp['entries']
                mkv = entries[0]
                self.assertEqual(mkv['key'], m['key'])
                self.assertEqual(mkv['value'], m['value'])

if __name__ == "__main__":
        unittest.main()

