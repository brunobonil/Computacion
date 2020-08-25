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

    def insertion_sort_precio(self, oldRepo, orden):
        newRepo = oldRepo
        if orden == "ascendente":

            for i in range(1, len(newRepo)):
                while (i >= 1) and (newRepo[i-1]['_precio'] >
                                    newRepo[i]['_precio']):
                    newRepo[i], newRepo[i-1] = newRepo[i-1], newRepo[i]
                    i -= 1
            return newRepo

        if orden == "descendente":

            for i in range(1, len(newRepo)):
                while (i >= 1) and (newRepo[i-1]['_precio'] <
                                    newRepo[i]['_precio']):
                    newRepo[i], newRepo[i-1] = newRepo[i-1], newRepo[i]
                    i -= 1
            return newRepo
