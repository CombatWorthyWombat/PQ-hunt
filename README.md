# cliFX_module
a small module for making CLI beautifying a little easier

added verbose_print function

command syntax as follows:

`print(c.ansi197("red text"))`

or, for named colours in the dictionary:

`print(c.red("red text"))`


supports all 256 ansi escape codes, does not support:

  - RGB
  - YPbPr
  - CYM
  - YIQ
  - or any other colour systems

might add support for these in the future (or if people ask)
