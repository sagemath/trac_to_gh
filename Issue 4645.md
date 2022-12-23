# Issue 4645: in setup.py module_list.py is hidden with no comment.  VERY CONFUSING

Issue created by migration from https://trac.sagemath.org/ticket/4645

Original creator: was

Original creation time: 2008-11-28 21:47:12

Assignee: mabshoff

Right in the middle of setup.py we find:

```

from module_list import ext_modules

```

without further comment.

Move this line to the very top of setup.py and surround it be huge helpful comments.




---

Comment by mabshoff created at 2008-11-29 06:08:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-29 06:08:38

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 06:26:48

The patch is at #4647. William gave the code already a blessing in IRC.

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-29 07:12:52

Yeah, it was pretty sloppy to not make any comments about where the module listing went. Positive review.


---

Comment by mabshoff created at 2008-11-29 07:36:51

Resolution: fixed


---

Comment by mabshoff created at 2008-11-29 07:36:51

Merged in Sage 3.2.1.rc0
