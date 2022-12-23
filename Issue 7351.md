# Issue 7351: optimize import of singular.py

Issue created by migration from https://trac.sagemath.org/ticket/7351

Original creator: was

Original creation time: 2009-10-29 22:56:33

Assignee: was

CC:  robertwb


```
I'm using sage -startuptime.

The singular interface also looks like a *major* culprit:

              sage.interfaces.singular: 0.329 (sage.rings.ideal)
               sage.structure.sequence: 0.000 (sage.interfaces.singular)

Looking, I see that a *horrendously* time consuming function called 
"generate_docstring_dictionary()" is called whenever the file sage/interfaces/singular.py is imported.  This is completely pointless, and shouldn't happen until somebody actually tries to use the singular interface.  A few lines of code would immediately reduce the startup time of Sage by nearly a half second there. 

```



---

Attachment

this fixes the issue for me


---

Comment by malb created at 2009-11-18 13:01:53

Changing status from new to needs_review.


---

Comment by robertwb created at 2009-11-20 03:49:38

Nice. Thanks!


---

Comment by robertwb created at 2009-11-20 03:49:38

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 05:17:46

Resolution: fixed
