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
    print("3. Modificar detalles articulo cientifico")
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
    print("3. Eliminar copia")
    print("4. Volver")

# 1.5 #
def menu_admin_info_autores():
    print("-- Autores --")
    print("1. Registrar autor")
    print("2. Buscar autor")
    print("3. Modificar detalles de autor")
    print("4. Asociar libro")
    print("5. Volver")

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
    print("1. Registrar lector")
    print("2. Buscar lector")
    print("3. Modificar lector ")
    print("4. Habilitar lector")
    print("5. Inhabilitar lector")
    print("6. Volver")

# 3 #
def menu_administracion_prestamos():
    print("-- Prestamos y transacciones --")
    print("1. Realizar transaccion")
    print("2. Administrar de multas")
    print("3. Volver")

# 3.1 #
def menu_admi_transacciones():
    print("-- Transacciones --")
    print("1. Solicitud de prestamo")
    print("2. Devolucion de prestamo")
    print("3. Volver")

# 3.2 #
def menu_admi_multas():
    print("-- Multas --")
    print("1. Asignar multa")
    print("2. Levantar multa")
    print("3. Volver")


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