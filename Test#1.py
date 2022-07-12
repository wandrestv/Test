from abc import ABC,abstractmethod

class Empleado(ABC):
    def __init__(self,nom,ced,tel,email,dir):## si tengo constructor, necesito metodos
        self.nombre_emp= nom
        self.cedula_emp= ced
        self._emp= tel
        self.correo_emp= email
        self.direccion_emp= dir

class Departamento:
    def __init__(self,nombre,telefono,codigo):
        self.nombre = nombre
        self.telefono = telefono
        self.codigo = codigo

class EmpleadoObre(Empleado):
    def __init__(self,nomb,cedu,tele,email,dir,horas_extra,años_servicio_obre):
        super().__init__(nomb,cedu,tele,email,dir)
        self.horas_extra = horas_extra
        self.años_servicio = años_servicio_obre

class Empleado_Admin(Empleado):
    _sueldo_admin = 600.00
    _des_iess = 0.0945
    def __init__(self,nomb,cedu,tele,email,dir,años_servicio_admin,estudios):
        super().__init__(nomb,cedu,tele,email,dir)
        self.años_servicio = años_servicio_admin
        self.estudios = estudios
    
    def Pago_admin(self):
        total_admin = Empleado_Admin._sueldo_admin * Empleado_Admin._des_iess
        return(total_admin)

class PagoSobretiempo:
    _sueldo_obre = 425.00
    _des_iess = 0.0945
    def __init__(self,horas,hora_entrada,hora_salida,pago_porHora,Horario):
        self.horas = horas
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.pago_porHora = pago_porHora
        self.Horario = Horario
    
    def Pago_obre(self):
        pago_extra = self.horas * self.pago_porHora
        total_ingreso_obre = pago_extra + PagoSobretiempo._sueldo_obre
        total_obre = total_ingreso_obre * PagoSobretiempo._des_iess
        return(total_obre)

class Nomina_Pago:
    def mostar_pago(self):
        pass



