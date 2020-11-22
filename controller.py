import model

MESSAGE_MENU_ITEM_NOT_EXISTS = "The menu item does not exist. Try again!"

phonebook = model.Phonebook(model.file_name)

def view_phonebook_items(**kwargs):
    print(phonebook.phonebook_items())

controller = {}

def show_menu():
    """функция думенстрации меню"""
    print('Menu:')
    for x in controller:
        print(x,' - ',controller[x].get('description'))


def input_action():
    """функция обработки ввода пункта меню пользователем"""
    action = input("Make your choice:\n").upper() .strip(' ')  
    if action in controller:
        return action
    else:
        raise KeyError(MESSAGE_MENU_ITEM_NOT_EXISTS)


def input_contact_name():
    """функция ввода имени"""
    return input("Name: ")


def input_contact_attribute():
    """функция ввода атрибута контакта"""
    key = input("Attribute: ")
    value = input("Value: ")
    return {key: value}


def input_login_name(**kwargs):
    """функция авторизации в справочнике"""
    return input("Dima or Vasa: ") 


def quit_app(**kwargs):
    """функция выхода из программы"""
    quit()


def view_config_file_format(**kwargs):
    print(model.file_format)




def add_controller_method(key, description, function_name, help_message):
    """функция наполнения справочника-контроллера"""
    description_dict = {
        'description': description,
        'function_name': function_name,
        'help_message': help_message,
    }
    controller[key] = description_dict

add_controller_method(  "C",
                        "Create contact",
                        phonebook.create_contact,
                        "Enter contact name",
                    )

add_controller_method(  "A",
                        "Add or update contact attribute",
                        phonebook.add_or_update_contact_attributes,
                        "Enter contact attribute",
                    )

add_controller_method(  "D",
                        "Delete contact",
                        phonebook.delete_contact,
                        "Enter contact name",
                    )

add_controller_method(  "V",
                        "View phonebook",
                        view_phonebook_items,
                        "",
                    )

add_controller_method(  "CP",
                        "Clear phonebook",
                        phonebook.clear_phonebook,
                        "",
                    )                   

add_controller_method(  "VC",
                        "View config",
                        view_config_file_format,
                        "Actual IO format:",
                    ) 

add_controller_method(  "UC",
                        "Update config",
                        model.update_config,
                        "Input pickle, json or csv",
                    )      

add_controller_method(  "S",
                        "Save phonebook",
                        phonebook.save_phonebook,
                        "",
                    )

add_controller_method(  "L",
                        "Login",
                        input_login_name,
                        "Enter user name",
                    )

add_controller_method(  "Q",
                        "Quit",
                        quit_app,
                        "Good Buy!",
                    )