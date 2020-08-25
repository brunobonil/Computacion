class Producto():

    def __init__(self, descripcion=None, precio=None, tipo=None):
        self._descripcion = descripcion
        self._precio = precio
        self._tipo = tipo

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value
