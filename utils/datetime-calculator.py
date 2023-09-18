import pytz
from datetime import datetime

datetime_format = "%Y-%m-%d %H:%M"

timezones_dict = {
    "PST": "US/Pacific",
    "EDT": "US/Eastern",
    "CST": "Asia/Shanghai",
}


def convert_to_cst():
    print("== Convert datetime to CST ==")
    datetime_input = input("Enter datetime (such as PST 2023-09-20 07:00), seperated by comma: ").split(",")
    for current in datetime_input:
        current = current.strip()
        time_zone, date_input = current.split(" ", 1)
        input_datetime = datetime.strptime(date_input, datetime_format)
        input_timezone = pytz.timezone(timezones_dict[time_zone])
        output_timezone = pytz.timezone(timezones_dict['CST'])
        converted_datetime = input_timezone.localize(input_datetime).astimezone(output_timezone)
        print(
            f"{str(input_timezone): <13} -> {str(output_timezone): <14}: {converted_datetime.strftime(datetime_format)}"
        )


def convert_cst_to_all():
    print("== Convert datetime from CST ==")
    datetime_input = input("Enter datetime in CST (such as 2023-09-20 07:00): ")
    input_datetime = datetime.strptime(datetime_input, datetime_format)
    input_timezone = pytz.timezone(timezones_dict['CST'])
    for key, value in timezones_dict.items():
        output_timezone = pytz.timezone(value)
        converted_datetime = input_timezone.localize(input_datetime).astimezone(output_timezone)
        print(f"{str(output_timezone): <14}: {converted_datetime.strftime(datetime_format)}")


if __name__ == '__main__':
    mode = input("Please enter mode (f: convert to CST, b: convert from CST): ")
    if mode == 'f':
        convert_to_cst()
    elif mode == 'b':
        convert_cst_to_all()

