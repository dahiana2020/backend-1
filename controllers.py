from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        if (email == "test@gmail.com" and password == "12345"):
            return jsonify({"auth": True, "name": "Pepe Perez", "token": token}), 200
        return jsonify({"auth": False}), 401

class RegistroUserControllers(MethodView):

    def post(self):
    
        time.sleep(3)
        content = request.get_json()
        nombres = content.get("nombres")
        apellidos = content.get("apellidos")
        cedula = content.get("cedula")
        direccion = content.get("direccion")
        telefono = content.get("telefono")
        correo = content.get("correo")
        password = content.get("password")
        password_verifi = content.get("password_verifi")

        return jsonify({"login ok": True, "nombres": nombres, "apellidos": apellidos, "cedula": cedula, "direccion": direccion, "telefono": telefono, "correo": correo}), 200
    


class InicioSesionUserControllers(MethodView):

    def post(self):
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        return jsonify({"login ok": True, "email": email}), 200

class TablaControllers(MethodView):
    
  def get(self):
        productos = [{"id": 1, "nombre": "Arroz", "precio": 2000},
                    {"id": 2, "nombre": "Aceite", "precio": 2500},
                    {"id": 3, "nombre": "Papa", "precio": 1800},
                    {"id": 4, "nombre": "Panela", "precio": 4000},
                    {"id": 5, "nombre": "Arroz", "precio": 2000},
                    {"id": 6, "nombre": "Aceite", "precio": 2500},
                    {"id": 7, "nombre": "Papa", "precio": 1800},
                    {"id": 8, "nombre": "Panela", "precio": 4000},
                    {"id": 9, "nombre": "Arroz", "precio": 2000},
                    {"id": 10, "nombre": "Aceite", "precio": 2500},
                    {"id": 11, "nombre": "Papa", "precio": 1800},
                    {"id": 12, "nombre": "Panela", "precio": 4000},
                    ]
        return jsonify({"datos": productos}), 200
class CategoriasGranosUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasCarnesUserControllers(MethodView):
    
    def post(self):
       pass 

class CategoriasVerdurasUserControllers(MethodView):
    
    def post(self):
       pass