#!/usr/bin/env python3
# ;ladjsf
import subprocess
import re
from monitor import monitor

def main():
    mMonitors = parse_monitors()
    print("Monitors:")
    for lMonitor in mMonitors:
        print(lMonitor)

# return a list of monitors with dimensions
def parse_monitors():
    toReturn=[]
    for line in subprocess.check_output(["bspc","query","-T"],universal_newlines=True).split('\n')[:-1]:
        if (line[0] != '\t'):
            # get dimensions from line  to use - eg name 1440x900+0+0
            # note: monitor names can have spaces.
            info = re.search('(.+) (\d+)x(\d+)\+(\d+)\+(\d+)', line )
            lInfo = info.groups()
            m = monitor(*lInfo)
            toReturn.append(m)
    return toReturn

if __name__ == "__main__":
    main()
