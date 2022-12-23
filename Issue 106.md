# Issue 106: maple (etc?) tab completion -- asking for a list of all completions gives a bad error message if maple isn't installed

Issue created by migration from https://trac.sagemath.org/ticket/106

Original creator: was

Original creation time: 2006-10-03 03:50:03

Assignee: was

This is especially a problem in the SAGE notebook.   Probably the same problem happens for Mathematica.


---

Comment by mabshoff created at 2007-08-23 12:13:36

This is still an issue with Sage 2.8.2-rc3:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2.rc3, Release Date: 2007-08-21                   |
| Type notebook() for the GUI, and license() for information.        |
sage: maple.
Building Maple command completion list (this takes
a few seconds only the first time you do it).
To force rebuild later, delete /home/mabshoff/.sage//maple_commandlist_cache.sobj.

------------------------------------------------------------
   File "<ipython console>", line 1
     maple.
           ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage: maple.
Building Maple command completion list (this takes
a few seconds only the first time you do it).
To force rebuild later, delete /home/mabshoff/.sage//maple_commandlist_cache.sobj.

------------------------------------------------------------
   File "<ipython console>", line 1
     maple.
           ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage:
```


An exception is raised you try execute a maple command without maple being installed:

```
sage: maple(1+1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/data/extcode/maple/user/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    556                 return cls(self, str(x))
    557             except TypeError, msg2:
--> 558                 raise TypeError, msg
    559
    560

<type 'exceptions.TypeError'>: Unable to start maple because the command 'maple -t' failed.
```


Cheers,

Michael

Cheers,

Michael


---

Attachment

fixes the problem


---

Comment by was created at 2007-09-06 18:45:27

Resolution: fixed


---

Comment by was created at 2007-09-06 18:45:27

fixed for sage-2.8.4
