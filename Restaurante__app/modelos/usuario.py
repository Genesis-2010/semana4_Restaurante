class Usuario:
    def __init__(self, nombre_usuario, correo):
        self.nombre_usuario = nombre_usuario
        self.correo = correo

    def iniciar_sesion(self):
        return f"El usuario {self.nombre_usuario} ha iniciado sesión."

    def __str__(self):
        return f"Usuario: {self.nombre_usuario} | Correo: {self.correo}"
    
    