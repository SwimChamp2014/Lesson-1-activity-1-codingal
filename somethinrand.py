import calendar

# Display the names of the months
for month in calendar.month_name:
    if month:  # Skip the empty string at index 0
        print(month)