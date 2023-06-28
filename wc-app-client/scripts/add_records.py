#!/usr/bin/env python3

"""
Script to add dummy data to the world cup app.

Command Options:

    L - add locations

Examples:

    # Add all the records
    >>> add_records.py

    # Add all  the location records i.e. 
    # add countries, cities and stadiums.
    >>> add_records.py L

"""

import sys



def _add_countries():

    # spam = Spam(foo=Foo(count=1, size=1.0),bars=[Bar()])

def main(options):

    if 'L' in options:
        _add_countries()
        _add_cities()
        _add_stadiums()


if __name__ == "__main__":

    if "h" in sys.argv:
        print (__doc__)

    else:
        main(sys.argv[1:])
    # add countries

    # add cities

    # add stadiums
