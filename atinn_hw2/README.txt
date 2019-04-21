Specs:
    Ubuntu 18.04
    Python 3.7
------------------------------------------------------------------------------------------------------------   
    
How to run:
    
    python big_bus.py
    
------------------------------------------------------------------------------------------------------------
Example Interaction:


Welcome to the Big Bus App!
Type `help` or `?` to list commands.

> sell 2019 4 21 red 2
sold 1 red ticket for $30.00 on Sunday 2019-04-21 under ID: c38edc2d-b44b-4a41-8da2-d7e92ff96765
sold 1 red ticket for $30.00 on Sunday 2019-04-21 under ID: 2f2a3945-e533-4b1f-b87c-e8b02e0c9d67
> sell 2019 4 21 red 4
sold 1 red ticket for $27.00 on Sunday 2019-04-21 under ID: bf8ef882-d6a1-40ee-a5ca-d09db1ef264a
sold 1 red ticket for $27.00 on Sunday 2019-04-21 under ID: e3e864ec-404d-4e35-8b65-4b56af0cd3ee
sold 1 red ticket for $27.00 on Sunday 2019-04-21 under ID: 0f596942-1205-4680-abd0-5929eab00e69
sold 1 red ticket for $27.00 on Sunday 2019-04-21 under ID: a5c8ce08-8179-4d88-bf2f-111f609f3c58
> sell 2019 4 22 blue 1
sold 1 blue ticket for $25.00 on Monday 2019-04-22 under ID: eed25b3e-a69c-40da-9484-d5f122226206
> sell 2019 4 22 green 3
sold 1 green ticket for $25.00 on Monday 2019-04-22 under ID: 7fa1b51d-bbb0-4f0f-8169-0677258f1614
sold 1 green ticket for $25.00 on Monday 2019-04-22 under ID: 549c50e5-7695-4c83-8278-da57f493ab2d
sold 1 green ticket for $25.00 on Monday 2019-04-22 under ID: 33e28372-c84a-4f27-ba88-6f69d6055a2f
> sell 2019 4 22 blue 4
sold 1 blue ticket for $22.50 on Monday 2019-04-22 under ID: 456f01a3-ffdc-47d2-baeb-2b8a375137a8
sold 1 blue ticket for $22.50 on Monday 2019-04-22 under ID: 75c82671-ef20-4318-95b4-8976b2476574
sold 1 blue ticket for $22.50 on Monday 2019-04-22 under ID: f58de2cc-fb44-44e6-9e03-447523547be1
sold 1 blue ticket for $22.50 on Monday 2019-04-22 under ID: a6e8b8d7-af16-4dbb-a7b6-7ece87e10224
> report True
Please enter a route: red, green or blue
red
6 red route tickets sold on 2019-04-21
> report True
Please enter a route: red, green or blue
blue
No tickets sold on this date.
> report False
please enter a year (ex. 2019)
2019
please enter a month (ex. 6)
4
please enter a day (ex. 21)
22
8 tickets sold on 2019-04-22
> refund 2019 4 21 red 0f596942-1205-4680-abd0-5929eab00e69
refunding 0f596942-1205-4680-abd0-5929eab00e69 back for $27.00
> refund 2019 4 22 blue a6e8b8d7-af16-4dbb-a7b6-7ece87e10224
refunding a6e8b8d7-af16-4dbb-a7b6-7ece87e10224 back for $22.50
> report True
Please enter a route: red, green or blue
red
5 red route tickets sold on 2019-04-21
> report False
please enter a year (ex. 2019)
2019
please enter a month (ex. 6)
4
please enter a day (ex. 21)
22
7 tickets sold on 2019-04-22
> 



------------------------------------------------------------------------------------------------------------

Comments:

    -Everything seems to be working okay. Built quick and dirty with more conditional statements than I would prefer but I tried to keep everything minimal with little functions and classes.
