# Issue 4377: Building the Sage library with parallel make is broken on OSX 10.4

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-28 15:03:40

Assignee: mabshoff

CC:  justin

exporting MAKE=make -j2 leads to

```
Traceback (most recent call last):
  File "setup.py", line 1545, in <module>
    cython(deps, ext_modules)
  File "setup.py", line 1311, in cython
    execute_list_of_commands(command_list)
  File "setup.py", line 1403, in execute_list_of_commands
    n = 2*number_of_cpus()
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
sage: There was an error installing modified sage library code.
```

on OSX 10.4.

This is caused by #3765.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 15:25:27

ok, the issue is simple enough and an extra "\n" in the output:

```
>>> import os
>>> os.popen2("sysctl -n hw.ncpu")[1].read()
'2\n'
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 15:29:06

Ok, the above wasn't the issue. Strange that number_of_cpus() returns None.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-10-28 15:58:04

The patch fixes the issue. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 16:19:40

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-28 16:19:40

Resolution: fixed
