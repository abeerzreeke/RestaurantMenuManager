from menu_manager import MenuManager


def load_manager():
        
    manager = MenuManager()
    return manager
    
def show_user_menu():

    
    print('     ---------WELCOME TO OUR PROGRAM MENU---------')
    print('     PLEASE CHOOSE ONE OPTION')
    print('  (A)   ADD AN ITEM  ')
    print('  (D)   DELETE AN ITEM  ')
    print('  (V)   VIEW THE MENU  ')
    print('  (X)   EXIT ')

    valid_flag = False
    while not valid_flag:

        user_choose = input(' YOUR CHOOSE :  ')
    
        if user_choose == 'a' or user_choose == 'A':
            add_item_to_menu()

        elif user_choose == 'd' or user_choose == 'D':
            remove_item_from_menu()

        elif user_choose == 'v' or user_choose == 'V':
            show_restaurant_menu()
            
        elif user_choose == 'x' or user_choose == 'X':
            print('ALL YOUR CHANGE WAS SAVED BYE BYE')
            valid_flag = True   
            exit()
        else:
            print('YOUR CHOOSE IS NOT EXIST')

def add_item_to_menu():

    manger = load_manager()
    name_item = input('WRITE THE NAME OF THE ITEM YOU WANT TO ADD: ')
    price_item = int(input('WRITE THE PRICE OF THE NEW ITEM: '))
    manger.add_item(name_item,price_item)
    manger.save_to_file()
    print(f'THE ITEM {name_item} WAS ADDED SUCCESSFLLY')
    

def remove_item_from_menu():

    manger = load_manager()
    name_item = input('WRITE THE NAME OF THE ITEM YOU WANT TO DELETE: ')
    res = manger.remove_item(name_item)
    manger.save_to_file()
    if res:
        print(f'YOUR ITEM {name_item} WAS DELETED SUCCESSFULLY')
    else:
        print(f'DID NOT SUCCEED TO DELETE THIS ITEM {name_item}')

def show_restaurant_menu():

    manger = load_manager()
    print(manger.save_to_file())


show_user_menu()


























