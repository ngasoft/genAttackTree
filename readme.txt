Description:
============
- main.py: the main script to runs
- treelib-mini: the template library for the mini example.
- treelib-full: the template library for the full example.
- treelib-sd: the template library for the streetdrone example.


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

The last two lines in the main script main.py indicate which example is used. To run an example, please comment out the other. In particular, to run the mini example, the last line must be commented and the line before that is uncommented. To run the full example, the last line is uncommented while the line before that is uncomment. Then, to execute the script, use run the following command from the command lines

python3 main.py

The output tree for the mini example is output-mini.xml, for the full example is output-full.xml. They can be imported in adtool2 for a graphical representation.
