from time import gmtime, strftime

class widget(object):
    def __init__(self):
        pass
    def Content(self):
        pass
    def Update(self):
        pass

class clock(object):
    time=""
    def Update(self):
        time = strftime("%H:%M", gmtime())
    def __str__(self):
        # Note: set widget icons elsewhere(config)
        print(self.icon, self.time, end = '')

