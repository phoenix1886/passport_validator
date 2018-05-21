from datetime import date
from dateutil.relativedelta import relativedelta
from parser import parse_arguments


def get_birtday_date(date_of_birth, age):
    return date_of_birth + relativedelta(years=age)


def get_passport_expiration_date(date_of_birth, date_of_passport_issue):
    if date_of_passport_issue < get_birtday_date(date_of_birth, age=20):
        return (
            get_birtday_date(date_of_birth, age=20)
            + relativedelta(months=1)
        )
    elif date_of_passport_issue < get_birtday_date(date_of_birth, age=45):
        return (
            get_birtday_date(date_of_birth, age=45)
            + relativedelta(months=1)
        )
    else:
        return None


def is_passport_fake(
        date_of_birth,
        date_of_passport_issue,
        date_of_validation_check=date.today()
):
    if (date_of_passport_issue < get_birtday_date(date_of_birth, age=14) or
            date_of_birth > date_of_validation_check or
            date_of_passport_issue > date_of_validation_check):
        return True
    return False


def is_passport_valid(
        date_of_birth,
        date_of_passport_issue,
        date_of_validation_check=date.today()
):
    if is_passport_fake(
        date_of_birth,
        date_of_passport_issue,
        date_of_validation_check
    ):
        return False

    passport_expiration_date = get_passport_expiration_date(
        date_of_birth,
        date_of_passport_issue
    )
    if not passport_expiration_date:
        return True
    if date_of_validation_check >= passport_expiration_date:
        return False
    return True


if __name__ == '__main__':
    arguments = parse_arguments()
    validation_status = is_passport_valid(
        arguments.date_of_birth,
        arguments.date_of_passport_issue,
        date_of_validation_check=arguments.date_of_validation_check
    )
    print(validation_status)
