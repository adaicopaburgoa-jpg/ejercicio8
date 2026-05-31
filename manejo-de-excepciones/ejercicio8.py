class SueldoInvalidoException(Exception):
    pass


class CargoInvalidoException(Exception):
    pass


class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Sueldo: {self.sueldo} Bs")
        print("-------------------------")


class Empresa:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.empleados = [None] * cantidad

    def contiene_numero(self, texto):
        for caracter in texto:
            if caracter.isdigit():
                return True
        return False

    def registrar_empleados(self):

        for i in range(len(self.empleados)):

            print(f"\nEmpleado {i + 1}")

            nombre = input("Ingrese nombre: ")

            while True:
                try:
                    cargo = input("Ingrese cargo: ")

                    if self.contiene_numero(cargo):
                        raise CargoInvalidoException(
                            "Error: El cargo no debe contener números."
                        )

                    break

                except CargoInvalidoException as e:
                    print(e)
                    print("Ingrese nuevamente el cargo.")

            try:
                sueldo = float(input("Ingrese sueldo: "))

                if sueldo < 2500:
                    raise SueldoInvalidoException(
                        "Error: El sueldo no puede ser menor a 2500 Bs."
                    )

            except SueldoInvalidoException as e:
                print(e)
                print("Se asignará automáticamente 2500 Bs.")
                sueldo = 2500

            self.empleados[i] = Empleado(nombre, cargo, sueldo)

    def mostrar_empleados(self):
        print(f"\n=== EMPLEADOS DE LA EMPRESA {self.nombre} ===")

        for i in range(len(self.empleados)):
            self.empleados[i].mostrar_datos()


nombre_empresa = input("Ingrese nombre de la empresa: ")
cantidad = int(input("Ingrese cantidad de empleados: "))

empresa = Empresa(nombre_empresa, cantidad)

empresa.registrar_empleados()

empresa.mostrar_empleados()