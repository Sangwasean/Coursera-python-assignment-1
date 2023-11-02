#question1

def seconds_difference(time_1, time_2):
    return time_2 - time_1


#question2

def hours_difference(time_1, time_2):

    return (time_2 - time_1) /3600

#question3

def to_float_hours(hours, minutes, seconds):

    if seconds > 59:
        minutes += seconds // 60
        seconds = seconds % 60

    if minutes > 59:
        hours += minutes // 60
        minutes = minutes % 60

    total_time = hours + (minutes / 60) + (seconds / 3600)

    return total_time

#question4

def to_24_hour_clock(hours):

    return hours % 24

def get_hours(seconds):
    hours= seconds // 3600
    return hours

def get_minutes(seconds):
    hours=seconds // 3600
    used_minutes=hours * 3600
    remained_minutes=(seconds -used_minutes)// 60
    return remained_minutes

def get_seconds(seconds):
    hours = seconds // 3600
    used_minutes = hours * 3600
    remained_seconds=(seconds - used_minutes) % 60
    return remained_seconds

#question5

def time_to_utc(utc_offset, time):
    time_in_24format = time - utc_offset
    result = to_24_hour_clock(time_in_24format)
    return result

def time_from_utc(utc_offset, time):
    time_in_24format = time + utc_offset
    result = to_24_hour_clock(time_in_24format)
    return result


