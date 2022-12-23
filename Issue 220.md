# Issue 220: SageX: generic power series over arbitrary ring

Issue created by migration from https://trac.sagemath.org/ticket/220

Original creator: was

Original creation time: 2007-01-25 19:01:19

Assignee: somebody




---

Comment by was created at 2007-01-25 21:24:40

Steps to get this done:
   1. Read through the current python code and add doctests for every single function.
   2. Move the abstract base class into a SageX file.
   3. Get to compile.
   4. Make the changes needed so it works correctly, e.g., Py_ssize_t's, etc. 
 
Later on -- make some specialized classes...


---

Comment by robertwb created at 2007-10-29 17:01:27

Are 2-4 done?


---

Comment by mhansen created at 2008-11-14 08:43:33

I think this has already been done as evidenced by sage/rings/power_series*.pyx.  This was done around Sage 2.4.2 -- changeset 4159.


---

Comment by mhansen created at 2008-11-14 08:43:33

Resolution: fixed
