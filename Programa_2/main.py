from objetos import vehiculos

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Agregar mantenimiento a vehículo")
        print("2. Consultar mantenimientos de vehículo")
        print("3. Consultar detalles de vehiculos")
        print("0. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            for vehiculo in vehiculos:
                if vehiculo._marca == marca and vehiculo._modelo == modelo:
                    fecha = input("Ingrese la fecha del mantenimiento: ")
                    tipo = input("Ingrese el tipo de mantenimiento: ")
                    vehiculo.agregar_mantenimiento(fecha, tipo)
                    print("Mantenimiento agregado con éxito")
                    break
            else:
                print("Vehículo no encontrado")
        elif opcion == "2":
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            for vehiculo in vehiculos:
                if vehiculo._marca == marca and vehiculo._modelo == modelo:
                    print(f"Marca: {vehiculo._marca}")
                    print(f"Modelo: {vehiculo._modelo}")
                    print(f"Color: {vehiculo._color}")
                    print(f"Año: {vehiculo._año}")
                    print(f"Kilometraje: {vehiculo._kilometraje}")
                    print("Mantenimientos:")
                    for fecha, tipo in vehiculo.mostrar_mantenimientos():
                        print(f"Fecha: {fecha}, Tipo: {tipo}")
                    break
            else:
                print("Vehículo no encontrado")
        elif opcion == "3":
            for vehiculo in vehiculos:
                print(vehiculo.mostrar_detalle())
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()