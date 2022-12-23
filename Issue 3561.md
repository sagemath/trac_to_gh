# Issue 3561: make it so sage does *not* import numpy by default on startup.

Issue created by migration from https://trac.sagemath.org/ticket/3561

Original creator: was

Original creation time: 2008-07-06 08:46:08

Assignee: cwitty




---

Comment by was created at 2008-07-06 09:18:14

The attached patch gets rid of a bunch of numpy imports.  However, according to 

```
  sage -timeup
```

(see #3559) there is still some mysterious numpy import that gets triggered in real_double_vector.pyx.  I'm very confused by that since there is no python "import numpy" anywhere there.  Fixing that can be another ticket for later.


---

Attachment

Patch looks good to me. Positive review.


---

Comment by mabshoff created at 2008-07-06 09:47:37

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 09:47:37

Merged in Sage 3.0.4.alpha2
