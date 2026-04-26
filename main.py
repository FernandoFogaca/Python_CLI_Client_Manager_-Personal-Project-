
import json
import os

clients = []

def add_client():
    name = input("Enter a client name: ")
    clients.append(name)
    save_clients()
    print(f'Client {name} added!')


def list_clients():
    if len(clients)==0:
        print("No clients yet")
    else:
        for i,client in enumerate(clients):
            print(f"{i +1}. {client}")
        input("\nPress Enter to continue...")



def remove_client():
    list_clients()
    index = input("Select client number to remove")

    if index.isdigit():
        index = int(index)

        if 0 <index <= len(clients):
            removed = clients.pop(index - 1)
            save_clients()
            print(f"{removed} removed!")
        else:
            print("Invalid number")
    else:
        print("Please enter a valid number")

def save_clients():
    with open("clients.json", "w") as file:
        json.dump(clients, file)

def load_clients():
    global clients 
    try: 
        with open("clients.json", "r") as file:
            clients=json.load(file)


    except:


        clients=[]


def clear_screen():
    os.system('clear')

def menu():
    
    while True:
        clear_screen()
        print("\n  Client Manager ")
        print("1. Add client ")
        print("2. List Clients ")
        print("3. Remove client ")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_client()
        elif option == "2":
            list_clients()
        elif option == "3":
            remove_client()
        elif option == "4":
            print("Cheerio")
            break
        else:
            print("Invalid option")

load_clients()
menu()

