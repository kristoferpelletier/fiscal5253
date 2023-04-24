from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import calendar

class FiscalYear(date):
    exampleFiscalYear = None
    exampleStartDate = None
    exampleEndDate = None
    firstMonth = None
    firstWeekday = None

    @staticmethod
    def set_example(year: int, examplestart: date, exampleend: date, firstfiscalmonth: int):
        FiscalYear.exampleFiscalYear = year
        FiscalYear.exampleStartDate = examplestart
        FiscalYear.exampleEndDate = exampleend
        FiscalYear.firstMonth = firstfiscalmonth
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
        self.lastyear = year - 1
        self.sameDateLastYear = self.dt - relativedelta(years=1)
        
    def leap_year_check(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def weeks_in_the_prior_year(self):
        weekday = (date(self.lastyear, self.firstMonth, 1).weekday() + 7 - self.firstWeekday) % 7
        print(f'theweekday method in weeks in the prior year is {weekday}')
        leapyear = self.leap_year_check(self.lastyear)

        if weekday == 2 and leapyear or weekday == 3 and not leapyear:
            return 53
        else:
            return 52
        
    def smallest_day_in_first_month_first_week(self):

        firstOfFirstMonth = date(self.year, self.firstMonth, 1)
        firstMonthFirstWeekday = firstOfFirstMonth.weekday()

        firstday = 1

        if (firstMonthFirstWeekday >= 3 and  firstMonthFirstWeekday <= 5) or self.weeks_in_the_prior_year() == 53:
            firstday += (5 - firstMonthFirstWeekday)
        return firstday

    def first_of_fiscal_year(self):
        pass


    def fiscal_year(self):
        pass





fy = FiscalYear(2024, 4, 23)
fy.set_example(2022, date(2022,1,29), date(2023,2,3), 2)

print(fy.dt)
print(fy.weekday())
print(fy.weeks_in_the_prior_year())
print(fy.first_day_of_week())
print(fy.end_of_previous_week())
print(fy.start_of_previous_week())

print(fy.smallest_day_in_first_month_first_week())