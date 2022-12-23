# Issue 3408: [with spkg] Cython 0.9.8 released

Issue created by migration from https://trac.sagemath.org/ticket/3408

Original creator: robertwb

Original creation time: 2008-06-12 23:50:10

Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/


---

Attachment

This seems to break the future import in padic_generic_element.pyx


---

Comment by gfurnish created at 2008-06-13 02:54:49


```
from __future__ import with_statement
                                    ^
------------------------------------------------------------

/home/gfurnish/sage-3.0.2-symbolics/devel/sage-symbolics/sage/rings/padics/padic_generic_element.pyx:19:37: future feature with_statement is not defined
```

There also seem to be issues with having to move the future statement to before any includes.


---

Comment by mabshoff created at 2008-06-13 02:56:31

Please be more precise, i.e. error message, which branch, i.e. non-symbolics and so on.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-13 03:17:40

Gary: Notice that Robert attached a patch which you did not apply, so this issue is fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-13 03:28:17

I am getting slight rejects here:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 --dry-run < trac_3408-cython-0.9.8.patch 
patching file sage/ext/interactive_constructors_c.pyx
Hunk #1 FAILED at 24.
1 out of 2 hunks FAILED -- saving rejects to file sage/ext/interactive_constructors_c.pyx.rej
patching file sage/misc/cython.py
patching file sage/rings/padics/padic_generic_element.pyx
patching file sage/rings/padics/pow_computer_ext.pyx
```


Cheers,

Michael


---

Comment by gfurnish created at 2008-06-13 03:29:40

This seems to work for me except for the doctest rejects.


---

Comment by robertwb created at 2008-06-13 17:07:06

rebased


---

Attachment

OK, I've rebased the patch. Note that interactive_constructors_c is sorted now, so this won't bite us again.


---

Comment by mabshoff created at 2008-06-23 23:40:33

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-23 23:40:33

Resolution: fixed
