from datetime import date

print("Days Calculator")
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

today = date.today()

years_lived = today.year - year
total_days = (years_lived * 365) + (years_lived // 4)

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


for i in range(today.month - 1):
    total_days += days_in_months[i]
total_days += today.day


for i in range(month - 1):
    total_days -= days_in_months[i]
total_days -= day

print(f"Total days: {total_days}")
