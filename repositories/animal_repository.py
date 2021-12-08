from db.run_sql import run_sql
from models.staff import Staff
from models.animals import Animal


import repositories.staff_repository as staff_repository



def save(animal):

    sql = "INSERT INTO animals (name,handler_id,type,species) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.handler.id,animal.type, animal.species]
    results = run_sql(sql,values)
    id = results[0]['id']
    animal.id = id 
    return animal



def select_all():
    all_animals = []

    sql = "SELECT * FROM animals"
    results =run_sql(sql)

    for row in results:
        handler = staff_repository.select(row['handler_id'])
       
        animal = Animal(row['name'],handler,row['type'],row['species'],row['id'])
        all_animals.append(animal)
        
        
    return all_animals

def select(id):
    
    animal = None 
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
      handler= staff_repository.select(result['handler_id'])
      animal = Animal(result['name'],handler,result['type'],result['species'],result['id'])
    return animal

def delete_all():
    sql ="DELETE FROM animals"
    run_sql(sql)

def delete(id):
  sql = "DELETE FROM animal WHERE id = %s"
  values =[id]
  run_sql(sql,values)

def update(animal):
    sql = "UPDATE animals SET (name, handler_id, type, species) = (%s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.handler.id, animal.type,animal.species,animal.id]
    run_sql(sql,values)

