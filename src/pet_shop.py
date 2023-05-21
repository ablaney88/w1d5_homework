# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold
    
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    
    
def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    return found_pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(list_of_pets, pet):
    list_of_pets["pets"].append(pet)
    return len(list_of_pets["pets"])

def get_customer_cash(customer_list):
    return customer_list["cash"]

def remove_customer_cash(customer_cash, amount):
    customer_cash["cash"] -= amount

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customers, new_pet):
    customer_cash = customers["cash"]
    pet_price = new_pet["price"]

    if customer_cash >= pet_price:
        return True
    else:
        return False
    
# def sell_pet_to_customer(pet_shop, pet, customer):
    

#     price_of_pet = pet["price"]

#     # customer["pets"].append(pet)
#     add_pet_to_customer(customer, pet)

#     # pet_shop["admin"]["pets_sold"] += 1
#     increase_pets_sold(pet_shop, 1)

#     # customer["cash"] -= pet["price"]
#     remove_customer_cash(customer, price_of_pet)

#     # pet_shop["admin"]["total_cash"] += pet["price"]
#     add_or_remove_cash(pet_shop, price_of_pet)


def sell_pet_to_customer(pet_shop, pet, customer):        
    if find_pet_by_name(pet_shop, pet) and customer_can_afford_pet(customer, pet):

        price_of_pet = pet["price"]

        customer["pets"].append(pet)
        # add_pet_to_customer(customer, pet)

        pet_shop["admin"]["pets_sold"] += len(customer["pets"])
        # increase_pets_sold(pet_shop, get_customer_pet_count(customer))

        # customer["cash"] -= pet["price"]
        remove_customer_cash(customer, price_of_pet)

        # pet_shop["admin"]["total_cash"] += pet["price"]
        add_or_remove_cash(pet_shop, price_of_pet)

    


