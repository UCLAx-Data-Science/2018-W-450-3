import yaml

def get_credentials():
    with open("data/credentials.yml", 'r') as stream:
        credentials = yaml.load(stream)

    return credentials