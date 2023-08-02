import datetime

date_str = "12/12/2023"

date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
converted_date_str = date_obj.strftime("%Y-%m-%d")

print(converted_date_str)  # Output: 2023/12/12
