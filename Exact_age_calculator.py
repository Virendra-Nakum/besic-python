from datetime import date

try:

    day = int(input("Enter Your Birth Date:- "))
    month = int(input("Enter Your Birth Month:- "))
    year = int(input("Enter Your Birth Year:- "))

    if day < 1 or day > 31:
        print("Date must be between 1 and 31.")

    elif month < 1 or month > 12:
        print("Month must be between 1 and 12.")

    else:

        dob = date(year, month, day)
        today = date.today()

        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day


        if days < 0:

            months -= 1

            if today.month == 1:
                previous_month = 12
                previous_year = today.year - 1

            else:
                previous_month = today.month - 1
                previous_year = today.year

            days += (
                date(previous_year, previous_month + 1, 1)
                - date(previous_year, previous_month, 1)
            ).days


        if months < 0:

            years -= 1
            months += 12


        print("---------- AGE CALCULATOR ----------")

        print("Birth Date   :", dob)
        print("Today Date   :", today)
        print(
            "Exact Age    :",
            years,
            "Years",
            months,
            "Months",
            days,
            "Days"
        )

except  :
    print("Please Enter Valid Date.")