from datetime import date

class Person:
    @staticmethod
    def _alcohol_restrictions_to_buy():
        return [
            (18, 100.0),
            (16, 16.5),
        ]

    def allowed_to_buy_alcohol(self, birthday, alcohol_percentage):
        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

        for artb in self._alcohol_restrictions_to_buy():
            if age >= artb[0] and alcohol_percentage <= artb[1]:
                return True

        return False

    def allowed_to_buy_tobacco(self, birthday):
        pass

class Alcohol:
    @staticmethod
    def calc_unit(cl, percentage):
        if not isinstance(percentage, (int, float)):
            raise ValueError("percentage must be an int or float")
        if not isinstance(cl, (int, float)):
            raise ValueError("cl must be an int or float")
        if percentage > 100:
            raise ValueError("percentage must be <= 100")

        return round((cl * percentage) / (100 * 1.5), 2)

    @staticmethod
    def unit_to_gram(units):

        return round(units*12)