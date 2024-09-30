from abc import ABC, abstractmethod

class Empleado_U03(ABC):
    def __init__(self, RFC, Apellidos, Nombres):
        self.__RFC = RFC
        self.__Apellidos = Apellidos
        self.__Nombres = Nombres
    def mostrar_info(self):
        return f"RFC: {self.__RFC}, Apellidos: {self.__Apellidos}, Nombres: {self.__Nombres}"
    @abstractmethod
    def calcular_sueldo(self):
        pass
class EmpleadoVendedor_U03(Empleado_U03):
    def __init__(self, RFC, Apellidos, Nombres, monto_vendido, tasa_comision):
        super().__init__(RFC, Apellidos, Nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision

    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision
    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return ingresos * 0.05
        else:
            return ingresos * 0.10 
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return ingresos * 0.10
        else:
            return ingresos * 0.15
    def calcular_sueldo(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        sueldo_neto = ingresos + bonificacion - descuento
        return sueldo_neto
class EmpleadoPermanente_U03(Empleado_U03):
    def __init__(self, RFC, Apellidos, Nombres, sueldo_base, nss):
        if sueldo_base < 150:
            raise SalarioInvalidoError(sueldo_base)
        super().__init__(RFC, Apellidos, Nombres)
        self.sueldo_base = sueldo_base
        self.nss = nss
    def calcular_ingresos(self):
        return self.sueldo_base
    def calcular_descuento(self):
        return self.sueldo_base * 0.11

    def calcular_sueldo(self):
        ingresos = self.calcular_ingresos()
        descuento = self.calcular_descuento()
        sueldo_neto = ingresos - descuento
        return sueldo_neto

class SalarioInvalidoError(Exception):
    def __init__(self, salario, mensaje="El salario no puede ser menor al mínimo de 150 pesos"):
        self.salario = salario
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def calcular_planta_empleados(empleados):
    for empleado in empleados:
        print(f"{empleado.mostrar_info()}")
        print(f"Sueldo Neto: {empleado.calcular_sueldo()}")
        print("---")

empleados = [
    EmpleadoVendedor_U03("BERU040421HMCCZRA2", "Becerril", "Uriel", 6000, 0.10),
    EmpleadoPermanente_U03("BERU040421HMCCZRA2", "Becerril", "Uriel", 2000, "123456789")
]

calcular_planta_empleados(empleados)
