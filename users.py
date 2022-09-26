from mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        #data = {"id": 1, "first_name":"Elena", "last_name":"De Troya", "email":"elena@cd.com", "created_at":"2022-09-26", "updated_at":"2022-09-26"}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def guardar(cls, formulario):
        #formulario = {"first_name":"Juana", "last_name":"De Arco", "email":"juana@cd.com"}
        query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )" #->INSERT INTO users(first_name, last_name, email) VALUES('Juana', 'De Arco', 'juana@codingdojo.com')
        result = connectToMySQL('esquema_usuarios_ch').query_db(query, formulario)
        return result
