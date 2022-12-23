# Issue 2459: Fix GSL_DISABLE_DEPRECAED macro in setup.py

Issue created by migration from https://trac.sagemath.org/ticket/2459

Original creator: mabshoff

Original creation time: 2008-03-10 14:58:39

Assignee: mabshoff

Francois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that:

```
In sage-2.10.3.rc3 in the top setup.py at line 430 we have:
define_macros = [('GSL_DISABLE_DEPRECAED','1')]
For those who can't spot it, it miss a 'T'. 
```




---

Comment by mabshoff created at 2008-03-10 14:59:37

Changing component from Cygwin to build.


---

Attachment


---

Comment by dfdeshom created at 2008-03-14 05:45:25

I've attached a patch that fixes this typo. `real_double_vector` (the module to be built in line 430) built fine and passed all doctests.


---

Comment by mabshoff created at 2008-03-15 07:33:45

Patch looks good to me and does the right thing.


---

Comment by mabshoff created at 2008-03-15 08:07:27

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 08:07:27

Merged in Sage 2.10.4.alpha0
