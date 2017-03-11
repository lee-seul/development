# coding: utf-8


class TouchBarInterface(object):
    def print_model(self):
        pass


class TouchBar(TouchBarInterface):
    def print_model(self):
        print(u"터치바, 13인치")


class NoTouchBar(TouchBarInterface):
    def print_model(self):
        print(u"13인치")


class NoTouchBar15(TouchBarInterface):
    def print_model(self):
        print(u"15인치")
    

class TouchBar15(TouchBarInterface):
    def print_model(self):
        print(u"터치바, 15인치")


class BaseMacBookPro(object):
    _model = None
    def __init__(self, modelType:TouchBarInterface) -> None:
        self._model = modelType

    def setModel(self, modelType:TouchBarInterface) -> None:
        self._model = modelType

    def modelFunction(self):
        self._model.print_model(self._model)

if __name__ == "__main__":
    macbook1 = BaseMacBookPro(NoTouchBar15)
    macbook1.modelFunction()

    macbook2 = BaseMacBookPro(TouchBar)
    macbook2.modelFunction()

    macbook1.setModel(NoTouchBar)
    macbook1.modelFunction()



