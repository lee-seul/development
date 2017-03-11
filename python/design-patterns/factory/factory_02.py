

class MacBookFactory(object):
    def createMacbook(model):
        pass

class ConreateMacBookFactory(MacBookFactory):
    def createMacbook(model):
        if model == "TouchBar15":
            return TouchBar15()

        elif model == "NoTouchBar":
            return NoTouchBar()

    

