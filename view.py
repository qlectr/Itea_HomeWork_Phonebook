"""
programmer: Dima
--
creation date: 2020-10-26
change date: 2020-11-15
"""

import controller

while True:
    try:
        controller.show_menu()
        input_action = controller.input_action()

        if input_action in ('A'):
            contact_name = controller.input_contact_name()
            contact_attribute = controller.input_contact_attribute()
        elif input_action in ('C','D'):
            contact_name = controller.input_contact_name()
            contact_attribute = ''
        else:
            contact_name = ''
            contact_attribute = ''
     
        print(controller.controller.get(input_action).get('help_message'))
        controller.controller.get(input_action).get('function_name')(contact_name = contact_name,
                                                                     contact_attribute = contact_attribute,)
    except KeyError as e:
        print(e)
