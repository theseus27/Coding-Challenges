def NumDaysBetween(year1, month1, day1, year2, month2, day2):
    days_passed = 0
    #Subtract days passed in earlier year
    days_passed -= day1
    for month in range(1, month1):
        days_passed -= DaysInMonth(month, year1)
    #Add all full years starting w/ earlier year up to not including later year
    for year in range(year1, year2):
        for month in range(1, 13):
            days_passed += DaysInMonth(month, year)
    #Add days passed in later year
    days_passed += day2
    for month in range(1, month2):
        days_passed += DaysInMonth(month, year2)
        
    return days_passed