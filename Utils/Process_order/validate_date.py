import datetime


def validate_date(initial_date: str, final_date: str) -> tuple:
    if initial_date is None:
        initial_date = datetime.datetime.strptime("2000-01-01", '%Y-%m-%d')
    else:
        initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')

    if final_date is None:
        final_date = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d')
    else:
        final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')

    return initial_date, final_date