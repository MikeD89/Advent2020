import os 

def get_dir() -> str: 
    return os.path.dirname(os.path.realpath(__file__))

def get_input_dir() -> str: 
    return os.path.realpath(os.path.join(get_dir(), "..\input"))

def load_data(data): 
    path = os.path.realpath(os.path.join(get_input_dir(), data))
    with open(path, 'r') as file:
        return file.read().splitlines()

def convert_string_data_to_ints(data): 
    return [int(numeric_string) for numeric_string in data]