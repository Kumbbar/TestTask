import unittest
from exceptions import *
from validation.validation import _validate_title, _validate_key, _validate_keys, _validate_longitude, \
    _validate_latitude, _validate_all_data, _validate_titles_keys


class TestValidation(unittest.TestCase):
    maxDiff = 4000

    def test__validate_title1(self):
        try:
            _validate_title("")
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_title2(self):
        try:
            _validate_title("12345670" * 19)
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_title3(self):
        try:
            _validate_title("Normal name")
        except InvalidValueError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_longitude1(self):
        try:
            _validate_longitude(-181)
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_longitude2(self):
        try:
            _validate_longitude("wedweded")
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_longitude3(self):
        try:
            _validate_longitude(181)
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_longitude4(self):
        try:
            _validate_longitude(22.9675)
        except InvalidValueError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_latitude1(self):
        try:
            _validate_latitude(-91)
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_latitude2(self):
        try:
            _validate_latitude("kjoiu88uh")
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_latitude3(self):
        try:
            _validate_latitude(91)
        except InvalidValueError as e:
            self.assertEqual(type(e), InvalidValueError)
        else:
            self.fail()

    def test__validate_latitude4(self):
        try:
            _validate_latitude(66.9966)
        except InvalidValueError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_key1(self):
        try:
            _validate_key(['wefffs'])
        except InvalidKeyError as e:
            self.assertEqual(type(e), InvalidKeyError)
        else:
            self.assertTrue(True)

    def test__validate_key2(self):
        try:
            _validate_key(['title'])
        except InvalidKeyError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_key3(self):
        try:
            _validate_key(['title', 'another_key'])
        except InvalidKeyError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_keys1(self):
        try:
            _validate_keys(['title', 'longitude', 'latitude'])
        except InvalidKeysError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_keys2(self):
        try:
            _validate_keys(['title', 'latitude'])
        except InvalidKeysError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_keys3(self):
        try:
            _validate_keys(['title', 'asfdfdf', 'latitude'])
        except InvalidKeysError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_keys4(self):
        try:
            _validate_keys([])
        except InvalidKeysError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_all_data1(self):
        try:
            _validate_all_data('Moskow', 123.431, 67.2341)
        except InvalidValueError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_all_data2(self):
        try:
            _validate_all_data('Moskow', 123.431)
        except InvalidValueError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_all_data3(self):
        try:
            _validate_all_data('', 123.431, 67.2341)
        except InvalidValueError:
            self.assertTrue(True)

        else:
            self.fail()

    def test__validate_all_data4(self):
        try:
            _validate_all_data('', 190.431, 67.2341)
        except InvalidValueError:
            self.assertTrue(True)

        else:
            self.fail()

    def test__validate_titles_keys1(self):
        try:
            _validate_keys([])
        except InvalidKeysError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_titles_keys2(self):
        try:
            _validate_titles_keys(['first_object_title', 'second_object_title'])
        except InvalidKeysError:
            self.fail()
        else:
            self.assertTrue(True)

    def test__validate_titles_keys3(self):
        try:
            _validate_titles_keys(['first_odgbcbvbsdf_title', 'second_object_title'])
        except InvalidKeysError:
            self.assertTrue(True)
        else:
            self.fail()

    def test__validate_titles_keys4(self):
        try:
            _validate_titles_keys(['first_object_title'])
        except InvalidKeysError:
            self.assertTrue(True)
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
