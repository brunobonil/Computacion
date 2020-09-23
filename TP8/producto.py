class Producto():

    def __init__(self, descripcion=' ', precio=0, tipo=' ', estado='Disponible'):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        self.estado = estado

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
        if value < 0:
            raise ValueError("El precio no puede ser negativo")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value
