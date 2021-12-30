from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    # @classmethod
    # def get_one(cls,data):
    #     query  = "SELECT * FROM users WHERE id = %(id)s";
    #     result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    #     return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name=%(fname)s,last_name=%(lname)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query  = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

