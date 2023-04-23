from datetime import date, timedelta
import calendar

class FiscalYear:
    exampleFiscalYear = None
    exampleStartDate = None
    exampleEndDate = None

    @staticmethod
    def set_example(year: int, examplestart: date, exampleend: date):
        FiscalYear.exampleFiscalYear = year
        FiscalYear.exampleStartDate = examplestart
        FiscalYear.exampleEndDate = exampleend

    def __init__(self, dt: date):
        self.dt = dt
        self.yr = dt.year
        self.mnth = dt.month
        
    def LeapYearCheck(self):
        if (self.yr % 4) == 0: 
            if (self.yr % 100) == 0: 
                if (self.yr % 400) == 0: 
                    return True
                else: 
                    return False
            else: 
                return True
        else: 
            return False
        
    def get_fiscal_year(self):
        thisyear = self.yr
        lastyear = thisyear - 1
        
        