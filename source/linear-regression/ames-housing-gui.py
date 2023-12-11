#!/usr/bin/env python
import ipywidgets as widgets
import numpy as np
import os

filepath = os.path.join('source', 'linear-regression', 
                       '_data', 'data_description.txt') 
with open(filepath, 'r') as fn:
    lines = fn.readlines()
i = 0
keys = {}
contents = {}
while i < len(lines):
    line = lines[i]
    if ':' in line and not line.startswith('  '):
        key, descrip = line.split(':')
        keys[key] = descrip
        if lines[i+2].startswith('  '):
            i += 2
            contents[key] = []
            while lines[i].strip():
                contents[key].append(lines[i].strip())
                i += 1
                if i >= len(lines): break
            contents[key] = '<br>'.join(contents[key])
        else:
            contents[key] = 'No categories'
    i += 1

start = [key[0] for key in keys.keys()]
tab = widgets.Tab()
tab.children = [widgets.Accordion(children=[widgets.HTML(contents[key]) for key in sorted(keys.keys()) if key[0] == s],
                                  titles=tuple(['{}: {}'.format(key, keys[key]) for key in sorted(keys.keys()) if key[0] == s]))
                for s in np.unique(start)]
tab.titles = tuple(np.unique(start))
tab
