from db.run_sql import run_sql

from models.staff import Staff
from models.animals import Animal 


def save(staff):

    sql = "INSERT INTO staff (name,start_date,department,performance_rating) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.department, staff.performance_rating]
    results = run_sql(sql,values)
    id = results[0]['id']
    staff.id = id 
    return staff

def select_all():
    all_staff = []

    sql = "SELECT * FROM staff"
    results =run_sql(sql)

    for row in results:
        staff = Staff(row['name'],row['start_date'],row['department'],row['performance_rating'],row['id'])
        staff.append(all_staff)
    return all_staff

def select(id):
    staff = None 
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        staff = Staff(result['name'],result['start_date'],result['department'],result['performance_rating'],result['id'])
    return staff

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)

def delete_id(id):
    
    sql = "DELETE FROM staff WHERE id = %s"
    values =[id]
    run_sql(sql,values)

def update(staff):
    sql = "UPDATE staff SET (name,start_date,department,performance_rating) = (%s, %s, %s, %s) WHERE id is %s"
    values = [staff.name, staff.start_date,staff.department,staff.performance_rating,staff.id]
    run_sql(sql,values)

def animals(staff):
    animals = []
    sql = "SELECT * FROM animals WHERE staff_id = %s"
    values = [staff.id]
    results =run_sql(sql,values)

    for row in results:
        animal = Animal(row['name'],staff,row['type'],row['species'],row['id'])
        animals.append(animal)
    return animals
