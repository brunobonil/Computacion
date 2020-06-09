class Book():
    def __init__(self, name='', authorName='', memberLegajo=''):
        self._name = name.upper()
        self._authorName = authorName.upper()
        self._memberLegajo = memberLegajo.upper()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def authorName(self):
        return self._authorName

    @authorName.setter
    def authorName(self, value):
        self._authorName = value.upper()

    @property
    def memberLegajo(self):
        return self._memberLegajo

    @memberLegajo.setter
    def memberLegajo(self, value):
        self._memberLegajo = value
