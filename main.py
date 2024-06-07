from clases.ArticuloCientifico import *
from clases.Autor import *
from clases.Bibliotecario import *
from clases.Categoria import *
from clases.Copias import *
from clases.Factory import *
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
categoria1 = Categoria("11", "Fantasía", "Un mundo de maravillas ome")
categoria2 = Categoria("12", "Realismo mágico", "Otro mundo de maravillas ome")
categoria3 = Categoria("13", "Distopía", "Un mundo diferente al que conocemos ome")
categoria4 = Categoria("14", "Novela romántica", "Un mundo lleno de romance omeee")
categoria5 = Categoria("15", "Novela picaresca", "Un mundo re picaro omeee")
categoria6 = Categoria("16", "Novela de aventuras", "Un mundo lleno de aventuras y exploraciones ome")
categoria7 = Categoria("17", "Literatura infantil", "Un mundo de aventuras infantiles ome")
categoria8 = Categoria("18", "Novela juvenil", "Un mundo de aventuras juveniles ome")
categoria9 = Categoria("19", "Ficción absurda", "Un mundo lleno de aventuras absurdas ome")
listaCategorias.append(categoria1)
listaCategorias.append(categoria2)
listaCategorias.append(categoria3)
listaCategorias.append(categoria4)
listaCategorias.append(categoria5)
listaCategorias.append(categoria6)
listaCategorias.append(categoria7)
listaCategorias.append(categoria8)
listaCategorias.append(categoria9)

autor2 = Autor("1","J.K. Rowling", "Británica", "31 de julio de 1965")
listaAutores.append(autor2)
libro2 = Libro("Harry Potter y la piedra filosofal", "9788478884455", "Edición especial", 1997, "Salamandra", "Usado", "Español", 50, categoria1.getNombre(), [autor2])
listaLibros.append(libro2)
autor2.libros.append(libro2)

autor3 = Autor("2","Gabriel García Márquez", "Colombiana", "6 de marzo de 1927")
listaAutores.append(autor3)
libro3 = Libro("Cien años de soledad", "9788437615030", "Edición conmemorativa", 1967, "Diana", "Nuevo", "Español", 80, categoria2.getNombre(), [autor3])
listaLibros.append(libro3)
autor3.libros.append(libro3)


autor4 = Autor("3","George Orwell", "Británica", "25 de junio de 1903")
listaAutores.append(autor4)
libro4 = Libro("1984", "9780141036144", "Reedición", 1949, "Penguin Books", "Usado", "Inglés", 10, categoria3.getNombre(), [autor4])
listaLibros.append(libro4)
autor4.libros.append(libro4)

autor5 = Autor("4","Jane Austen", "Británica", "16 de diciembre de 1775")
listaAutores.append(autor5)
libro5 = Libro("Orgullo y prejuicio", "9788497940821", "Edición ilustrada", 1813, "Alba Editorial", "Nuevo", "Español", 70, categoria4.getNombre(), [autor5])
listaLibros.append(libro5)
autor5.libros.append(libro5)

autor6 = Autor("5","Miguel de Cervantes", "Española", "29 de septiembre de 1547")
listaAutores.append(autor6)
libro6 = Libro("Don Quijote de la Mancha", "9788420412146", "Edición crítica", 1605, "Alfaguara", "Usado", "Español", 90, categoria5.getNombre(), [autor6])
listaLibros.append(libro6)
autor6.libros.append(libro6)

autor7 = Autor("6","Herman Melville", "Estadounidense", "1 de agosto de 1819")
listaAutores.append(autor7)
libro7 = Libro("Moby Dick", "9788491050364", "Edición de lujo", 1851, "Alba Editorial", "Nuevo", "Español", 40, categoria6.getNombre(), [autor7])
listaLibros.append(libro7)
autor7.libros.append(libro7)

autor8 = Autor("7","Antoine de Saint-Exupéry", "Francés", "29 de junio de 1900")
listaAutores.append(autor8)
libro8 = Libro("El principito", "9780547964069", "Edición de colección", 1943, "Houghton Mifflin Harcourt", "Usado", "Español", 120, categoria7.getNombre(), [autor8])
listaLibros.append(libro8)
autor8.libros.append(libro8)

