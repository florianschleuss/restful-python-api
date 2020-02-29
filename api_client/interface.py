import os
import sys

import client

menu_actions = {}
api = client.api_client('http://localhost:5000/api/v1') #Client referenziert RESTful Web Service per URI
api.auth('demo', 'demo')

def main_menu():
    os.system('clear')

    print("Welcome to API CLI,\n")
    print("please choose the function you want to execute:")
    print("1. Post Request")
    print("2. Patch Request")
    print("3. Get Request")
    print("4. Delete Request")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)


def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1: Post
def post_menu():
    print("Post a new element !\n")
    print("11. Post new customer")
    menu_suffix()
    return


# Menu 2: Patch
def patch_menu():
    print("Patch existing element !\n")
    print("21. Patch Customer")
    menu_suffix()
    return


# Menu 3: Get
def get_menu():
    print("Get existing element !\n")
    print("31. Get customer")
    print("32. Get all customers")
    print("33. Get all locations")
    menu_suffix()
    return


# Menu 4: Delete
def delete_menu():
    print("Delete existing element !\n")
    print("41. Delete customer")
    menu_suffix()
    return


# Menu Suffix
def menu_suffix():
    print("\n9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# Under maintenance
def under_maintenance():
    print("This function is under maintenance. Thanks for your understanding! \n")
    menu_suffix()
    return


def post_customer():
    print("Please insert customer information:\n")
    customer = {}
    print("Customer name:")
    customer['name'] = input(" >>  ")
    print("City:")    
    customer['city'] = input(" >>  ")
    print("Manager:")    
    customer['manager'] = input(" >>  ")
    print("Enterprise value in Mrd $:")    
    customer['value'] = input(" >>  ")

    api.post('/customer/{}'.format(customer['name'].lower().replace(' ', '_')), customer)

    print("Customer added!")
    menu_suffix()
    return


def patch_customer():
    print("Please insert customer information:\n")
    customer = {}
    print("Customer name:")    
    customer['name'] = input(" >>  ")
    print("City:")    
    customer['city'] = input(" >>  ")
    print("Manager:")    
    customer['manager'] = input(" >>  ")
    print("Enterprise value in Mrd $:")    
    customer['value'] = input(" >>  ")

    print("Customer patched!")
    menu_suffix()
    return

def get_customer():
    print("Please insert customer information:\n")
    customer = {}
    print("Customer name:")    
    customer['name'] = input(" >>  ")

    print(api.get('/customer/{}'.format(customer['name'].lower().replace(' ', '_'))).text)

    menu_suffix()
    return

def get_all_customers():
    print("This are all customers:\n")

    print(api.get('/customers').text)

    menu_suffix()
    return

def get_all_locations():
    print("This are all locations:\n")

    print(api.get('/locations').text)

    menu_suffix()
    return

def del_customer():
    print("Please insert customer information:\n")
    customer = {}
    print("Customer name:")    
    customer['name'] = input(" >>  ")

    print(api.delete('/customer/{}'.format(customer['name'].lower().replace(' ', '_'))).text)

    menu_suffix()
    return

menu_actions = {
    'main_menu': main_menu,
    '1': post_menu,
    '11': post_customer,
    '2': patch_menu,
    '21': patch_customer,
    '3': get_menu,
    '31': get_customer,
    '32': get_all_customers,
    '33': get_all_locations,
    '4': delete_menu,
    '41': del_customer,
    '9': back,
    '0': exit,
}

if __name__ == "__main__":
    # Launch main menu
    main_menu()