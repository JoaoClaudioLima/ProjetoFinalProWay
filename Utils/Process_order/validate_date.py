import datetime


def validate_date(initial_date: str, final_date: str) -> tuple:
    if initial_date is None:
        initial_date = datetime.datetime.strptime("2000-01-01 08:36:39.621017", "%Y-%m-%d %H:%M:%S.%f")
    else:
        initial_date = datetime.datetime.strptime((f"{initial_date}"+" 00:00:00.621017"), '%Y-%m-%d %H:%M:%S.%f')

    if final_date is None:
        final_date = datetime.datetime.today()
    else:
        final_date = datetime.datetime.strptime((f"{final_date}"+" 23:59:59.999999"), '%Y-%m-%d %H:%M:%S.%f')

    return initial_date, final_date