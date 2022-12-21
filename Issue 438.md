# Issue 438: cython -v prints standard help text

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-18 17:52:27

Assignee: was

Instead of some version number I get

[mabshoff`@`m940 sage-2.8.1]$ cython -v
Cython (http://cython.org) is a compiler for code written in the
Cython language.  Cython is based on Pyrex by Greg Ewing.

Usage: cython [options] sourcefile.pyx ...

Options:
  -v, --version                  Display version number of cython compiler
  -l, --create-listing           Write error messages to a listing file
  -I, --include-dir <directory>  Search for include files in named directory
                                 (multiply include directories are allowed).
  -o, --output-file <filename>   Specify name of generated C file
  -p, --embed-positions          If specified, the positions in Cython files of each
                                 function definition is embedded in its docstring.
  -z, --pre-import <module>      If specified, assume undeclared names in this
                                 module. Emulates the behavior of putting
                                 "from <module> import *" at the top of the file.


---

Comment by mabshoff created at 2007-12-29 21:12:47

I will report this to the Cython dev mailing list.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 01:32:33

I never reported this to the cython-devel list, but somebody else did this week and it ought to be fixed soon then.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 01:32:33

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-02-23 06:36:36

Resolution: fixed
