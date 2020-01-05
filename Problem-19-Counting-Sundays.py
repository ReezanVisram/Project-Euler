# Project Euler Problem 19
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Initializing the days of each month in a dictionary which are used to determine which month the counter is in
monthDays = {"JANUARY":31, "FEBRUARY":28, "MARCH":31, "APRIL":30, "MAY":31, "JUNE":30, "JULY":31, "AUGUST":31, "SEPTEMBER":30, "OCTOBER":31, "NOVEMBER":30, "DECEMBER":31}

# Creating a list of days of the week to determine which week the counter is in
daysOfWeek = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

# Creating a list of months instead of using the dictionary (Getting months with index easier in list)
monthsOfYear = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

# Initializing the problem specifications
currYear = 1901
currMonth = "JANUARY"
currDay = 1
currDayOfWeek = daysOfWeek[1]
sundaysOnFirstDay = 0
monthIndex = 0
dayIndex = 1

# Looping through each year
while currYear < 2001:
    # Incrementing days and day of the week index
    currDay += 1
    dayIndex += 1

    # If the day becomes SATURDAY, reset it to SUNDAY
    if dayIndex > 6:
        dayIndex = 0

    # Check if a leap year
    if currYear % 4 == 0 and currYear != 1900:
        monthDays["FEBRUARY"] = 29

    # Loops through the dictionary to find how many days in each month
    for key in monthDays:
        if key == currMonth:
            # If the current day matches the limit of the current month, reset the day to 1
            if currDay == monthDays[key]:
                currDay = 1

                # If the month is not DECEMBER, increment it by 1
                try:
                    currMonth = monthsOfYear[monthIndex + 1]
                    monthIndex += 1

                # If the month is DECEMBER, reset the next month to  JANUARY
                except:
                    currMonth = monthsOfYear[0]
                    monthIndex = 0
                    currYear += 1

                # If the day is a SUNDAY, increment the counter
                if dayIndex == 0:
                    sundaysOnFirstDay += 1

    # Reset the month to JANUARY
    if monthIndex > 11:
        monthIndex = 0

    
    currMonth = monthsOfYear[monthIndex]

print(sundaysOnFirstDay)
    
