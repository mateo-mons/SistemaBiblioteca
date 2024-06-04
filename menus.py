# main #
def main_menu():
    print("****** SISTEMA BIBLIOTECA ******")
    print("1. Administrar productos")
    print("2. Administrar usuarios")
    print("3. Administracion de prestamos")
    print("4. Salir")

# 1 #
def menu_administracion_productos():
    print("-- Productos --")
    print("1. Administrar tesis")
    print("2. Administrar articulo cientifico")
    print("3. Administrar libro")
    print("4. Administrar copias")
    print("5. Administrar informacion de autores")
    print("6. Volver")

# 1.1 #
def menu_admin_tesis():
    print("-- Tesis --")
    print("1. Registrar tesis")
    print("2. Buscar tesis")
    print("3. Modificar tesis")
    print("4. Eliminar tesis")
    print("5. Volver")

# 1.2 #
def menu_admin_arti_cient():
    print("-- Articulos Cientificos --")
    print("1. Registrar articulo cientifico")
    print("2. Buscar articulo cientifico")
    print("3. Modificar articulo cientifico")
    print("4. Eliminar articulo cientifico")
    print("5. Volver")

# 1.3 #
def menu_admin_libros():
    print("-- Libros --")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Modificar detalles de libro")
    print("4. Inhabilitar libro")
    print("5. Volver")

# 1.4 #
def menu_admin_copias():
    print("-- Copias --")
    print("1. Registrar copia")
    print("2. Buscar copia")
    print("3. Eliminar tesis")
    print("4. Volver")

# 1.5 #
def menu_admin_info_autores():
    pass

# 2 #
def menu_administracion_usuarios():
    print("-- Usuarios --")
    print("1. Administrar bibliotecario")
    print("2. Administrar lector")
    print("3. Volver")

# 2.1 #
def menu_admin_bibliotecario():
    print("-- Bibliotecario --")
    print("1. Registrar bibliotecario")
    print("2. Buscar bibliotecario")
    print("3. Eliminar bibliotecario")
    print("4. Volver")

# 2.2 #
def menu_admin_lector():
    print("-- Lector --")
    print("1. Registrar Lector")
    print("2. Buscar Lector")
    print("3. Modificar Lector ")
    print("4. Habilitar Lector")
    print("5. Inhabilitar Lector")
    print("6. Volver")

def menu_administracion_prestamos():
    pass


'''
1. Administrar productos
    - tesis
        * administrar autor
        * administrar categoria
    - arti. cientifico
        * administrar autor
        * administrar categoria
    - libros
        * administrar autor
        * administrar categoria, subcategoria
    - copias
        * tesis
        * art. cient
        * libros
    - informacion de autores
        * consultas, modificaciones
2. Administrar usuario
    - bibliotecario
    - lector
        * consultar prestamos, multas y esa vuelta

3. Administracion de prestamos
    - Realizar transaccion
        * solicitud de prestamo
        * devolver prestamo
        * pagar multa
    - Administracion de multas
        * asignar multa
        * consultar estado de multas
4. Salir

'''