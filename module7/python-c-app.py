#!/usr/bin/env python
#
# @description
#   Simple python application to print the current running processes using
#   'psutil' module which contains C components.
#

import datetime
import psutil


# This program displays the current running processes in tabular form
def main():
    """ Prints current active processes """
    # Create a format and print table headings
    row_format = "{:<40} {:<10} {:<30} {:<20}"
    print row_format.format("Proc Name", "Proc ID", "Start Time", "Status",
                            "Priority")
    print "-"*100
    # Iterate over all running processes
    for proc in psutil.process_iter():
        # Get process create time in the standard time format
        time = datetime.datetime.fromtimestamp(proc.create_time()).strftime(
            "%Y-%m-%d %H:%M:%S")
        # Print process's name, pid, create time and status in a table format
        print row_format.format(proc.name(),
                                proc.pid,
                                time,
                                proc.status())

if __name__ == '__main__':
    main()
