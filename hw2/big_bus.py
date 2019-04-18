from datetime import date, timedelta
import calendar
from uuid import uuid4

class BigBus(object):

    # making up prices
    cheap = 25.00 # Mon, Tues, Wed, Thurs
    normal = 30.00 # Fri, Sat, Sun

    def __init__(self):
        self.red = 5 * 89
        self.green = 4 * 89
        self.blue = 2 * 89
        self.red_i = {}
        self.green_i = {}
        self.blue_i = {}

    def sell_ticket(self, year, month, day, route=None, amount=1):
        '''given a date, route and amount, will purchase tickets'''

        _date = date(year, month, day) # year-month-day
        day = calendar.day_name[_date.weekday()] # sun - sat

        #check if valid route
        if route not in ('red','blue','green'):
            print('please choose a valid route \"red\", \"blue\", \"green\"')
            return

        # check if more than 10 days ahead
        if _date > (date.today()+timedelta(days=10)) or _date < date.today():
            print("please choose a date from {} to {}".format(date.today(),(date.today()+timedelta(days=10))))
            return

        # check if amount is between 1 and 4
        if amount > 4 or amount < 1:
            print("please choose a valid ticket amount from 1 to 4")
            return

        else:
            # set the price
            price = BigBus.normal
            if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday'):
                price = BigBus.cheap

            #check if amount = 4 for discount
            if amount == 4:
                price = price * .9

            if route == 'red':
                if str(_date) in self.red_i:
                    if len(self.red_i[str(_date)]) > self.red - amount:
                        print('not enough tickets available for this day')
                        return
                    else:
                        for i in range(amount):
                            self.red_i[str(_date)].append((str(uuid4()),price))
                else:
                    self.red_i[str(_date)] = [(str(uuid4()),price)]
                    for i in range(amount-1):
                        self.red_i[str(_date)].append((str(uuid4()),price))

            if route == 'blue':
                if str(_date) in self.blue_i:
                    if len(self.blue_i[str(_date)]) > self.blue - amount:
                        print('not enough tickets available for this day')
                        return
                    else:
                        for i in range(amount):
                            self.blue_i[str(_date)].append((str(uuid4()),price))
                else:
                    self.blue_i[str(_date)] = [(str(uuid4()),price)]
                    for i in range(amount-1):
                        self.blue_i[str(_date)].append((str(uuid4()),price))

            if route == 'green':
                if str(_date) in self.green_i:
                    if len(self.green_i[str(_date)]) > self.green - amount:
                        print('not enough tickets available for this day')
                        return
                    else:
                        for i in range(amount):
                            self.green_i[str(_date)].append((str(uuid4()),price))
                else:
                    self.green_i[str(_date)] = [(str(uuid4()),price)]
                    for i in range(amount-1):
                        self.green_i[str(_date)].append((str(uuid4()),price))

            print('sold {} {} ticket(s) for ${:.2f} on {} {}'.format(amount, route, round(price*amount,2), day, _date))

    def refund_ticket(self, year, month, day, route, id):
        '''given a date, route and id, will attempt to refund and remove from database.'''

        _date = date(year, month, day)

        if route == 'red':
            for i in range(len(self.red_i[str(_date)])):
                if self.red_i[str(_date)][i][0] == id:
                    print('refunding {} back'.format(self.red_i[str(_date)][i][0]))
                    del self.red_i[str(_date)][i]
                    break

        if route == 'green':
            for i in range(len(self.green_i[str(_date)])):
                if self.green_i[str(_date)][i][0] == id:
                    print('refunding {} back'.format(self.green_i[str(_date)][i][0]))
                    del self.green_i[str(_date)][i]
                    break

        if route == 'blue':
            for i in range(len(self.blue_i[str(_date)])):
                if self.blue_i[str(_date)][i][0] == id:
                    print('refunding {} back'.format(self.blue_i[str(_date)][i][0]))
                    del self.blue_i[str(_date)][i]
                    break

    def report(self, today=False, route='red', year=date.today().year, month=date.today().month, day=date.today().day):

        '''return a report of tickets on a specific day'''

        try:
            if today:
                _date = str(date.today())
                count = 0
                if route == 'red':
                    for i in self.red_i[_date]:
                        count += 1
                if route == 'green':
                    for i in self.green_i[_date]:
                        count += 1
                if route == 'blue':
                    for i in self.blue_i[_date]:
                        count += 1
                print('{} {} route tickets sold on {}'.format(count, route, _date))

            else:
                count = 0
                _date = str(date(year, month, day))  # year-month-day
                for i in [self.red_i[_date],self.green_i[_date],self.blue_i[_date]]:
                    r_count = 0
                    for j in i:
                        r_count += 1
                        count += 1

                print('{} tickets sold on {}'.format(count, _date))

        except KeyError:
            print('No tickets sold on this date.')



# initiate the BigBus ticket stand
x = BigBus()

# sell a few tickets
x.sell_ticket(2019,4,17,'red',1)
x.sell_ticket(2019,4,17,'blue',2)
x.sell_ticket(2019,4,17,'green',3)
x.sell_ticket(2019,4,18,'red',1)
x.sell_ticket(2019,4,18,'green',3)
x.sell_ticket(2019,4,18,'red',1)
x.sell_ticket(2019,4,18,'blue',1)
x.sell_ticket(2019,4,18,'red',4)
x.sell_ticket(2019,4,18,'green',1)
x.sell_ticket(2019,4,19,'red',1)
x.sell_ticket(2019,4,19,'green',1)
x.sell_ticket(2019,4,19,'blue',3)
x.sell_ticket(2019,4,19,'red',1)
x.sell_ticket(2019,4,19,'green',1)
x.sell_ticket(2019,4,19,'red',1)
x.sell_ticket(2019,4,19,'red',1)
x.sell_ticket(2019,4,20,'blue',1)
x.sell_ticket(2019,4,20,'red',20)
x.sell_ticket(2019,4,20,'green',1)
x.sell_ticket(2019,4,20,'red',1)
x.sell_ticket(2019,4,20,'red',1)
x.sell_ticket(2019,4,20,'green',1)
x.sell_ticket(2019,4,21,'red',1)
x.sell_ticket(2019,4,21,'green',1)
x.sell_ticket(2019,4,21,'red',1)
x.sell_ticket(2019,4,21,'blue',1)
x.sell_ticket(2019,4,21,'blue',1)
x.sell_ticket(2019,4,21,'red',1)
x.sell_ticket(2019,4,22,'red',1)
x.sell_ticket(2019,4,22,'green',1)
x.sell_ticket(2019,4,22,'blue',1)
x.sell_ticket(2019,4,22,'red',1)
x.sell_ticket(2019,4,22,'red',1)
x.sell_ticket(2019,4,23,'green',1)
x.sell_ticket(2019,4,23,'red',1)
x.sell_ticket(2019,4,23,'blue',1)
x.sell_ticket(2019,4,23,'blue',1)
x.sell_ticket(2019,4,23,'red',1)
x.sell_ticket(2019,4,23,'green',1)
x.sell_ticket(2019,4,24,'red',1)
x.sell_ticket(2019,4,24,'green',1)
x.sell_ticket(2019,4,24,'red',1)
x.sell_ticket(2019,4,24,'blue',1)


x.report(False, 'blue')
