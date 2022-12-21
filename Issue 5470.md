# Issue 5470: Update Cython entry in Developer's Guide

Issue created by migration from Trac.

Original creator: cswiercz

Original creation time: 2009-03-10 19:54:07

Assignee: cswiercz

CC:  cswiercz

Keywords: documentation, cython

The current description for adding a new Cython module is outdated:

http://www.sagemath.org/doc/prog/node29.html

```
3. Create a .pyx file in the Sage library and add a listing for it to the variable
ext_modules in the file SAGE_ROOT/devel/sage/setup.py. For example, the file 
SAGE_ROOT/devel/sage/sage/graphs/chrompoly.pyx has lines

    Extension('sage.graphs.chrompoly',
              ['sage/graphs/chrompoly.pyx']
              ), \

in setup.py. Also, the module - in this example sage.graphs.chrompoly - needs to be 
added to the packages list in setup.py . Then type sage -b to build Sage with the new 
code.
```


This documentation needs to account for the separate `module_list.py` file.


---

Comment by mabshoff created at 2009-03-10 20:55:19

Yes, it is under version control:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.rc2/devel/sage$ hg log doc/en/developer/coding_in_other.rst
changeset:   11689:d83194742483
user:        Mike Hansen <mhansen`@`gmail.com>
date:        Tue Feb 24 09:13:12 2009 -0800
summary:     Added the documentation to the main repository.
```


Cheers,

Michael


---

Attachment


---

Comment by cswiercz created at 2009-03-10 21:39:55

D'oh! I must have been looking at another screen or something.

The patch is attached an is ready for review.


---

Comment by robertwb created at 2009-03-17 00:53:24

Mostly looks good. The only complaint I have is about step (2)


```
   #. Then, add the module name to the ``packages`` list in the file
      ``SAGE_ROOT/devel/sage/setup.py``.
```


one only does this if one is making an new package (directory).


---

Attachment

Apply in the following order:

`sage-5470.patch`

`sage-5470-part2.patch`


---

Comment by mabshoff created at 2009-04-01 01:15:21

Resolution: fixed


---

Comment by mabshoff created at 2009-04-01 01:15:21

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael
