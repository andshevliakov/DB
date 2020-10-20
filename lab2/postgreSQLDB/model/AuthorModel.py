from model.DBmodel import DBModel
from storages.author import Author
import psycopg2

class AuthorModel(DBModel):
    def __init__(self , dbname , user , password , host ):
        super(AuthorModel, self).__init__(dbname , user, password , host)
        try:
            self.cursor = self.conn.cursor()
        except (Exception , psycopg2.DatabaseError) as error:
            print(error)

    def __del__(self):
        try:
            self.cursor.close()
        except (Exception , psycopg2.DatabaseError) as error:
            print(error)

    def add_entity(self , new_entity):
       request = 'INSERT INTO author(name , date_of_first_publication , year_of_birth , year_of_death) VALUES (%s, %s, %s, %s)'
       data = (new_entity.name, new_entity.date_of_first_publication, new_entity.year_of_birth, new_entity.year_of_death)
       try:
           self.cursor.execute(request, data)
           self.conn.commit()
       except(Exception,psycopg2.DatabaseError) as error:
           print(error)

    def get_entities(self):
        request = 'SELECT * FROM author'
        authors = list()
        try:
            self.cursor.execute(request)
            records = self.cursor.fetchall()
            for record in records:
                authors.append(Author(record[0] , record[1] , record[2] , record[3] , record[4]))
        except (Exception , psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return authors

    def update_entity(self , update_entity):

        pass

    def delete_entity(self , id):
        pass