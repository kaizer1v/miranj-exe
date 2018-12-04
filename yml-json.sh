#!/bin/bash

python -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=2)' < events.yml > events.json