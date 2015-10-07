from widgets import clock
import subprocess

class panel:
    def SetMonitor(self, aMonitor):
        self.mMonitor = aMonitor

    # expected: width, height, xoffset, yoffset, hpadding, vpadding
    def __init__(self, attributes):
        self.__dict__ = attributes


    def AddWidget(self, aWidget, aAlign):
        pass

    # Consider Flags
    def Run(self):
        lBarHeight = self.height
        if self.width == 'auto':
            lBarWidth = int(self.mMonitor.width) - (int(self.hpadding) * 2)
        else:
            lBarWidth = self.width
        lBarX = int(self.mMonitor.xoffset) + int(self.hpadding) + int(self.xoffset)
        lBarY = int(self.mMonitor.yoffset) + int(self.vpadding) + int(self.yoffset)
        lBarGeom = str(lBarWidth) + "x" + str(lBarHeight) + "+" + str(lBarX) + "+" + str(lBarY)
        print("lemonbar"+" -g "+lBarGeom+" -p")
        subprocess.call(["lemonbar","-g",lBarGeom," -p"])

