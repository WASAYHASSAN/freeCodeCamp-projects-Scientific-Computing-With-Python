def add_time(start, duration, start_day=None):
    # Extract hours, minutes, and AM/PM from start time
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    # Convert start time to 24-hour clock
    if period == 'PM':
        start_hours += 12

    # Extract hours and minutes from duration time
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate total hours and minutes
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes
    if total_minutes >= 60:
        total_hours += 1
        total_minutes -= 60

    # Calculate days elapsed
    days_elapsed = total_hours // 24
    days_remaining_hours = total_hours % 24

    # Convert back to 12-hour clock
    if days_remaining_hours < 12:
        period = 'AM'
        if days_remaining_hours == 0:
            days_remaining_hours = 12
    else:
        period = 'PM'
        if days_remaining_hours > 12:
            days_remaining_hours -= 12

    # Format result time
    result_time = f"{days_remaining_hours:02d}:{total_minutes:02d} {period}"

    # Format days later string
    if days_elapsed == 1:
        days_later = " (next day)"
    elif days_elapsed > 1:
        days_later = f" ({days_elapsed} days later)"
    else:
        days_later = ""

    # Format result string
    result = result_time + days_later

    # Add day of week if specified
    if start_day:
        # Convert day of week to lower case and get index
        start_day_index = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"].index(start_day.lower())
        # Calculate new day of week index
        new_day_index = (start_day_index + days_elapsed) % 7
        # Get new day of week name
        new_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][new_day_index]
        result += f", {new_day}"

    return result

print(add_time("3:00 PM", "3:10"))
