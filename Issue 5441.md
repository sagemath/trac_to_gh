# Issue 5441: preparser_ipython edit

Issue created by migration from https://trac.sagemath.org/ticket/5441

Original creator: kohel

Original creation time: 2009-03-05 16:34:20

Assignee: cwitty

In the function prepare_ipython, in the block:
 
 if interface_name == 'magma' and magma_colon_equals:

I suggest changing:

line = line.replace(':=','=').replace('=',':=')

to

line = line.replace('=',':=').replace('::=',':=').replace(':=:=','=')

in sage/misc/preparser_ipython.py.

This will almost never be used (except by me), 
but in principal allows one to write x == y to 
get a magma relation (x = y) while preserving 
the hack (= -> :=). 

Also, in the block:

if interface_name in ['gap', 'magma', 'kash', 'singular']:

I also suggest deleting the lines:

if not line.endswith(';'):                          
    line += ';'

since the call to interface.eval() should handle this.
