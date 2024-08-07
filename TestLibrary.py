import unittest
from Person_calc import Person, Alcohol
from datetime import datetime, date

class TestAllowedToBuyAlcohol(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_date_str = '2002-10-16'
        self._person = Person()
        self.__alcohol = Alcohol()

    def tearDown(self) -> None:
        del self._person
        del self.__alcohol

    @staticmethod
    def convert_str_to_datetime(date_str, age_limit=None):
        today = date.today()
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        age = today.year - dt.year - ((today.month, today.day) < (dt.month, dt.day))

        if age_limit and age > age_limit:
            add_years = age - age_limit
            dt = dt.replace(year=dt.year + add_years)
        print(dt)

        return dt

    def test_age_are_too_low_to_buy(self):
        self.convert_str_to_datetime('2002-10-16', 15)
        self.assertEqual(False, self._person.allowed_to_buy_alcohol(self.convert_str_to_datetime(self.__test_date_str, age_limit=15), 4.6))
        self.assertEqual(False, self._person.allowed_to_buy_alcohol(self.convert_str_to_datetime(self.__test_date_str, age_limit=17), 30.6))

    def test_age_its_allowed_to_buy(self):
        self.assertEqual(True, self._person.allowed_to_buy_alcohol(self.convert_str_to_datetime(self.__test_date_str, age_limit=16), 4.6))

    def test_alcohol_calc_units(self):
        self.assertEqual(1.01, self.__alcohol.calc_unit(cl=33, percentage=4.6))
        self.assertEqual(6.6, self.__alcohol.calc_unit(cl=33, percentage=20))
        self.assertEqual(22.0, self.__alcohol.calc_unit(cl=33, percentage=100))

        with self.assertRaises(ValueError):
            self.__alcohol.calc_unit(cl=30, percentage=110)
            self.__alcohol.calc_unit(cl=30, percentage="type is wrong")
            self.__alcohol.calc_unit(cl=None, percentage=50)
            self.__alcohol.calc_unit(cl='cl in str', percentage=50)

    def test_convert_unit_to_gram(self):
        self.assertEqual(8, self.__alcohol.unit_to_gram(units=1))
        self.assertEqual(12, self.__alcohol.unit_to_gram(units=1.5))
        self.assertEqual(30, self.__alcohol.unit_to_gram(units=3.75))

if __name__ == '__main__':
    unittest.main()
