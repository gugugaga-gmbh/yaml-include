#!/usr/bin/python

import yaml
import argparse
from yamlinclude import YamlIncludeConstructor

# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description='')
parser.add_argument('input', metavar='i', type=str, help='Path to yaml file')
parser.add_argument('output', metavar='o', type=str, help='Path to generated yaml file')
args = parser.parse_args()

YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir='/app')

with open(args.input) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

with open(args.output, 'w') as file:
    yaml.dump(data, file, sort_keys=False)
