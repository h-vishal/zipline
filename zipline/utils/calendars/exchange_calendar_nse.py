# for setting our open and close times
from datetime import time
# for setting our start and end sessions
import pandas as pd
# for setting our timezone
from pytz import timezone

# for creating and registering our calendar
from zipline.utils.calendars import (
  TradingCalendar
)
from zipline.utils.memoize import lazyval


class NSEExchangeCalendar(TradingCalendar):
    """
    Exchange Calendar for NSE
    Open Time: 9:15 AM, Asia/Kolkata
    Close Time: 3:30 PM, Asia/Kolkata

    Regularly-Observed Holidays:
    - Republic Day
    - Mahashivratri
    - Holi
    - Ram Navami
    - Mahavir Jayanti
    - Good Friday
    - Dr.Baba Saheb Ambedkar Jayanti
    - Maharashtra Day
    - Id-Ul-Fitr (Ramzan ID)
    - Independence day
    - Bakri ID
    - Ganesh Chaturthi
    - Moharram
    - Mahatama Gandhi Jayanti
    - Dasera
    - Diwali-Laxmi Pujan
    - Diwali-Balipratipada
    - Gurunanak Jayanti
    - Christmas

    Additional Irregularities:
    - Closed on 4/24/2014 due to parliamentary elections
    - Closed on 10/15/2014 due to assembly elections

    These holidays are added using adhoc_holidays from a CSV file because a lot of them are based on the lunar calendar.
    TODO : Explore a better way to add holidays
    TODO : Make date format consistent in the holidays CSV file
    TODO : Add extra trading days from the extra days CSV file
    """

    @staticmethod
    def read_dates_from_file(path):
        file = open(path)
        dates = list(file)
        days = []
        for date in dates:
            days.append(pd.Timestamp(date, tz="utc"))
        return days
    
    @property
    def name(self):
        return "NSE"

    @property
    def tz(self):
        return timezone('Asia/Kolkata')

    @property
    def open_time(self):
        return time(9, 15)

    @property
    def close_time(self):
        return time(15, 30)

    @property
    def adhoc_holidays(self):
        return self.read_dates_from_file("./nse_holidays.csv")


