import unittest
from producto import Producto
from parameterized import parameterized
from productoServices import ProductoService
from repositorios import Repositorios


class TestProducto(unittest.TestCase):
    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'Disponible'})

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'Disponible'})

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras', 'Vendido'),
            ("samsung s10", 200000, 'celular', 'Disponible'),
            ("samsung s20", 400000, 'celular', 'Disponible'),
            ("acer", 6000500, 'computadoras', 'Disponible'),
            ("HP", 6000000, 'computadoras', 'Disponible')
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo, estado):
        producto = Producto(descripcion, precio, tipo, estado)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)

    @parameterized.expand([
        ("ascendente",
            {0: {'_descripcion': 'samsung s10', '_precio': 200000,
             '_tipo': 'celular', '_estado': 'Disponible'},
             1: {'_descripcion': 'samsung s20',
             '_precio': 400000, '_tipo': 'celular', '_estado': 'Disponible'},
             2: {'_descripcion': 'lenovo t490', '_precio': 6000000, '_tipo':
             'computadoras', '_estado': 'Vendido'},
             3: {'_descripcion': 'HP', '_precio': 6000000, '_tipo':
             'computadoras', '_estado': 'Disponible'},
             4: {'_descripcion': 'acer', '_precio': 6000500, '_tipo':
             'computadoras', '_estado': 'Disponible'}}),
        ("descendente",
            {0: {'_descripcion': 'acer', '_precio': 6000500,
             '_tipo': 'computadoras', '_estado': 'Disponible'},
             1: {'_descripcion': 'lenovo t490', '_precio': 6000000, '_tipo':
             'computadoras', '_estado': 'Vendido'},
             2: {'_descripcion': 'HP', '_precio': 6000000, '_tipo':
             'computadoras', '_estado': 'Disponible'},
             3: {'_descripcion': 'samsung s20', '_precio': 400000, '_tipo':
             'celular', '_estado': 'Disponible'},
             4: {'_descripcion': 'samsung s10', '_precio': 200000, '_tipo':
             'celular', '_estado': 'Disponible'}})
    ])
    # Ordenar lista
    def test_insertion_sort_precio(self, tipo_orden, list_ordenada):
        lista_ordenada = ProductoService().\
            insertion_sort_precio(Repositorios.productosList, tipo_orden)
        self.assertDictEqual(lista_ordenada, list_ordenada)

    @parameterized.expand([
        (200000, {'_descripcion':
         'samsung s10', '_precio': 200000, '_tipo': 'celular',
                                                    '_estado': 'Disponible'}),
        (400000, {'_descripcion':
         'samsung s20', '_precio': 400000, '_tipo': 'celular', '_estado':
                                                               'Disponible'}),
    ])
    # Busqueda binaria
    def test_busqueda_binaria(self, precio_buscado, producto):
        busqueda = ProductoService().\
            busqueda_binaria(Repositorios.productosList, precio_buscado)
        self.assertDictEqual(busqueda, producto)

    # Eliminar un producto
    # def test_delete_producto(self):
    #    ProductoService().delete_producto(0)
    #    self.assertEqual(Repositorios.productosList.get(0), None)

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_delete_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1)

    #@parameterized.expand([
    #        (3, {'_descripcion': 'lenovo t490', '_precio': 6000000, '_tipo':
    #             'computadoras', '_estado': 'Vendido'}),
    #])
    #def test_update_producto(self, key, producto):
    #    ProductoService().update_producto(key, producto)
    #    self.assertDictEqual(Repositorios.productosList[key],
    #                         producto.dict)

    @parameterized.expand([
        ('Disponible',
            {0: {'_descripcion': "samsung s10", '_precio': 200000, '_tipo':
                 'celular', '_estado': 'Disponible'},
             1: {'_descripcion': "samsung s20", '_precio': 400000, '_tipo':
                 'celular', '_estado': 'Disponible'},
             2: {'_descripcion': "acer", '_precio': 6000500, '_tipo':
                 'computadoras', '_estado': 'Disponible'},
             3: {'_descripcion': "HP", '_precio': 6000000, '_tipo':
                 'computadoras', '_estado': 'Disponible'}}),
        ('Vendido', {0: {'_descripcion': "lenovo t490", '_estado': 'Vendido',
         '_precio': 6000000, '_tipo': 'computadoras'}})
    ])
    def test_get_lista_estado(self, estado, dicc):
        self.maxDiff = None
        lista = ProductoService.get_productosList(self)
        lista_filtrada = ProductoService.get_lista_estado(self, lista, estado)
        self.assertDictEqual(lista_filtrada, dicc)


    #def test_valor_negativo(self, ):


if __name__ == '__main__':
    unittest.main()
