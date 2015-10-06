from widgets import clock
import subprocess

class panel:
    def SetMonitor(self, aMonitor):
        self.mMonitor = aMonitor

    def __init__(self, width, height, xoffset, yoffset, hpadding, vpadding):
        self.width = width
        self.height = height
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.hpadding = hpadding
        self.vpadding = vpadding

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
        subprocess.call("lemonbar"," -g " + lBarGeom," -p")

