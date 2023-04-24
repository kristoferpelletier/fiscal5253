from datetime import date, timedelta
import calendar

class FiscalYear(date):
    exampleFiscalYear = None
    exampleStartDate = None
    exampleEndDate = None
    firstMonth = None
    firstWeekday = None

    @staticmethod
    def set_example(year: int, examplestart: date, exampleend: date):
        FiscalYear.exampleFiscalYear = year
        FiscalYear.exampleStartDate = examplestart
        FiscalYear.exampleEndDate = exampleend
        FiscalYear.firstMonth = examplestart.month
        FiscalYear.firstWeekday = examplestart.weekday()

    def weekday(self):
        # Since this is a custom class, I want to have Saturday as the beginning of the week.
        # I am also using the example to figure out when the first day of the week should be
        return (super().weekday() + 7 - self.firstWeekday) % 7
    
    def first_day_of_week(self):
        return self - timedelta(days=self.weekday())

    def end_of_previous_week(self):
        return self.first_day_of_week() - timedelta(days=1)
    
    def start_of_previous_week(self):
        return self.end_of_previous_week() - timedelta(days=6)

    def __init__(self, year, month, day):
        self.dt = date(year, month, day)
        self.yr = year
        self.mnth = self.dt.month
        
    def leap_year_check(self):
        return self.yr % 4 == 0 and (self.yr % 100 != 0 or self.yr % 400 == 0)
    
    def weeks_in_the_year(self):
        weekday = self.weekday()
        leapyear = self.leap_year_check()

        if weekday == 2 and leapyear or weekday == 3 and not leapyear:
            return 53
        else:
            return 52
        





fy = FiscalYear(2023, 4, 23)
fy.set_example(2022, date(2022,1,29), date(2023,2,3))

print(fy.dt)
print(fy.weekday())
print(fy.weeks_in_the_year())
print(fy.first_day_of_week())
print(fy.end_of_previous_week())
print(fy.start_of_previous_week())