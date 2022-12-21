# Issue 3343: arguments, documentation to ln function

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-05-31 21:46:29

Assignee: somebody

Keywords: ln, calculus

First, ln should only take 1 argument.  As it is, it accepts more than one, and just ignores all of the extra ones:


```
sage: ln(6,2)
log(6)
sage: ln(12,-2,0,0,3,4,5)
log(12)
```


Second, the documentation for ln (hitting 'ln?') gives the documentation for the class Function_log, and hence includes things like this:

```
sage: log(1024, 2) # the following is ugly (for now)
log(1024)/log(2)
sage: log(10, 4)
log(10)/log(4)
```


The attached patch defines ln as a function accepting only one argument, and with its own documentation.



---

Attachment


---

Comment by gfurnish created at 2008-06-10 05:31:12

This is a good idea.


---

Comment by mabshoff created at 2008-06-10 05:51:51

Resolution: fixed


---

Comment by mabshoff created at 2008-06-10 05:51:51

Merged in Sage 3.0.3.alpha2