autor9 = Autor("8","Mark Twain", "Estadounidense", "30 de noviembre de 1835")
listaAutores.append(autor9)
libro9 = Libro("Las aventuras de Tom Sawyer", "9788491815234", "Edición especial", 1876, "Penguin Clásicos", "Nuevo", "Español", 55, categoria8.getNombre(), [autor9])
listaLibros.append(libro9)
autor9.libros.append(libro9)

autor10 = Autor("9","Franz Kafka", "Austrohúngaro", "3 de julio de 1883")
listaAutores.append(autor10)

libro10 = Libro("La metamorfosis", "9788483461646", "Edición anotada", 1915, "Editorial Losada", "Nuevo", "Español", 65, categoria9.getNombre(), [autor10])
listaLibros.append(libro10)
autor10.libros.append(libro10)

autor1 = Autor("5", "Rafael Camilo Lopez Gomez", "Colombia", "04-07-1987")
tesis1 = Tesis("10", autor1, "UTP", "23-06-2023", "05-12-2023", "Ingenieria", "Disponible", 10)

listaAutores.append(autor1)
listaTesis.append(tesis1)

articC1 = ArticuloCientifico("Redaccion a la fisica cuantica", "2354", "Editorial planeta", "23-4-2023", "3 semanas", "Vol 1", "Fisica cuantica", "Disponible")
listaArtiCientificos.append(articC1)

bibliotecario1 = Bibliotecario("Alejandro Magno", "20", "323432023", "Cra 32 # 433-543")
listaBibliotecarios.append(bibliotecario1)

lector1 = Lector("Carlos Dario", "10", "321323443", "Calle falsa # 123", "Normal")
lector2 = Lector("Jose Manuel", "11", "321323443", "Calle real # 123", "Sancionado")
lector3 = Lector("Manuela Garcia", "12", "321323443", "Calle quien sabe # 123", "Suspendido")
listaLectores.append(lector1)
listaLectores.append(lector2)
listaLectores.append(lector3)

prestamo1 = Prestamo("1", "1984", "2", lector1.getNombre(), 3, 24-7-6, 24-10-6)
listaPrestamos.append(prestamo1)


