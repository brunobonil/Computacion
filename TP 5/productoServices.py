from repositorios import Repositorios


class ProductoService:

    def get_productosList(self):
        for i in Repositorios.productosList:
            print("ID ->", i, Repositorios.productosList[i])

    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        lastKey = lastKey + 1
        Repositorios.productosList[lastKey] = producto.__dict__
        return lastKey

    def delete_producto(self, key):
        dicc = Repositorios.productosList
        if key not in Repositorios.productosList:
            raise ValueError
        del dicc[key]

    def modify_producto(self, key, producto):
        dicc = Repositorios.productosList
        dicc[key] = producto.__dict__
