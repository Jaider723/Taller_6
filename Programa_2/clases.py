class Vehiculo:
    def __init__(self, marca, modelo, color, año, kilometraje):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._año = año
        self._kilometraje = kilometraje

    def mostrar_detalle(self):
        return f"{self._marca} {self._modelo} ({self._color}, {self._año})"

class Mantenimiento:
    def __init__(self):
        self._registro_mantenimientos = []

    def agregar_mantenimiento(self, fecha, tipo):
        self._registro_mantenimientos.append((fecha, tipo))

    def mostrar_mantenimientos(self):
        return self._registro_mantenimientos

class Coche(Vehiculo, Mantenimiento):
    def __init__(self, marca, modelo, color, año, kilometraje, tipo_combustible, capacidad_pasajeros):
        Vehiculo.__init__(self, marca, modelo, color, año, kilometraje)
        Mantenimiento.__init__(self)
        self._tipo_combustible = tipo_combustible
        self._capacidad_pasajeros = capacidad_pasajeros

class Motocicleta(Vehiculo, Mantenimiento):
    def __init__(self, marca, modelo, color, año, kilometraje, cilindrada):
        Vehiculo.__init__(self, marca, modelo, color, año, kilometraje)
        Mantenimiento.__init__(self)
        self._cilindrada = cilindrada

class Camion(Vehiculo, Mantenimiento):
    def __init__(self, marca, modelo, color, año, kilometraje, capacidad_carga):
        Vehiculo.__init__(self, marca, modelo, color, año, kilometraje)
        Mantenimiento.__init__(self)
        self._capacidad_carga = capacidad_carga

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, año, tipo_bicicleta):
        Vehiculo.__init__(self, marca, modelo, color, año, 0) # Kilometraje no aplicable
        self._tipo_bicicleta = tipo_bicicleta

class PatinetaElectrica(Vehiculo):
    def __init__(self, marca, modelo, color, año, autonomia_bateria):
        Vehiculo.__init__(self, marca, modelo, color, año, 0) # Kilometraje no aplicable
        self._autonomia_bateria = autonomia_bateria
