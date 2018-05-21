import unittest
from datetime import date
from passport_validator import is_passport_valid


class TestPassportValidators(unittest.TestCase):

    def test_age_less_than_14(self):
        date_of_birth = date(2000, 1, 1)
        date_of_passport_issue = date(2010, 1, 1)
        date_of_validation_check = date(2010, 1, 1)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_validation_check = date(2010, 1, 2)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_age_14(self):
        date_of_birth = date(2000, 1, 1)
        date_of_passport_issue = date(2014, 1, 1)
        date_of_validation_check = date(2014, 1, 1)
        self.assertTrue(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_passport_issue_date_at_13_years_old(self):
        date_of_birth = date(2000, 1, 1)
        date_of_passport_issue = date(2013, 1, 1)
        date_of_validation_check = date(2018, 5, 21)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_passport_issue = date(2013, 12, 31)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_passport_issue_date_from_future_date(self):
        date_of_birth = date(2000, 1, 1)
        date_of_passport_issue = date(2020, 1, 1)
        date_of_validation_check = date(2018, 5, 21)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_birth_date_from_future(self):
        date_of_birth = date(2020, 1, 1)
        date_of_passport_issue = date(2040, 1, 1)
        date_of_validation_check = date(2018, 5, 21)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_passport_issue = date(2010, 1, 1)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_1_month_after_birthday(self):
        date_of_birth = date(2000, 1, 1)
        date_of_passport_issue = date(2014, 1, 10)
        date_of_validation_check = date(2020, 1, 1)
        self.assertTrue(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_validation_check = date(2020, 2, 1)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_passport_issue = date(2020, 2, 1)
        date_of_validation_check = date(2045, 1, 1)
        self.assertTrue(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_validation_check = date(2045, 2, 1)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_age_after_45(self):
        date_of_birth = date(2000, 1, 1)
        date_of_passport_issue = date(2045, 1, 10)
        date_of_validation_check = date(2060, 1, 1)
        self.assertTrue(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_validation_check = date(2120, 1, 1)
        self.assertTrue(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

    def test_leap_year(self):
        date_of_birth = date(2000, 2, 29)
        date_of_passport_issue = date(2020, 3, 1)
        date_of_validation_check = date(2045, 3, 27)
        self.assertTrue(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )
        date_of_validation_check = date(2045, 3, 28)
        self.assertFalse(
            is_passport_valid(
                date_of_birth,
                date_of_passport_issue,
                date_of_validation_check
            )
        )

if __name__ == '__main__':
    unittest.main()
