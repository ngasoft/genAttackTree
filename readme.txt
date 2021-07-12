Description:
============
- mainADT.py: the main script to runs
- treelib-sd: the template library for the streetdrone example.
- model-sd.inp: the input system model for the streetdrone example


Dependencies:
=============
  Mandatory:
  - Python 3 (https://www.python.org)
  - antlr4-python3-runtime (https://pypi.org/project/antlr4-python3-runtime/)
  Optional
  - Adtool2 (https://satoss.uni.lu/members/piotr/adtool/)

Installation:
=============
  - Install all required depenencies:
    + antlr-python3-runtime can be installed using pip:
      pip install antlr4-python3-runtime
  - Adtool2 is optional, it can be used to create attack tree templates and to view the output attack tree.

Usage:
======

To execute the script, use run the following command from the command lines

python3 mainADT.py

The output trees for the streetdrone example are output-mini-COMPONENT.xml for each COMPONENT from the input model. They can be imported in adtool2 for a graphical representation.
