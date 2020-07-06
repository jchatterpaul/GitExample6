import yaml
from yaml import load, load_all

stream = open('sample1.yaml','r')

# SafeLoader for yaml file unsure of
# load_all if multi document in yaml
documents = load_all(stream, Loader=yaml.FullLoader)

print(type(documents))

for doc in documents:
    print(type(doc))

    

