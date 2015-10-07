#!/usr/bin/env python3
# ;ladjsf
import subprocess
import re
from monitor import monitor
from panel import panel

def main():
    mMonitors = parse_monitors()
    print("Monitors:")
    for lMonitor in mMonitors:
        print(lMonitor)
    # Make a panel with on first monitor
    #p = panel('auto', 32, 0, 0, 10, 10)
    p = panel({'width': 'auto', 'xoffset': 0, 'yoffset': 0, 'height': 32, 'hpadding': 10, 'vpadding': 10 })
    p.SetMonitor(mMonitors[0])
    p.Run()


# return a list of monitors with dimensions
def parse_monitors():
    toReturn=[]
    for line in subprocess.check_output(["bspc","query","-T"],universal_newlines=True).split('\n')[:-1]:
        if (line[0] != '\t'):
            # get dimensions from line  to use - eg name 1440x900+0+0
            # note: monitor names can have spaces.
            info = re.search('(.+) (\d+)x(\d+)\+(\d+)\+(\d+)', line )
            toReturn.append(monitor(*info.groups()))

    # Sort them left to right.
    toReturn.sort(key=lambda mon: mon.xoffset)
    # lemonbars -g flag yoffset appears to be in relation to current monitor, not xrootwin.

    return toReturn

if __name__ == "__main__":
    main()
