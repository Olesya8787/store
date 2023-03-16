# Start -menu 
# 1) Registration
# 2) Auth
# 3) Product catalog
# 4) Buy product
# 5) Money
# 6) Exit
####################################################



def registration(user_name , password, money ) :
    registered_user.append({
        "user_name" : user_name,
        "password" : password,
        "money" : money 
    })
    return len(registered_user) - 1
 
def auth( user_name, password, registered_user) :
    for index in range(len(registered_user)):
        item = registered_user[index] 
      
        if registered_user[index]["user_name"]==user_name and registered_user[index]["password"]==password :
            print("OK")
            return index
    return -1
        
def show_products_catalog(list_of_products_catalog) :
    for products_catalog_item in list_of_products_catalog :
        print(products_catalog_item)       

def money_user (money, registered_user) :
    if money_user != 0:
        print("You can continue shopping") 
    else :
        print("You pocket is empty")

def buy_products (products_catalog_value) :
    product_choose = True
    exit_symbol = False

    for index in range(len(products_catalog_value)):
        print(index , ": ", products_catalog_value[index])
    
    while product_choose :
        product_index = input('Choose a product (exit = "x"): ') 
        if product_index.lower()== "x" :
            product_choose = False
        else:
            print(products_catalog_value[int(product_index)]) 
            price = products_catalog[int(product_index)]["price"] 
            user_money = registered_user[user_index]["money"]
            money_left =  int(user_money) - int(price)
            if money_left >= 0 :
                print("Congratulations on your purchase")
                registered_user[user_index]["money"] = money_left
            else :
                print("You don't have enough money to buy")
                print(registered_user[user_index]["money"]) 

def is_exit() :
     exit_symbol= input("Do you want to leave the store ? y/n : ")
     return exit_symbol.lower()                
              


user_index = -1

products_catalog = [
    {
        "label" : "Lavazza",
        "product" : "coffee",
        "price" : 500
    },
    {
        "label" : "Ambassador",
        "product" : "coffee",
        "price" : 600 
    },
    {
        "label" : "Tchibo",
        "product" : "coffee",
        "price" : 400
    },
    {
        "label" : "Raffaello",
        "product" : "candy",
        "price" : 300 
    },
    {
        "label" : "Ritter sport",
        "product" : "candy",
        "price" : 300 
    },
    {
        "label" : "Lind Lindor",
        "product" : "candy",
        "price" : 400 
    }
]

registered_user  = [
    {
        "user_name" : "Milan",
        "password" : "123456",
        "money" : "2000"
    },
    {
        "user_name" : "Katrin",
        "password" : "98765",
        "money" : "1500"
    },
    {
        "user_name" : "Alex",
        "password" : "734567",
        "money" : "3000"
    },
]


is_running = True

is_has_account = False

while is_running :
    choose_action = input("""
        1) Registration
        2) Auth
        3) Product catalog
        4) Buy product
        5) Exit
    Answer : """.lower()    
    ) 


    if choose_action == "1" :
            if user_index == -1:
                user_name = input("Enter your name : " )
                password = input("Enter your password  : ")
                money = input("How much money do you have ?  : ")
                user_index = registration(user_name , password, money )  

    elif choose_action == "2"  :
            if user_index == -1:
                user_name = input("Enter your name : " )
                password = input("Enter your password  : ")
                user_index = auth( user_name, password,registered_user)

    elif choose_action == "3" :          
        show_products_catalog(products_catalog) 

    elif choose_action == "4" :
        if user_index != -1 : 
            buy_products(products_catalog) 
        
    elif choose_action == "5" :
        exit_symbol = is_exit()
        if exit_symbol == "y" :
            
            is_running = False  
        


  
    


   



        

 


     