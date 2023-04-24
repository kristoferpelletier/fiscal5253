from datetime import date, timedelta
import calendar

class FiscalYear(date):
    exampleFiscalYear = None
    exampleStartDate = None
    exampleEndDate = None
    firstMonth = None

    @staticmethod
    def set_example(year: int, examplestart: date, exampleend: date):
        FiscalYear.exampleFiscalYear = year
        FiscalYear.exampleStartDate = examplestart
        FiscalYear.exampleEndDate = exampleend
        FiscalYear.firstMonth = examplestart.month

    def weekday(self):
        # Since this is a custom class, I want to have Saturday as the beginning of the week.
        return (super().weekday() + 2) % 7

    def __init__(self, year, month, day):
        self.dt = date(year, month, day)
        self.yr = year
        self.mnth = self.dt.month
        
    def LeapYearCheck(self):
        return self.yr % 4 == 0 and (self.yr % 100 != 0 or self.yr % 400 == 0)
        
    def get_fiscal_year(self):
        thisyear = self.yr
        lastyear = thisyear - 1
    
    def weeksInTheYear(self):
        weekday = self.weekday()
        leapyear = self.LeapYearCheck()

        if weekday == 2 and leapyear or weekday == 3 and not leapyear:
            return 53
        else:
            return 52
        





fy = FiscalYear(2021, 2, 1)
fy.set_example(2022, date(2022,1,29), date(2023,2,3))

print(fy.dt)
print(fy.weekday())
print(fy.weeksInTheYear())