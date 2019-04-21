from datetime import date, timedelta
import calendar
from uuid import uuid4
import cmd

class BigBus(cmd.Cmd):

    intro = "\nWelcome to the Big Bus App!\nType `help` or `?` to list commands.\n"
    prompt = '> '

    # making up prices
    cheap = 25.00 # Mon, Tues, Wed, Thurs
    normal = 30.00 # Fri, Sat, Sun
    red = 5 * 89
    green = 4 * 89
    blue = 2 * 89
    red_i = {}
    green_i = {}
    blue_i = {}

    def do_sell(self, arg):
        '''given a date, route and amount, will purchase tickets
        :param: year 2019
        :param: month 1 - 12
        :param: day 1 - 31
        :param: route [red, green, blue]
        :param: amount 1 - 4
        :return:
        '''

        arg = arg.split()
        if len(arg) != 5:
            print('please enter the correct number of arguments [year, month, day, route, amount]')
            return
        year = int(arg[0])
        month = int(arg[1])
        day = int(arg[2])
        route = arg[3]
        amount = int(arg[4])

        try:
            _date = date(year, month, day) # year-month-day
            day = calendar.day_name[_date.weekday()] # sun - sat
        except ValueError:
            print('please enter correct values for the date')
            return
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
                if str(_date) in BigBus.red_i:
                    if len(BigBus.red_i[str(_date)]) > BigBus.red - amount:
                        print('not enough tickets available for this day')
                        return
                    else:
                        for i in range(amount):
                            ID = uuid4()
                            BigBus.red_i[str(_date)].append((ID,price))
                            print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route,round(price, 2), day,_date, ID))
                else:
                    ID = uuid4()
                    BigBus.red_i[str(_date)] = [(ID,price)]
                    print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route, round(price, 2), day, _date,ID))
                    for i in range(amount-1):
                        ID = uuid4()
                        BigBus.red_i[str(_date)].append((ID,price))
                        print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route, round(price, 2), day,_date, ID))

            if route == 'blue':
                if str(_date) in BigBus.blue_i:
                    if len(BigBus.blue_i[str(_date)]) > BigBus.blue - amount:
                        print('not enough tickets available for this day')
                        return
                    else:
                        for i in range(amount):
                            ID = uuid4()
                            BigBus.blue_i[str(_date)].append((ID,price))
                            print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route,round(price, 2), day,_date, ID))
                else:
                    ID = uuid4()
                    BigBus.blue_i[str(_date)] = [(ID,price)]
                    print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route, round(price, 2), day, _date,ID))
                    for i in range(amount-1):
                        ID = uuid4()
                        BigBus.blue_i[str(_date)].append((ID,price))
                        print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route, round(price, 2), day,_date, ID))

            if route == 'green':
                if str(_date) in BigBus.green_i:
                    if len(BigBus.green_i[str(_date)]) > BigBus.green - amount:
                        print('not enough tickets available for this day')
                        return
                    else:
                        for i in range(amount):
                            ID = uuid4()
                            BigBus.green_i[str(_date)].append((ID,price))
                            print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route,round(price, 2), day,_date, ID))
                else:
                    ID = uuid4()
                    BigBus.green_i[str(_date)] = [(ID,price)]
                    print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route, round(price, 2), day, _date, ID))
                    for i in range(amount-1):
                        ID = uuid4()
                        BigBus.green_i[str(_date)].append((ID,price))
                        print('sold 1 {} ticket for ${:.2f} on {} {} under ID: {}'.format(route, round(price, 2), day,_date, ID))



    def do_refund(self, arg):
        '''given a year, month, day, route and id, will attempt to refund and remove from database.
        :param year: 2019
        :param month: integer 1 - 12
        :param day: interger 1 - 31
        :param route: red, green or blue
        :param arg:[year, month, day, route, id]
        :param today: 2019
        :param route: red, green or blue

        :return:
        '''

        arg = arg.split()
        if len(arg) != 5:
            print('please enter the correct number of arguments [year, month, day, route, id]')
            return
        year = int(arg[0])
        month = int(arg[1])
        day = int(arg[2])
        route = arg[3]
        ID = arg[4]

        _date = date(year, month, day)

        if route == 'red':
            for i in range(len(BigBus.red_i[str(_date)])):
                if str(BigBus.red_i[str(_date)][i][0]) == ID:
                    print('refunding {} back for ${:.2f}'.format(BigBus.red_i[str(_date)][i][0],BigBus.red_i[str(_date)][i][1]))
                    del BigBus.red_i[str(_date)][i]
                    break

        if route == 'green':
            for i in range(len(BigBus.green_i[str(_date)])):
                if str(BigBus.green_i[str(_date)][i][0]) == ID:
                    print('refunding {} back for ${:.2f}'.format(BigBus.green_i[str(_date)][i][0],BigBus.green_i[str(_date)][i][1]))
                    del BigBus.green_i[str(_date)][i]
                    break

        if route == 'blue':
            for i in range(len(BigBus.blue_i[str(_date)])):
                if str(BigBus.blue_i[str(_date)][i][0]) == ID:
                    print('refunding {} back for ${:.2f}'.format(BigBus.blue_i[str(_date)][i][0],BigBus.blue_i[str(_date)][i][1]))
                    del BigBus.blue_i[str(_date)][i]
                    break

    def do_report(self, arg):
        '''
        :param arg:[today, route, year, month, day]
        :param today: True or False
        :param route: red, green or blue
        :param year: 2019
        :param month: integer 1 - 12
        :param day: integer 1 - 31
        :return:
        '''


        arg = arg.split()
        if len(arg) != 1:
            print('please enter the correct number of arguments [year, month, day, route, amount]')
            return
        today = arg[0]


        try:
            if today == 'True':
                route = str(input('Please enter a route: red, green or blue\n'))
                # check if valid route
                if route not in ('red', 'blue', 'green'):
                    print('please choose a valid route \"red\", \"blue\", \"green\"')
                    return
                _date = str(date.today())
                count = 0
                if route == 'red':
                    for i in BigBus.red_i[_date]:
                        count += 1
                if route == 'green':
                    for i in BigBus.green_i[_date]:
                        count += 1
                if route == 'blue':
                    for i in BigBus.blue_i[_date]:
                        count += 1
                print('{} {} route tickets sold on {}'.format(count, route, _date))
                return

        except KeyError:
            print('No tickets sold on this date.')
            return

        if today == 'False':
            try:
                year = int(input('please enter a year (ex. 2019)\n'))
                month = int(input('please enter a month (ex. 6)\n'))
                day = int(input('please enter a day (ex. 21)\n'))
                count = 0
                _date = str(date(year, month, day))  # year-month-day
            except ValueError:
                print('please return valid numbers')
                return

            for i in [BigBus.red_i,BigBus.green_i,BigBus.blue_i]:
                if _date in i:
                    for j in i[_date]:
                        count += 1
            print('{} tickets sold on {}'.format(count, _date))
            return

        else:
            print('please enter either \"True\" for reports today, or \"False\" for different date!')


    def do_quit(self, arg):
        """Quit"""
        return True


if __name__ == '__main__':
    x = BigBus().cmdloop()