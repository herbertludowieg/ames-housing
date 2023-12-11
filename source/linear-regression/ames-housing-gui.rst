GUI representation of description file
======================================

This is a simple script to create a GUI with the contents of the
descriptions for each of the columns in the housing data set for Ames,
Iowa. The raw file can be found `here <https://github.com/herbertludowieg/ml-projects/ames-housing/data/data_description.txt>`_.

This utilizes the
`Tab <https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#tabs>`_
and
`Accordion <https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#accordion>`_
GUI objects from the
`ipywidgets <https://ipywidgets.readthedocs.io/en/latest/index.html>`_
Python library. I made use of this library as the
``data_description.txt`` file had a very repetitive structure that I
could use to extract the relevant information. This GUI can help in
understanding the column values and how to process any missing values in
the data set, which is important in the `data
pre-processing <ames-housing-data.html#Data-Preprocessing>`__ step.

.. code:: ipython3

    import ipywidgets as widgets
    import numpy as np
    import os

.. code:: ipython3

    with open(os.path.join('_data', 'data_description.txt'), 'r') as fn:
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

Create GUI with a tab and accordion object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the dictionaries that I generated above I then made a set of
accordion objects that are arranged in alphabetical order separated into
tabs based on the first character in the key name (column name). This
way if you are wondering what is he meaning behind a set of values in a
particular column in the data set you can easily find it in this GUI.

.. code:: ipython3

    start = [key[0] for key in keys.keys()]
    tab = widgets.Tab()
    tab.children = [widgets.Accordion(children=[widgets.HTML(contents[key]) for key in sorted(keys.keys()) if key[0] == s],
                                      titles=tuple(['{}: {}'.format(key, keys[key]) for key in sorted(keys.keys()) if key[0] == s]))
                    for s in np.unique(start)]
    tab.titles = tuple(np.unique(start))
    tab

.. jupyter-execute:: ames-housing-gui.py
    :hide-code:

