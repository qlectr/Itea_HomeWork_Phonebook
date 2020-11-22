import config
import os
from io_package import pickle_
from io_package import json_
from io_package import csv_

MESSAGE_CONTACT_NOT_EXISTS = 'Contact does not exist!'
MESSAGE_CONTACT_EXISTS = 'Contact already exists!'

config.create_config_if_not_exists()

file_format, file_name  = config.read_config().upper() , config.read_config_file_name()

if file_format  == 'JSON':
    dumper = json_.json_dumper(file_name)
elif file_format  == 'PICKLE':
    dumper = pickle_.pickle_dumper(file_name)
elif file_format  == 'CSV':
    dumper = csv_.csv_dumper(file_name)


def is_name_exists_in_phonebook(contact_name, phonebook):
    """Функция проверки наличия имени в справочнике"""
    if contact_name in phonebook:
        return contact_name

def update_config(**kwargs):
    """Функция обновления формата файла справочника"""
    config.update_config()
 

class Phonebook:
    def __init__(self, file_name):
        """Загрузка ранее сохраненного справочника или создание пустого"""
        if os.path.exists(file_name):
            self.phonebook = dumper.load()
        else:
            self.phonebook = {}

    def clear_phonebook(self,**kwargs):        
        """функция очистки справочника"""
        self.phonebook.clear()


    def delete_contact(self, contact_name, **kwargs):
        """функция удаления записи из справочника"""
        if is_name_exists_in_phonebook(contact_name, self.phonebook):
            del self.phonebook[contact_name]
        else:
            raise KeyError(MESSAGE_CONTACT_NOT_EXISTS)

    def create_contact(self, contact_name, **kwargs):
        """функция создания контакта в справочнике"""
        if is_name_exists_in_phonebook(contact_name, self.phonebook):
            raise KeyError(MESSAGE_CONTACT_EXISTS)
        else:
            self.phonebook[contact_name] = {}

    def add_or_update_contact_attributes(self, contact_name, contact_attribute, **kwargs):
        """функция создания или обновления атрибутов контакта"""
        if is_name_exists_in_phonebook(contact_name, self.phonebook): 
            for key, value in contact_attribute.items():
                new_attribute = {key: value}
                old_attributes = self.phonebook.get(contact_name)
                all_attributes = {**old_attributes, **new_attribute}
                self.phonebook[contact_name] = all_attributes
        else:
            raise KeyError(MESSAGE_CONTACT_NOT_EXISTS)

    def phonebook_items(self, **kwargs):
        """функция отображения всего содержимого справочника"""
        return self.phonebook.items()

    def save_phonebook(self, **kwargs):
        """функция сохранения справочника"""
        dumper.save(phonebook=self.phonebook)
