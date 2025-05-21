
class RichWord:
    def __init__(self, parola):
        self._parola = parola
        self._corretta = None

    @property
    def corretta(self):
        print("getter della parola data")
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        print("setter della parola chiamata")
        self._corretta = boolValue

    def __str__(self):
        return self._parola