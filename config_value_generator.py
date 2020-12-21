import csv
import json

CONFIG_PATH = 'config/mappings.csv'

class ConfigValueGenerator():
    def __init__(self):
        self.__classname__     = 'ConfigValueGenerator'
        self.mapping_file_path = CONFIG_PATH
        self.configurations = self.all_config()

    def get_value(self, key, entity):
        values = []
        for rows in self.configurations:
            if (key == rows['VariableKey'] and entity == rows['Entity']):
                values.append(rows['VariableValue'])
        return values[0]

    def all_config(self):
        configurations = []
        with open(self.mapping_file_path) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                configurations.append(rows)
        return configurations
