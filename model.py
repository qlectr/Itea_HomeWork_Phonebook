import config
import os
from IO_package import pickle_
from IO_package import json_
from IO_package import csv_

MESSAGE_CONTACT_NOT_EXISTS = 'Contact does not exist!'
MESSAGE_CONTACT_EXISTS = 'Contact already exists!'
MESSAGE_DONE = 'Done!'

config.create_config_if_not_exists()

file_format, file_name  = config.read_config().upper() , config.read_config_file_name()

#Блок определения формата файла, с которым мы будем работать в рамках данной сессии:
if file_format  == 'JSON':
    load, save = json_.load_json, json_.save_json
elif file_format  == 'PICKLE':
    load, save = pickle_.load_pickle, pickle_.save_pickle
elif file_format  == 'CSV':
    load, save = csv_.load_csv, csv_.save_csv

#Загрузка ранее сохраненного справочника или создание нового:
if os.path.exists(file_name):
    phonebook = load(filename = file_name)
else:
    phonebook = {}


def is_name_exists_in_phonebook(contact_name):
    """Функция проверки наличия имени в справочнике"""
    if contact_name in phonebook:
        return contact_name

def update_config( **kwargs):
    """Функция обновления формата файла справочника"""
    config.update_config()

class Phonebook:
    def __init__(self):
        pass

    def clear_phonebook(**kwargs):        
        """функция очистки справочника"""
        phonebook.clear()
        print(MESSAGE_DONE)

    def delete_contact(contact_name, **kwargs):
        """функция удаления записи из справочника"""
        if is_name_exists_in_phonebook(contact_name):
            del phonebook[contact_name]
            print(MESSAGE_DONE)
        else:
            raise KeyError(MESSAGE_CONTACT_NOT_EXISTS)

    def create_contact(contact_name, **kwargs):
        """функция создания контакта в справочнике"""
        if is_name_exists_in_phonebook(contact_name):
            KeyError(MESSAGE_CONTACT_EXISTS)
        else:
            phonebook[contact_name] = {}
            print(MESSAGE_DONE)

    def add_or_update_contact_attributes(contact_name, contact_attribute, **kwargs):
        """функция создания или обновления атрибутов контакта"""
        if is_name_exists_in_phonebook(contact_name): 
            for key, value in contact_attribute.items():
                new_attribute = {key: value}
                old_attributes = phonebook.get(contact_name)
                all_attributes = {**old_attributes, **new_attribute }
                phonebook[contact_name] = all_attributes
                print(MESSAGE_DONE)
        else:
            raise KeyError(MESSAGE_CONTACT_NOT_EXISTS)

    def view_phonebook(**kwargs):
        """функция отображения всего содержимого справочника"""
        print(phonebook.items())

    def save_phonebook(**kwargs):
        """функция сохранения справочника"""
        save(phonebook = phonebook,filename = file_name)
        print(MESSAGE_DONE)
