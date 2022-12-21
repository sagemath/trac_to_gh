# Issue 5536: [with patch, review pending] trivial docstring patches for permgp.py

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-16 22:50:39

Assignee: jhpalmieri

The subject says it all.



---

Attachment

REFEREE REPORT



The patch *permgp.patch* applies OK against Sage 3.4 and all doctests passed with the options

```
-t -long
```

The reference manual builds fine. Looking at the HTML doc for `sage/groups/perm_gps/permgroup.py`, I see that the patch fixes the formatting issues that it meant to fix. So positive review. 



However, while reviewing the patch I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. But these are addressed in ticket #5542.


---

Comment by mabshoff created at 2009-03-20 21:20:17

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-20 21:20:17

Resolution: fixed
