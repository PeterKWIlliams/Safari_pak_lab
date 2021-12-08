import pdb 
from models.animals import Animal 
from models.staff import Staff

import repositories.staff_repository as staff_repository 
import repositories.animal_repository as animal_repository


staff_repository.delete_all()
animal_repository.delete_all()


staff1 = Staff("Jack Cheeseman", "01.02.2021","Plumbing",1)
staff_repository.save(staff1)

staff2 = Staff("Gary Polle","02.02.2021","herbivores",3)
staff_repository.save(staff2)

staff3 =Staff("John Start","03.02.2021","carnivores",5)
staff_repository.save(staff3)

animal1 = Animal("Terry",staff1,"carnivore","Tiger")
animal_repository.save(animal1)

animal2 =Animal("Larry",staff2,"herbivore","Llama")
animal_repository.save(animal2)


staff_repository.select_all()









