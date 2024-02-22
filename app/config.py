from configparser import ConfigParser
import os

def load_config(filename='path', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return config

if __name__ == '__main__':
    path = os.getcwd()
    config = load_config(filename=path+r'\app\database.ini')
    print(config)