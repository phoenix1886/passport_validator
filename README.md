# Passport validator service
The function `is_passport_valid` produces passport validation.
In Russia, the first passport is given at the age of 14.
When one achieves 20 or 45 years old, he must renew passport in one month.
So, old passports are valid only one month after the birthday of 20 and 45 y.o.
Example: If citizen gets 20 years old at 01.01.2018, he must renew passport in one month.
So, at 01.02.2018, his old passport is expired, but at at 31.01.2018 it is
still valid.
This script validates passports, using this logic.

To run the script, one should have python 3.6 installed.
All side packages are listed in requirements.txt. One can install
necessary packages, using the following command:
```
pip install -r requirements.txt
```

One can you console application, or import `is_passport_valid` function.

## How to you console application
Console script takes 3 arguments (all dates in the format DD.MM.YYYY):
* date_of_bith (positional): the date of birth of passport owner ,
* date_of_passport_issue (positional): the date of passport issuance,
* -dv, --date_of_validation_check (optional): the date of validation,
 by default, it is today date. Thus, the script can validate passports
 retrospectively.
Validation status (True for valid, False for expired passports) is
returned.
### Example of use
```
$ python passport_validator.py 01.01.2000 01.01.2013
False
$ python passport_validator.py 01.01.2000 01.01.2014
True
$ python passport_validator.py 01.01.2000 01.01.2014 -dv 01.02.2020
False
$ python passport_validator.py 01.01.2000 01.01.2014 -dv 01.01.2020
True
```

## How to import
```
from passport_validator import is_passport_valid
```

## How to use
The function `is_passport_valid` takes 3 arguments:
* date_of_bith: the date of birth of passport owner,
* date_of_passport_issue: the date of passport issuance,
* date_of_validation_check (optional): the date of validation,
 by default, it is today date. Thus, the script can validate passports
 retrospectively.

### Example (results actual for 21.05.2018)
```
from passport_validator import is_passport_valid
from datetime import date

is_passport_valid(
    date_of_birth=date(2000, 1, 1),
    date_of_passport_issue=date(2014, 1, 15)
)
Out[6]: True

is_passport_valid(
    date_of_birth=date(1998, 1, 1),
    date_of_passport_issue=date(2012, 1, 15)
)
Out[7]: False

is_passport_valid(
    date_of_birth=date(1998, 1, 1),
    date_of_passport_issue=date(2012, 1, 15),
    date_of_validation_check=date(2018, 1, 31)
)
Out[8]: True
```

## How to run tests:
```
$ python tests.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK
```

The project is made for educational purposes only.