# MAIN PROGRAM #
while True:
    factory = Factory()     # Posicion de la fabrica
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
                        autor = input("Ingresa nombre de autor(es): ")
                        institucion = input("Ingresa la institucion de estudios: ")
                        fecha_investigacion = input("Ingresa la fecha de investigacion: ")
                        fecha_presentacion = input("Ingresa la fecha de presentacion: ")
                        campo = input("Ingresa el campo de estudios: ")
                        estado = input("Ingresa el estado: ")
                        num_paginas = int(input("Ingresa el numero de paginas: "))
                        tesis = factory.crear_tesis(id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, num_paginas)
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
                                
                    elif option1_1 == 3:
                        print("-- Modifica detalles de una tesis --")
                        id_tes = int(input("Identificador de la tesis: "))
                        for ident in listaTesis:
                            if ident.id_tesis == id_tes:
                                nuevo_autor = input("Nombre del nuevo autor: ")
                                nueva_institucion = input("Nueva institucion: ")
                                nueva_fecha_investigacion = input("Nueva fecha investigacion: ")
                                nueva_fecha_presentacion = input("Nueva fecha de presentacion: ")
                                nuevo_campo = input("Nuevo campo: ")
                                nuevo_estado = input("Nuevo estado: ")
                                nuevo_num_paginas = int(input("Nuevo numero de paginas: "))
                                ident.modificarDatos(nuevo_autor, nueva_institucion, nueva_fecha_investigacion, nuevo_campo, nuevo_estado, nuevo_num_paginas)
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
                        titulo = input("Ingresa el titulo del articulo: ")
                        doi = input("Ingresa el identificador DOI del articulo: ")
                        editor = input("Ingresa el editor del articulo: ")
                        fecha_publicacion = input("Ingresa la fecha de publicacion del articulo: ")
                        periodicidad = input("Ingresa la periodicidad del articulo: ")
                        volumen = input("Ingresa el volumen del articulo: ")
                        campo_interes = input("Ingresa el campo de interes del articulo: ")
                        estado = input("Ingresa estado del articulo: ")
                        artCienti = factory.crear_articulo(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado)
                        listaArtiCientificos.append(artCienti)

                    elif option1_2 == 2:
                        print("-- Busca articulo cientifico --")
                        id_doi = input("Identificador DOI del articulo cientifico: ")
                        for ident in listaArtiCientificos:
                            if ident.doi == id_doi:
                                ident.verArticuloCientifico()
                                break
                        else:
                            print("El articulo solicitado no está en el sistema")

                    elif option1_2 == 3:
                        print("-- Modifica un articulo cientifico --")
                        id_doi = input("Identificador DOI del articulo cientifico: ")
                        for ident in listaArtiCientificos:
                            if ident.doi == id_doi:
                                nuevo_titulo = input("Ingrese el nuevo titulo: ")
                                nuevo_doi = input("Ingrese el nuevo DOI: ")
                                nuevo_editor = input("Ingrese el nuevo editor: ")
                                nueva_fecha_publicacion = input("Ingrese la nueva fecha de publicacion: ")
                                nueva_periodicidad = input("Ingrese la nueva periodicidad: ")
                                nuevo_volumen = input("Ingrese el nuevo volumen: ")
                                nuevo_campo_interes = input("Ingrese el nuevo campo de interes: ")
                                nuevo_estado = input("Ingrese el nuevo estado: ")
                                ident.modificarDatos(nuevo_titulo, nuevo_doi, nuevo_editor, nueva_fecha_publicacion, nueva_periodicidad, nuevo_volumen, nuevo_campo_interes, nuevo_estado)
                                break
                        else:
                            print("El articulo solicitado no está en el sistema")

                    elif option1_2 == 4:
                        print("-- Elimina un articulo cientifico --")
                        id_doi = input("Identificador DOI del articulo cientifico: ")
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
                        print("-- Registra un libro --")
                        titulo = input("Titulo: ")
                        isbn = input("ISBN: ")
                        edicion = input("Edicion: ")
                        ano_publicacion = int(input("Año de publicacion: "))
                        editorial = input("Editorial: ")
                        estado = input("Estado: ")
                        idioma = input("Idioma: ")
                        num_copias = int(input("Numero de copias: "))
                        categoria = input("Categoria: ")

                        for identC in listaCategorias:
                            if identC.getNombre() != categoria:
                                print(f"Categoria {categoria} no encontrada.")
                                print("Desea añadir la categoria? (S/N)")
                                respuesta = input("Respuesta: ")
                                if respuesta == "S" or respuesta == "s":
                                    id_cat = input("Ingrese identificador de la categoria: ")
                                    descripcion = input("Ingrese descripcion de la categoria: ")
                                    cat_instancia = Categoria(id_cat, categoria, descripcion)
                                listaCategorias.append(cat_instancia)
                                break
                            else:
                                print("Categoria")
                        else:
                            print("Paila categoria, no se por que")

                        nombre_autor = input("Autor(es): ")

                        for ident in listaAutores:
                            if ident.getNombre != nombre_autor:
                                print(f"Autor {nombre_autor} no encontrado.")
                                print("Desea añadir el autor? (S/N)")
                                respuesta = input("Respuesta: ")
                                if respuesta == "S" or respuesta == "s":
                                    id_autor = input("Identificador del autor: ")
                                    nacionalidad = input("Nacionalidad: ")
                                    fecha_nacimiento = input("Fecha de nacimiento: ")
                                    autor = Autor(id_autor, nombre_autor, nacionalidad, fecha_nacimiento)
                                listaAutores.append(autor)
                                break
                            else:
                                print("Ah no listo")    
                        else:
                            print("Paila autor, no se por que")          
                        
                        libro = factory.crear_libro(titulo, isbn, edicion, ano_publicacion, editorial, estado, idioma, num_copias, categoria, [autor])
                        listaLibros.append(libro)
                        autor.agregarLibro(libro)
                        print("Libro registrado al sistema")
                
                    elif option1_3 == 2:
                        print("\n")
                        print("-- Busca un libro --")
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
                        print("-- Modifica detalles de un libro --")
                        print("Busca por...")
                        print("1. Por ISBN")
                        print("2. Por título")
                        opcion_busqueda = int(input("Opción: "))
                        if opcion_busqueda == 1:
                            isbn = input("ISBN: ")
                            libro = next((libro for libro in listaLibros if libro.getIsbn() == isbn), None)
                            if libro is not None:
                                nuevo_titulo = input("Nuevo titulo: ")
                                nuevo_isbn = input("Nuevo ISBN: ")
                                nueva_edicion = input("Nueva edicion: ")
                                nuevo_ano_publicacion = int(input("Nuevo año de publicación: "))
                                nueva_editorial = input("Nueva editorial: ")
                                nuevo_estado = input("Nuevo estado: ")
                                nuevo_idioma = input("Nuevo idioma: ")
                                nuevo_num_copias = int(input("Nuevo número de copias: "))
                                nueva_categoria = input("Nueva categoria: ") 
                                
                                libro.modificarDatos(nuevo_titulo, nuevo_isbn, nueva_edicion, nuevo_ano_publicacion, nueva_editorial, nuevo_estado, nuevo_idioma, nuevo_num_copias, nueva_categoria, nuevo_autor=nombre_autor)                           

                            else:
                                print("Libro no encontrado")

                        elif opcion_busqueda == 2:
                            titulo = input("Título: ")
                            libro = next((libro for libro in listaLibros if libro.getTitulo() == titulo), None)
                            if libro is not None:
                                nuevo_titulo = input("Nuevo titulo: ")
                                nuevo_isbn = input("Nuevo ISBN: ")
                                nueva_edicion = input("Nueva edicion: ")
                                nuevo_ano_publicacion = int(input("Nuevo año de publicación: "))
                                nueva_editorial = input("Nueva editorial: ")
                                nuevo_estado = input("Nuevo estado: ")
                                nuevo_idioma = input("Nuevo idioma: ")
                                nuevo_num_copias = int(input("Nuevo número de copias: "))
                                nueva_categoria = input("Nueva categoria: ")
                                nuevo_autor = input("Nuevo autor")

                                libro.modificarDatos(nuevo_titulo, nuevo_isbn, nueva_edicion, nuevo_ano_publicacion, nueva_editorial, nuevo_estado, nuevo_idioma, nuevo_num_copias, nueva_categoria, nuevo_autor=nombre_autor)                           

                            else:
                                print("Libro no encontrado")                                                                  
                    
                    elif option1_3 == 4:
                        print("\n")
                        print("Inhabilitar libro")
                        print("Busca por...")
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
                    menu_admin_categorias()
                    option1_4 = int(input("Opcion: "))

                    if option1_4 == 1:
                        print("-- Registra categoria --")
                        id_cat = input("Ingresa identificador de la categoria: ")
                        nombre = input("Ingresa el nombre de la categoria: ")
                        descripcion = input("Ingresa descripcion de la categoria: ")
                        categoria = Categoria(id_cat, nombre, descripcion)
                        listaCategorias.append(categoria)
                        print("Categoria registrada")

                    elif option1_4 == 2:
                        print("-- Busca categoria --")
                        print("1. Por identificador")
                        print("2. Por nombre")
                        opcion_busqu = int(input("Opcion: "))
                        
                        if opcion_busqu == 1:
                            id_cat = input("Identificador de la categoria: ")
                            categoria_encontrada = False
                            for ident in listaCategorias:
                                if ident.id == id_cat:
                                    ident.verCategoria()
                                    categoria_encontrada = True
                                    break
                            else:
                                print("La categoria solicitada no está en el sistema")
                        
                        elif opcion_busqu == 2:
                            nombre = input("Nombre de la categoria: ")
                            categoria_encontrada = False
                            for ident in listaCategorias:
                                if ident.nombre == nombre:
                                    ident.verCategoria()
                                    categoria_encontrada = True
                                    break
                            else:
                                print("La categoria solicitada no está en el sistema")                       
                    
                    elif option1_4 == 3:
                        print("-- Modifica una categoria --")
                        id_cat = input("Identificador de la categoria: ")
                        categoria_encontrada = False
                        for ident in listaCategorias:
                            if ident.id == id_cat:
                                nuevo_id = input("Nuevo identificador: ")
                                nuevo_nombre = input("Nuevo nombre: ")
                                nueva_desc = input("Nueva descripcion: ")
                                ident.modificarDatos(nuevo_id, nuevo_nombre, nueva_desc)
                                categoria_encontrada = True
                                print("Categoria modificada")
                                break
                        else:
                            print("La categoria solicitada no está en el sistema")

                    elif option1_4 == 4:
                        print("-- Elimina una categoria --")
                        id_cat = input("Identificador de la categoria: ")
                        categoria_encontrada = False
                        for ident in listaCategorias:
                            if ident.id == id_cat:
                                listaCategorias.remove(ident)
                                categoria_encontrada = True
                                print("Categoria eliminada")
                                break
                        else:
                            print("La categoria solicitada no está en el sistema")                       

                    elif option1_4 == 5:
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
                        id_autor = input("Ingresa identificador del autor: ")
                        nombre = input("Ingresa nombre del autor: ")
                        nacionalidad = input("Ingresa la nacionalidad del autor: ")
                        fecha_nacimiento = input("Ingresa la fecha de nacimiento del autor: ")
                        autor = Autor(id_autor, nombre, nacionalidad, fecha_nacimiento)
                        listaAutores.append(autor)

                    elif option1_5 == 2:
                        print("-- Busca autor --")
                        print("1. Por identificador")
                        print("2. Por nombre")
                        opcion_busq = int(input("Opcion: "))
                        
                        if opcion_busq == 1:
                            id_autor = input("Identificador del autor: ")
                            for ident in listaAutores:
                                if ident.id_autor == id_autor:
                                    ident.verAutor()
                                    break
                            else:
                                print("El autor solicitado no está en el sistema")
                        
                        elif opcion_busq == 2:
                            nombre_autor = input("Nombre del autor: ")
                            for ident in listaAutores:
                                if ident.nombre == nombre_autor:
                                    ident.verAutor()
                                    break
                            else:
                                print("El autor solicitado no está en el sistema")

                    elif option1_5 == 3:
                        print("-- Modifica detalles de autor --")
                        id_autor = input("Identificador del autor: ")
                        for ident in listaAutores:
                            if ident.id_autor == id_autor:
                                nuevo_id = input("Nuevo identificador: ")
                                nuevo_nombre = input("Nuevo nombre: ")
                                nueva_nacionalidad = input("Nueva nacionalidad: ")
                                nueva_fechaNac = input("Nueva fecha de nacimiento: ")
                                ident.modificarDatos(nuevo_id, nuevo_nombre, nueva_nacionalidad, nueva_fechaNac)
                                print("Autor modificado")
                                break
                        else:
                            print("El autor solicitado no está en el sistema")

                    elif option1_5 == 4:
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
                        nombre = input("Nombre del Bibliotecario: ")
                        id = input("ID: ")
                        telefono = int(input("Teléfono: "))
                        direccion = input("Dirección: ")
                        bibliotecario = Bibliotecario(nombre, id, telefono, direccion)
                        listaBibliotecarios.append(bibliotecario)
                        print("Bibliotecario agregado")
                        
                    elif option2_1 == 2:
                        print("-- Busca Bibliotecario --")
                        id_biblio = input("Identificador Bibliotecario: ")
                        for ident in listaBibliotecarios:
                            if ident.id == id_biblio:
                                ident.verBibliotecario()
                                break
                        else:
                            print("El Bibliotecario solicitado no está en el sistema")

                    elif option2_1 == 3:
                        print("-- Modifica detalles de un bibliotecario --")
                        id_biblio = input("Identificador del bibliotecario a modificar: ")
                        for ident in listaBibliotecarios:
                            if ident.id == id_biblio:
                                nombre = input("Nombre del bibliotecario: ")
                                id = input("ID: ")
                                telefono = int(input("Teléfono: "))
                                direccion = input("Dirección: ")
                                bibliotecario = Bibliotecario(nombre, id, telefono, direccion)
                                ident.modificarDatos(nombre, id, telefono, direccion)
                                print("Bibliotecario modificado con éxito!")   
                                break
                        else:
                            print("El bibliotecario solicitado no está en el sistema")
                        
                    elif option2_1 == 4:
                        print("-- Elimina un bibliotecario --")
                        id_biblio = input("Identificador bibliotecario: ")
                        for ident in listaBibliotecarios:
                            found = False
                            if ident.id == id_biblio:
                                listaBibliotecarios.remove(ident)
                                print("El bibliotecario se ha eliminado del sistema")
                                found  = True
                                break
                        if found == False:
                            print("El bibliotecario solicitado no está en el sistema")

                    elif option2_1 == 5:
                        print("...")
                        break
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option2 == 2:
                while True:
                    menu_admin_lector()
                    option2_2 = int(input("Opcion: "))

                    if option2_2 == 1:
                        nombre = input("Nombre del lector: ")
                        id = input("ID: ")
                        telefono = int(input("Teléfono: "))
                        direccion = input("Dirección: ")
                        estado = input("Estado: ")
                        lector = Lector(nombre, id, telefono, direccion, estado)
                        listaLectores.append(lector)
                        print("Lector agregado")
                    
                    elif option2_2 == 2:
                        print("-- Busca Lector --")
                        id_lector = input("Identificador del lector: ")
                        for ident in listaLectores:
                            if ident.id == id_lector:
                                ident.verLector()
                                break
                        else:
                            print("El lector solicitado no está en el sistema")

                    elif option2_2 == 3:
                        print("-- Modifica detalles de un lector --")
                        id_lector = input("Identificador del lector a modificar: ")
                        for ident in listaLectores:
                            if ident.id == id_lector:
                                nombre = input("Nombre del lector: ")
                                id = input("ID: ")
                                telefono = int(input("Teléfono: "))
                                direccion = input("Dirección: ")
                                estado = input("Estado: ")
                                lector = Lector(nombre, id, telefono, direccion, estado)
                                ident.modificarDatos(nombre, id, telefono, direccion, estado)
                                print("Lector modificado con éxito!")   
                                break
                        else:
                            print("El lector solicitado no está en el sistema")

                    elif option2_2 == 4:
                        print("-- Habilita un lector --")
                        id_lector = input("Identificador del lector a habilitar: ")
                        for ident in listaLectores:
                            if ident.id == id_lector:
                                ident.setEstado("Habilitado")
                                print("Lector habilitado con éxito!")
                                break
                        else:
                            print("El lector solicitado no está en el sistema")

                    elif option2_2 == 5:
                        print("-- Inhabilita un lector --")
                        id_lector = input("Identificador del lector a inhabilitar: ")
                        for ident in listaLectores:
                            if ident.id == id_lector:
                                ident.setEstado("Inhabilitado")
                                print("Lector inhabilitado con éxito!")
                                break
                        else:
                            print("El lector solicitado no está en el sistema")

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
            menu_administracion_transacciones()
            option3 = int(input("Opcion: "))

            if option3 == 1:
                while True:
                    menu_admi_prestamos()
                    option3_1 = int(input("Opcion: "))

                    if option3_1 == 1:
                        libro = input("Título del libro a buscar: ")
                        for ident in listaLibros:
                            if ident.titulo == libro:
                                copias_disponibles = ident.buscar_copias_disponibles()
                                if copias_disponibles:
                                    print("Copias disponibles:")
                                    for i, copia in enumerate(copias_disponibles, 1):
                                        print(f"{i}. {copia-{i}.verCopia()}")
                                    opcion_copia = input("Seleccione el número de copia que desea prestar: ")
                                    try:
                                        indice_copia = int(opcion_copia) - 1
                                        copia_seleccionada = copias_disponibles[indice_copia]
                                        id_prestamo = input("Ingrese identificador del prestamo: ")
                                        lector = input("Ingrese id del lector: ")
                                        dias_prest = int(input("Ingrese el numero de dias de prestamo: "))
                                        fecha_prestamo =input("Ingrese fecha de prestamo (YYYY-MM-DD): ")
                                        fecha_entrega = input("Ingrese fecha de entrega (YYYY-MM-DD): ")
                                        prestamo = Prestamo(id_prestamo, libro, copia_seleccionada, lector, dias_prest, fecha_prestamo, fecha_entrega)
                                        listaPrestamos.append(prestamo)
                                        if prestamo:
                                            print("Prestamo realizado")
                                        else:
                                            print("Fallo al registrar prestamo")

                                        # Código para registrar préstamo de la copia seleccionada
                                    except ValueError:
                                        print("Entrada inválida. Introduzca un número válido.")
                                    except IndexError:
                                        print("Número de copia seleccionada fuera de rango.")
                                else:
                                    print("No hay copias disponibles en la biblioteca.")
                        '''else:
                            print("Libro no encontrado.")'''
                    
                    elif option3_1 == 2:
                        print("-- Busca un prestamo --")
                        id_pres = input("Ingrese identificador del prestamo: ")
                        for ident in listaPrestamos:
                            if ident.id_prestamo == id_pres:
                                ident.verPrestamo()
                                break
                        else:
                            print("El prestamo solicitado no está en el sistema")

                    elif option3_1 == 3:
                        print("-- Devolver un prestamo --")
                        id_lector = input("Ingrese el ID del lector: ")
                        lector = next((l for l in listaLectores if l.getId() == id_lector), None)
                        if not lector:
                            print("Lector no encontrado.")
                            break
                        
                        id_libro = input("Ingrese el ID del libro: ")
                        libro = next((l for l in listaLibros if l.getId() == id_libro), None)
                        if not libro:
                            print("Libro no encontrado.")
                            break
                        
                        prestamo = next((p for p in listaPrestamos if p.getIdLector() == id_lector and p.getIdLibro() == id_libro), None)
                        if not prestamo:
                            print("Préstamo no encontrado.")
                            break
                        
                        fecha_devolucion = datetime.now().strftime("%Y-%m-%d")
                        multa = Multa(len(multa) + 1, prestamo)
                        multa.generar_multa(fecha_devolucion)
                        listaMultas.append(multa)
                        
                        if multa.estado == "activa":
                            print(f"Préstamo devuelto con retraso. Multa generada por {multa.dias_retraso} días de retraso. Valor de la multa: {multa.calcular_multa()}")

                        else:
                            print("Préstamo devuelto exitosamente sin multa.")

                        lector.removerLibroPrestado(libro)
                        libro.setEstado("disponible")
                    
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

                        id_lector = input("Ingrese el ID del lector: ")
                        lector = next((l for l in listaLectores if l.getId() == id_lector), None)
                        if not lector:
                            print("Lector no encontrado.")
                            break
                        
                        monto = float(input("Ingrese el monto de la multa: "))
                        multa = Multa(lector, monto, "activa")
                        listaMultas.append(multa)
                        lector.agregarMulta(multa)
                        print("Multa aplicada exitosamente.")

                    elif option3_2 == 2:

                        id_lector = int(input("Ingrese el ID del lector: "))
                        lector = next((l for l in listaLectores if l.getId() == id_lector), None)
                        if not lector:
                            print("Lector no encontrado.")
                            break
                        
                        monto = float(input("Ingrese el monto de la multa a levantar: "))
                        multa = next((m for m in listaMultas if m.getLector() == lector and m.getMonto() == monto and m.getEstado() == "activa"), None)
                        if not multa:
                            print("Multa no encontrada.")
                            break
                        
                        lector.levantarMulta(multa)
                        print("Multa levantada exitosamente.")

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