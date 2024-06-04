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
artiCientificos = []
autores = []
categorias = []
copias = []
lectores = []
libros = []
multas = []
prestamos = []
tesis = []
bibliotecarios = []

# OBJETOS QUEMADOS PARA PRUEBAS #
autor1 = Autor("Rafael Camilo Lopez Gomez", "Colombia", "04-07-1987")
tesis1 = Tesis(autor1, "UTP", "23-06-2023", "05-12-2023", "Ingenieria", "Disponible", 10)

autores.append(autor1)
tesis.append(tesis1)

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
                        pass
                    elif option1_1 == 2:
                        pass
                    elif option1_1 == 3:
                        pass
                    elif option1_1 == 4:
                        pass
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
                        pass
                    elif option1_2 == 2:
                        pass
                    elif option1_2 == 3:
                        pass
                    elif option1_2 == 4:
                        pass
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
                        pass
                    elif option1_5 == 2:
                        pass
                    elif option1_5 == 3:
                        pass
                    elif option1_5 == 4:
                        pass
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
                        pass
                    elif option3_1 == 2:
                        pass
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
