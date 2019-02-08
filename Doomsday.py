month = input("Enter the month (mm): ")
month = int(month)
day = input("Enter the day (dd): ")
day = int(day)
year = input("Enter the year (yyyy): ")
year = int(year)
anchor_day = (5 * ((year//100)%4)) % 7 + 2
year2 = year - (year // 100) * 100
doomsday = ((year2 // 12) + (year2 % 12) + ((year2 % 12) // 4) + anchor_day) % 7
if (year % 4) == 0:
    if month == 1:
        week_day = (((day - 4) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 2:
        week_day = (((day - 29) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 3:
        week_day = (((day - 7) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 4:
        week_day = (((day - 4) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 5:
        week_day = (((day - 9) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 6:
        week_day = (((day - 6) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 7:
        week_day = (((day - 11) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 8:
        week_day = (((day - 8) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 9:
        week_day = (((day - 5) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 10:
        week_day = (((day - 10) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 11:
        week_day = (((day - 7) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 12:
        week_day = (((day -12) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    else:
        print("There was an error with this date")
else:
    if month == 1:
        week_day = (((day - 3) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 2:
        week_day = (((day - 28) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 3:
        week_day = (((day - 7) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 4:
        week_day = (((day - 4) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 5:
        week_day = (((day - 9) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 6:
        week_day = (((day - 6) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 7:
        week_day = (((day - 11) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 8:
        week_day = (((day - 8) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 9:
        week_day = (((day - 5) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 10:
        week_day = (((day - 10) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 11:
        week_day = (((day - 7) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    elif month == 12:
        week_day = (((day -12) % 7) + doomsday) % 7
        if week_day == 0:
            print("The day of the week for", month, "/", day, "/", year, "was Sunday")
        elif week_day == 1:
            print("The day of the week for", month, "/", day, "/", year, "was Monday")
        elif week_day == 2:
            print("The day of the week for", month, "/", day, "/", year, "was Tuesday")
        elif week_day == 3:
            print("The day of the week for", month, "/", day, "/", year, "was Wednesday")
        elif week_day == 4:
            print("The day of the week for", month, "/", day, "/", year, "was Thursday")
        elif week_day == 5:
            print("The day of the week for", month, "/", day, "/", year, "was Friday")
        else:
            print("The day of the week for", month, "/", day, "/", year, "was Saturday")
    else:
        print("There was an error with this date")
    
