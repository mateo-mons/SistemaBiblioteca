from clases.ArticuloCientifico import *
from clases.Autor import *
from clases.Categoria import *
from clases.Copias import *
from clases.Lector import *
from clases.Libro import *
from clases.Multa import *
from clases.Prestamos import *
from clases.Tesis import *
from menus import *
import os

# LISTAS PARA ALMACENAR INFORMACION DE OBJETOS #
listaArtiCientificos = []
listaAutores = []
listaCategorias = []
listaCopias = []
listaLectores = []
listaLibros = []
listaMultas = []
listaPrestamos = []
listaTesis = []
listaBibliotecarios = []

# OBJETOS QUEMADOS PARA PRUEBAS #

autor2 = Autor(1,"J.K. Rowling", "Británica", "31 de julio de 1965")
listaAutores.append(autor2)
libro2 = Libro("Harry Potter y la piedra filosofal", "9788478884455", "Fantasía", "Edición especial", 1997, "Salamandra", "Usado", "Español", 50, [autor2])
listaLibros.append(libro2)
autor2.libros.append(libro2)

autor3 = Autor(2,"Gabriel García Márquez", "Colombiana", "6 de marzo de 1927")
listaAutores.append(autor3)
libro3 = Libro("Cien años de soledad", "9788437615030", "Realismo mágico", "Edición conmemorativa", 1967, "Diana", "Nuevo", "Español", 80, [autor3])
listaLibros.append(libro3)
autor3.libros.append(libro3)

autor4 = Autor(3,"George Orwell", "Británica", "25 de junio de 1903")
listaAutores.append(autor4)
libro4 = Libro("1984", "9780141036144", "Distopía", "Reedición", 1949, "Penguin Books", "Usado", "Inglés", 60, [autor4])
listaLibros.append(libro4)
autor4.libros.append(libro4)

autor5 = Autor(4,"Jane Austen", "Británica", "16 de diciembre de 1775")
listaAutores.append(autor5)
libro5 = Libro("Orgullo y prejuicio", "9788497940821", "Novela romántica", "Edición ilustrada", 1813, "Alba Editorial", "Nuevo", "Español", 70, [autor5])
listaLibros.append(libro5)
autor5.libros.append(libro5)

autor6 = Autor(5,"Miguel de Cervantes", "Española", "29 de septiembre de 1547")
listaAutores.append(autor6)
libro6 = Libro("Don Quijote de la Mancha", "9788420412146", "Novela picaresca", "Edición crítica", 1605, "Alfaguara", "Usado", "Español", 90, [autor6])
listaLibros.append(libro6)
autor6.libros.append(libro6)

autor7 = Autor(6,"Herman Melville", "Estadounidense", "1 de agosto de 1819")
listaAutores.append(autor7)
libro7 = Libro("Moby Dick", "9788491050364", "Novela de aventuras", "Edición de lujo", 1851, "Alba Editorial", "Nuevo", "Español", 40, [autor7])
listaLibros.append(libro7)
autor7.libros.append(libro7)

autor8 = Autor(7,"Antoine de Saint-Exupéry", "Francés", "29 de junio de 1900")
listaAutores.append(autor8)
libro8 = Libro("El principito", "9780547964069", "Literatura infantil", "Edición de colección", 1943, "Houghton Mifflin Harcourt", "Usado", "Español", 120, [autor8])
listaLibros.append(libro8)
autor8.libros.append(libro8)

autor9 = Autor(8,"Mark Twain", "Estadounidense", "30 de noviembre de 1835")
listaAutores.append(autor9)
libro9 = Libro("Las aventuras de Tom Sawyer", "9788491815234", "Novela juvenil", "Edición especial", 1876, "Penguin Clásicos", "Nuevo", "Español", 55, [autor9])
listaLibros.append(libro9)
autor9.libros.append(libro9)

autor10 = Autor(9,"Franz Kafka", "Austrohúngaro", "3 de julio de 1883")
listaAutores.append(autor10)

libro10 = Libro("La metamorfosis", "9788483461646", "Ficción absurda", "Edición anotada", 1915, "Editorial Losada", "Nuevo", "Español", 65, [autor10])
listaLibros.append(libro10)
autor10.libros.append(libro10)

autor1 = Autor(5, "Rafael Camilo Lopez Gomez", "Colombia", "04-07-1987")
tesis1 = Tesis(10, autor1, "UTP", "23-06-2023", "05-12-2023", "Ingenieria", "Disponible", 10)

