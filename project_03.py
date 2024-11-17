"""Projecto de lista telefonica"""
# EJEMPLO DE .POP
# mi_lista = [10, 20, 30, 40]
# elemento = mi_lista.pop(1)  # Elimina y retorna el elemento en índice 1 (20)
# print(mi_lista)  # Resultado: [10, 30, 40]
# print(elemento)  # Resultado: 20

import json


def add_person():
    """Funcion para registrar los contactos"""
    name = input("Name: ").capitalize()
    age = input("Age: ").capitalize()
    email = input("Email: ")

    person = {
        "name": name,
        "age": age,
        "email": email
    }
    return person


def display_people(people):
    """Funcion que nos da el listado de los contactos"""
    for i, person in enumerate(people):
        print(i+1, "-", person["name"], "|",
              person["age"], "|", person["email"])


def delete_contact(people):
    """Funcion para enlistar y escoger que contacto eliminar"""
    display_people(people)
    while True:
        number = input("Choice a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number.")

    people.pop(number-1)
    print("Contact deleted!")


def search(people):
    """Funcion para realizar busqueda cercana"""
    search_name = input("Search for a name: ").capitalize()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.capitalize():
            results.append(person)
    display_people(results)


print()
print("Hi, Welcome to the Contact Managament System.")
print()

with open("Projectos\contacts.json", "r") as f:
    people = json.load(f)["contacts"]

# people = []

while True:
    print("Number of contacts is:", len(people))
    choice = input(
        "You can 'Add','Delete' or 'Search' and use 'Q' or 'Quit' for exit: ").capitalize()

    if choice == "Add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif choice == "Delete":
        delete_contact(people)
    elif choice == "Search":
        search(people)
    elif choice == "Quit" or "Q":
        break
    else:
        print("Invalid choice")

with open("Tipos\Projectos\contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
