import argparse
from datetime import datetime, date


def valid_date(string_date):
    try:
        return datetime.strptime(string_date, "%d.%m.%Y").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(string_date)
        raise argparse.ArgumentTypeError(msg)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'date_of_birth',
        help="Birth Date - format DD.MM.YYYY",
        type=valid_date
    )
    parser.add_argument(
        'date_of_passport_issue',
        help="Date of passport issuance - format DD.MM.YYYY",
        type=valid_date
    )
    parser.add_argument(
        '-dv',
        '--date_of_validation_check',
        help="Date of validation check - format DD.MM.YYYY",
        default=date.today(),
        type=valid_date
    )
    return parser.parse_args()
