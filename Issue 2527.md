# Issue 2527: get doctests for congroup.py and congroup_element.py up to 100%

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-15 02:40:26

Assignee: was

Start:

```
teragon:modular was$ sage -coverage congroup.py congroup_element.py 
SCORE congroup.py: 20% (14 of 68)
SCORE congroup_element.py: 0% (0 of 10)
```




---

Comment by AlexGhitza created at 2008-04-23 02:36:19

Changing component from number theory to modular forms.


---

Comment by AlexGhitza created at 2008-04-23 02:36:19

Changing assignee from was to craigcitro.


---

Comment by mabshoff created at 2008-08-12 23:46:47

Resolution: fixed


---

Comment by mabshoff created at 2008-08-12 23:46:47

This was achieved in Sage 3.1.alpha2 via #1220.

Cheers,

Michael
