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
autor1 = Autor(5, "Rafael Camilo Lopez Gomez", "Colombia", "04-07-1987")
tesis1 = Tesis(10, autor1, "UTP", "23-06-2023", "05-12-2023", "Ingenieria", "Disponible", 10)

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
                        pass
                    elif option1_3 == 2:
                        pass
                    elif option1_3 == 3:
                        pass
                    elif option1_3 == 4:
                        pass
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
                        pass
                    elif option1_4 == 2:
                        pass
                    elif option1_4 == 3:
                        pass
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
                                break
                            
                            id_libro = input("Ingrese el ID del libro: ")
                            libro = next((l for l in listaLibros if l.getId() == id_libro), None)
                            if not libro:
                                print("Libro no encontrado.")
                                break
                            
                            if libro.getEstado() != "disponible":
                                print("Libro no disponible para préstamo.")
                                break
                            
                            dias_prestamo = int(input("Ingrese los días de préstamo (máximo 3): "))
                            fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
                            prestamo = Prestamo(len(prestamos) + 1, id_libro, id_lector, dias_prestamo, fecha_prestamo)
                            listaPrestamos.append(prestamo)
                            lector.agregarLibroPrestado(libro)
                            libro.setEstado("prestado")
                            print(f"Préstamo registrado exitosamente. Fecha de devolución: {prestamo.getFechaEntrega().strftime('%Y-%m-%d')}")

                    elif option3_1 == 2:

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
                                                
                    else:
                        print("Opcion invalida, intente nuevamente")

            elif option3 == 2:
                while True:
                    menu_admi_multas()
                    option3_2 = int(input("Opcion: "))

                    if option3_2 == 1:

                        id_lector = input("Ingrese el ID del lector: ")
                        lector = next((l for l in lectores if l.getId() == id_lector), None)
                        if not lector:
                            print("Lector no encontrado.")
                            break
                        
                        monto = float(input("Ingrese el monto de la multa: "))
                        multa = Multa(lector, monto, "activa")
                        multas.append(multa)
                        lector.agregarMulta(multa)
                        print("Multa aplicada exitosamente.")

                    elif option3_2 == 2:

                        id_lector = input("Ingrese el ID del lector: ")
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

                        else:
                            print("Préstamo devuelto exitosamente sin multa.")

                        lector.removerLibroPrestado(libro)
                        libro.setEstado("disponible")

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