copia1 = Copia(1, "Disponible", "9788478884455")
listaCopias.append(copia1)

listaAutores.append(autor1)
listaTesis.append(tesis1)

print(tesis1.verTesis())
print("--------------------------------")
print(tesis1.autor.verAutor())


# MAIN PROGRAM #
while True:
    os.system("clear")
    main_menu()
    main_option = int(input("Opcion: "))

    if main_option == 1:
        while True:
            menu_administracion_productos()
            option1 = int(input("Opcion: "))

            if option1 == 1:
                while True:
                    menu_admin_tesis()
                    option1_1 = int(input("Opcion: "))

                    if option1_1 == 1:
                        print("-- Registra tesis --")
                        id_tesis = int(input("Ingresa identificador de la tesis: "))
                        autor = str(input("Ingresa nombre de autor(es): "))
                        institucion = str(input("Ingresa la institucion de estudios: "))
                        fecha_investigacion = str(input("Ingresa la fecha de investigacion: "))
                        fecha_presentacion = str(input("Ingresa la fecha de presentacion: "))
                        campo = str(input("Ingresa el campo de estudios: "))
                        estado = str(input("Ingresa el estado: "))
                        num_paginas = int(input("Ingresa el numero de paginas: "))
                        tesis = Tesis(id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, num_paginas)
                        listaTesis.append(tesis)

                    elif option1_1 == 2:
                        print("-- Busca tesis --")
                        id_tesis = int(input("Identificador de la tesis: "))
                        for ident in listaTesis:
                            if ident.id_tesis == id_tesis:
                                ident.verTesis()
                                print("\n")
                                break
                            else:
                                print("La tesis solicitada no está en el sistema")
                                print("\n")
                                
                    elif option1_1 == 3:
                        print("-- Modufica detalles de una tesis --")
                        id_tes = int(input("Identificador de la tesis: "))
                        for ident in listaTesis:
                            if ident.id_tesis == id_tes:
                                ident.modificarDatos()
                                break
                            else:
                                print("La tesis solicitada no está en el sistema")

                    elif option1_1 == 4:
                        print("-- Elimina una tesis --")
                        id_tes = int(input("Identificador de la tesis: "))
                        for ident in listaTesis:
                            if ident.id_tesis == id_tes:
                                listaTesis.remove(ident)
                                break
                            else:
                                print("La tesis solicitada no está en el sistema")

                    elif option1_1 == 5:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option1 == 2:
                while True:
                    menu_admin_arti_cient()
                    option1_2 = int(input("Opcion: "))

                    if option1_2 == 1:
                        print("-- Registra articulo cientifico --")
                        titulo = str(input("Ingresa el titulo del articulo: "))
                        doi = int(input("Ingresa el identificador DOI del articulo: "))
                        editor = str(input("Ingresa el editor del articulo: "))
                        fecha_publicacion = str(input("Ingresa la fecha de publicacion del articulo: "))
                        periodicidad = str(input("Ingresa la periodicidad del articulo: "))
                        volumen = str(input("Ingresa el volumen del articulo: "))
                        campo_interes = str(input("Ingresa el campo de interes del articulo: "))
                        estado = str(input("Ingresa estado del articulo: "))
                        artCienti = ArticuloCientifico(id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, num_paginas)
                        listaArtiCientificos.append(artCienti)

                    elif option1_2 == 2:
                        print("-- Busca articulo cientifico --")
                        id_doi = int(input("Identificador DOI del articulo cientifico: "))
                        for ident in listaArtiCientificos:
                            if ident.doi == id_doi:
                                ident.verArticuloCientifico()
                                break
                            else:
                                print("El articulo solicitado no está en el sistema")

                    elif option1_2 == 3:
                        print("-- Modificar un articulo cientifico --")
                        id_doi = int(input("Identificador DOI del articulo cientifico: "))
                        for ident in listaArtiCientificos:
                            if ident.doi == id_doi:
                                ident.modificarDatos()
                                break
                            else:
                                print("El articulo solicitado no está en el sistema")

                    elif option1_2 == 4:
                        print("-- Elimina un articulo cientifico --")
                        id_doi = int(input("Identificador DOI del articulo cientifico: "))
                        for ident in listaArtiCientificos:
                            if ident.doi == id_doi:
                                listaArtiCientificos.remove(ident)
                                break
                            else:
                                print("El articulo solicitado no está en el sistema")

                    elif option1_2 == 5:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option1 == 3:
                while True:
                    menu_admin_libros()
                    option1_3 = int(input("Opcion: "))

                    if option1_3 == 1:
                        titulo = input("Titulo: ")
                        isbn = input("ISBN: ")
                        genero = input("Genero: ")
                        edicion = input("Edicion: ")
                        ano_publicacion = int(input("Año de publicacion: "))
                        editorial = input("Editorial: ")
                        estado = input("Estado: ")
                        nombre_autor = input("Autor: ")
                        idioma = input("Idioma: ")
                        num_copias = int(input("Numero de copias: "))
                        
                        autor_instancia = next((autor for autor in listaAutores if autor.getNombre() == nombre_autor), None)
                        if autor_instancia is None:
                            print(f"Autor {nombre_autor} no encontrado.")
                            print("Desea añadir el autor? (S/N)")
                            respuesta = input()
                            if respuesta == "S" or respuesta == "s":
                                nombre_autor = input("Nombre del autor: ")
                                nacionalidad = input("Nacionalidad: ")
                                fecha_nacimiento = input("Fecha de nacimiento: ")
                                autor_instancia = Autor(nombre_autor, nacionalidad, fecha_nacimiento)
                                listaAutores.append(autor_instancia)
                            else:
                                continue               
                        
                        libro = Libro(titulo, isbn, genero, edicion, ano_publicacion, editorial, estado, idioma, num_copias, [autor_instancia])
                        listaLibros.append(libro)
                        autor_instancia.listaLibros.append(libro)
                        print(libro)
                
                    elif option1_3 == 2:
                        print("\n")
                        print("Buscar libro")
                        print("1. Por ISBN")
                        print("2. Por título")
                        print("3. Por autor")
                        opcion_busqueda = int(input("Opción: "))
                        if opcion_busqueda == 1:
                            isbn = input("ISBN: ")
                            libro = next((libro for libro in listaLibros if libro.getIsbn() == isbn), None)
                            if libro is not None:
                                libro.verLibro()
                            else:
                                print("Libro no encontrado")
                        elif opcion_busqueda == 2:
                            titulo = input("Título: ")
                            libro = next((libro for libro in listaLibros if libro.getTitulo() == titulo), None)
                            if libro is not None:
                                libro.verLibro()
                            else:
                                print("Libro no encontrado")
                        elif opcion_busqueda == 3:
                            autor = input("Autor: ")
                            libros_autor = [libro for libro in listaLibros if autor in [autor.getNombre() for autor in libro.getAutores()]]
                            if len(libros_autor) > 0:
                                for libro in listaLibros:
                                    libro.verLibro()
                            else:
                                print("Libro no encontrado")                       
                    elif option1_3 == 3:
                        print("\n")
                        print("Modificar libro")
                        print("1. Por ISBN")
                        print("2. Por título")
                        opcion_busqueda = int(input("Opción: "))
                        if opcion_busqueda == 1:
                            isbn = input("ISBN: ")
                            libro = next((libro for libro in listaLibros if libro.getIsbn() == isbn), None)
                            if libro is not None:
                                nuevo_genero = input("Nuevo género: ")
                                nuevo_edicion = input("Nueva edición: ")
                                nuevo_ano_publicacion = int(input("Nuevo año de publicación: "))
                                nueva_editorial = input("Nueva editorial: ")
                                nuevo_estado = input("Nuevo estado: ")
                                nuevo_idioma = input("Nuevo idioma: ")
                                nuevo_num_copias = int(input("Nuevo número de copias: "))
                                libro.modificarDatos(nuevo_genero, nuevo_edicion, nuevo_ano_publicacion, nueva_editorial, nuevo_estado, nuevo_idioma, nuevo_num_copias)                           

                            else:
                                print("Libro no encontrado")
                        elif opcion_busqueda == 2:
                            titulo = input("Título: ")
                            libro = next((libro for libro in listaLibros if libro.getTitulo() == titulo), None)
                            if libro is not None:
                                nuevo_genero = input("Nuevo género: ")
                                nuevo_edicion = input("Nueva edición: ")
                                nuevo_ano_publicacion = int(input("Nuevo año de publicación: "))
                                nueva_editorial = input("Nueva editorial: ")
                                nuevo_estado = input("Nuevo estado: ")
                                nuevo_idioma = input("Nuevo idioma: ")
                                nuevo_num_copias = int(input("Nuevo número de copias: "))
                                libro.modificarDatos(nuevo_genero, nuevo_edicion, nuevo_ano_publicacion, nueva_editorial, nuevo_estado, nuevo_idioma, nuevo_num_copias)                           

                            else:
                                print("Libro no encontrado")                                                                  
                    
                    elif option1_3 == 4:
                        print("\n")
                        print("Inhabilitar libro")
                        print("1. Por ISBN")
                        print("2. Por título")
                        print("3. Por autor")
                        opcion_busqueda = int(input("Opción: "))
                        if opcion_busqueda == 1:
                            isbn = input("ISBN: ")
                            libro = next((libro for libro in listaLibros if libro.getIsbn() == isbn), None)
                            if libro is not None:
                                libro.setEstado("Inhabilitado")
                            else:
                                print("Libro no encontrado")
                        elif opcion_busqueda == 2:
                            titulo = input("Título: ")
                            libro = next((libro for libro in listaLibros if libro.getTitulo() == titulo), None)
                            if libro is not None:
                                libro.setEstado("Inhabilitado")
                            else:
                                print("Libro no encontrado")
                        elif opcion_busqueda == 3:
                            autor = input("Autor: ")
                            libros_autor = [libro for libro in listaLibros if autor in [autor.getNombre() for autor in libro.getAutores()]]
                            if len(libros_autor) > 0:
                                for libro in listaLibros:
                                    libro.setEstado("Inhabilitado")
                            else:
                                print("Libro no encontrado")

                    elif option1_3 == 5:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option1 == 4:
                while True:
                    menu_admin_copias()
                    option1_4 = int(input("Opcion: "))

                    if option1_4 == 1:
                        print("-- Registra copias --")
                        id_copia = int(input("Ingresa identificador de la copia: "))
                        estado = str(input("Ingresa el estado de la copia: "))
                        isbn = int(input("Ingresa el ISBN del libro: "))
                        copia = Copia(id_copia, estado, isbn)
                        listaCopias.append(copia)
                    elif option1_4 == 2:
                        print("-- Busca copias --")
                        id_copia = int(input("Identificador de la copia: "))
                        copia_encontrada = False
                        for ident in listaCopias:
                            if ident.identificador == id_copia:
                                print(ident)
                                copia_encontrada = True
                                break
                            else:
                                print("La copia solicitada no está en el sistema")
                    elif option1_4 == 3:
                        print("-- Eliminar la copia --")
                        id_copia = int(input("Identificador de la copia: "))
                        copia_encontrada = False
                        for ident in listaCopias:
                            if ident.identificador == id_copia:
                                listaCopias.remove(ident)
                                copia_encontrada = True
                                print("Copia eliminada")
                                break
                            else:
                                print("La copia solicitada no está en el sistema")                       

                    elif option1_4 == 4:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option1 == 5:
                while True:
                    menu_admin_info_autores()
                    option1_5 = int(input("Opcion: "))

                    if option1_5 == 1:
                        print("-- Registra autor --")
                        id_autor = int(input("Ingresa identificador del autor: "))
                        nombre = str(input("Ingresa nombre del autor: "))
                        nacionalidad = str(input("Ingresa la nacionalidad del autor: "))
                        fecha_nacimiento = str(input("Ingresa la fecha de nacimiento del autor: "))
                        autor = Autor(id_autor, nombre, nacionalidad, fecha_nacimiento)
                        listaAutores.append(autor)

                    elif option1_5 == 2:
                        print("-- Busca autor --")
                        id_autor = int(input("Identificador del autor: "))
                        for ident in listaAutores:
                            if ident.id_autor == id_autor:
                                ident.verAutor()
                                break
                            else:
                                print("El autor solicitado no está en el sistema")

                    elif option1_5 == 3:
                        print("-- Modifica detalles de autor --")
                        id_autor = int(input("Identificador del autor: "))
                        for ident in listaAutores:
                            if ident.id_autor == id_autor:
                                ident.modificarDatos()
                                break
                            else:
                                print("El autor solicitado no está en el sistema")

                    elif option1_5 == 4:
                        print("-- Asociar libro a autor --")
                        id_autor = int(input("Identificador del autor: "))
                        for ident1 in listaAutores:
                            if ident1.id_autor == id_autor:
                                id_prod = int(input("Identificador de producto: "))
                                for ident2 in listaArtiCientificos or ident2 in listaLibros or ident2 in listaTesis:
                                    if ident2.doi == id_prod or ident2.isbn == id_prod or ident2.id_tesis == id_prod:
                                        ident1.agregarLibro(ident2)
                                    else:
                                        print("El producto solicitado no está en el sistema")
                                break
                            else:
                                print("El autor solicitado no está en el sistema")

                    elif option1_5 == 5:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option1 == 6:
                        print("...")
                        break
            else:
                print("Opcion invalida, intente nuevamente")

    elif main_option == 2:
        while True:
            menu_administracion_usuarios()
            option2 = int(input("Opcion: "))

            if option2 == 1:
                while True:
                    menu_admin_bibliotecario()
                    option2_1 = int(input("Opcion: "))

                    if option2_1 == 1:
                        pass
                    elif option2_1 == 2:
                        pass
                    elif option2_1 == 3:
                        pass
                    elif option2_1 == 4:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option2 == 2:
                while True:
                    menu_admin_lector()
                    option2_2 = int(input("Opcion: "))

                    if option2_2 == 1:
                        pass
                    elif option2_2 == 2:
                        pass
                    elif option2_2 == 3:
                        pass
                    elif option2_2 == 4:
                        pass
                    elif option2_2 == 5:
                        pass
                    elif option2_2 == 6:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option2 == 3:
                        print("...")
                        break
            else:
                print("Opcion invalida, intente nuevamente")


    elif main_option == 3:
        while True:
            menu_administracion_prestamos()
            option3 = int(input("Opcion: "))

            if option3 == 1:
                while True:
                    menu_admi_transacciones()
                    option3_1 = int(input("Opcion: "))

                    if option3_1 == 1:
                        
                            id_lector = input("Ingrese el ID del lector: ")
                            lector = next((l for l in listaLectores if l.getId() == id_lector), None)
                            if not lector:
                                print("Lector no encontrado.")
                                #return
                            
                            id_libro = input("Ingrese el ID del libro: ")
                            libro = next((l for l in listaLibros if l.getIsbn() == id_libro), None)
                            if not libro:
                                print("Libro no encontrado.")
                                #return
                            
                            if libro.getEstado() != "disponible":
                                print("Libro no disponible para préstamo.")
                                #return
                            
                            dias_prestamo = int(input("Ingrese los días de préstamo (máximo 3): "))
                            fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
                            prestamo = Prestamo(len(prestamo) + 1, id_libro, id_lector, dias_prestamo, fecha_prestamo)
                            listaPrestamos.append(prestamo)
                            lector.agregarLibroPrestado(libro)
                            libro.setEstado("prestado")
                            print(f"Préstamo registrado exitosamente. Fecha de devolución: {prestamo.getFechaEntrega().strftime('%Y-%m-%d')}")

                    elif option3_1 == 2:

                        id_lector = input("Ingrese el ID del lector: ")
                        lector = next((l for l in listaLectores if l.getId() == id_lector), None)
                        if not lector:
                            print("Lector no encontrado.")
                            #return
                        
                        id_libro = input("Ingrese el ID del libro: ")
                        libro = next((l for l in listaLibros if l.getIsbn() == id_libro), None)
                        if not libro:
                            print("Libro no encontrado.")
                            #return
                        
                        prestamo = next((p for p in listaPrestamos if p.getIdLector() == id_lector and p.getIdLibro() == id_libro), None)
                        if not prestamo:
                            print("Préstamo no encontrado.")
                            #return
                        
                        fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
                        multa = Multa(len(multa) + 1, prestamo)
                        multa.generar_multa(fecha_devolucion)
                        listaMultas.append(multa)
                        
                        if multa.estado == "activa":
                            print(f"Préstamo devuelto con retraso. Multa generada por {multa.dias_retraso} días de retraso. Valor de la multa: {multa.dias_retraso * 3000}")

                        else:
                            print("Préstamo devuelto exitosamente sin multa.")

                        lector.removerLibroPrestado(libro)
                        libro.setEstado("disponible")
                        
                    elif option3_1 == 3:
                        pass
                    elif option3_1 == 4:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option3 == 2:
                while True:
                    menu_admi_multas()
                    option3_2 = int(input("Opcion: "))

                    if option3_2 == 1:
                        pass
                    elif option3_2 == 2:
                        pass
                    elif option3_2 == 3:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")
            elif option3 == 3:
                print("...")
                break
            else:
                print("Opcion invalida, intente nuevamente")

    elif main_option == 4:
        print("Hasta pronto!")
        break

    else:
        print("Opcion invalida, intente nuevamente")
