import csv
import json
import random

CONFIG_PATH = 'config/address_mapping.csv'

class Address():
    def __init__(self):
        self.__classname__     = 'Address'
        self.mapping_file_path = CONFIG_PATH
        self.configurations = self.all_config()

    def get_address_row(self):
        index = random.randrange(0, len(self.configurations))
        return self.configurations[index]

    def all_config(self):
        configurations = []
        with open(self.mapping_file_path) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                configurations.append(rows)
        return configurations
