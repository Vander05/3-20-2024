import datetime

def count_business_days(start_date, end_date):
    business_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday to Friday are considered business days
            business_days += 1
        current_date += datetime.timedelta(days=1)

    return business_days

# Example usage
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 1, 31)
num_business_days = count_business_days(start_date, end_date)
print("Number of business days:", num_business_days)