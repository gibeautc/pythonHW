#!/bin/python

# Consider a table fan and implement a TableFan class. What would be the attributes of this
# class? Examples of attributes could be speed levels of the fan, side-to-side movement (on/off,
# and degrees of movement), manufacturer name, cost, etc. Think about it this way: you want
# to be able to get information about the fan; for example, if you want to buy or sell a fan on a
# website such as Craigslist, what features would you be interested in? Also, consider control
# (operations) you might want to have over the fan such as setting the speed or having it
# oscillate.
# The TableFan class should include at least three attributes and three methods.


class TableFan:
    speed=0 #0 is off, 10 is max
    ossilation=False
    orientation=0 # degrees, can be +-90
    