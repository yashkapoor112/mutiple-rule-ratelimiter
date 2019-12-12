import datetime

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def get_datetime_object_from_string(date_time_str):
    return datetime.datetime.strptime(date_time_str, '%Y-%m-%d-%H:%M')

def get_difference_between_two_dates(date_first, date_second):
    return (date_first - date_second).total_seconds() // 3600

