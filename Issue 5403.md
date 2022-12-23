# Issue 5403: fix "from ... import *" in class QuadraticForm (cf #4470)

Issue created by migration from https://trac.sagemath.org/ticket/5403

Original creator: tornaria

Original creation time: 2009-02-28 21:30:35

Assignee: mabshoff

There are a number of "from ... import *" in the new quadratic forms code. This messes up tab completion (among other issues).

The attached patch fixes the issue by explicitly listing every function defined in the quadratic forms files.


---

Attachment

patch to fix import * issues in quadratic forms


---

Comment by tornaria created at 2009-02-28 22:50:15

There are still some issues in the attached patch. I'm working on that now.


---

Comment by tornaria created at 2009-02-28 22:50:15

Changing status from new to assigned.


---

Comment by tornaria created at 2009-02-28 22:50:15

Changing assignee from mabshoff to tornaria.


---

Attachment

2nd version of the patch, stilll some issue with deepcopy


---

Comment by mabshoff created at 2009-03-01 02:29:47

Changing component from algebra to quadratic forms.


---

Comment by mabshoff created at 2009-03-01 02:29:47

This would be nice to fix since on every first startup after moving Sage or cloning python will complain about those imports.

I am also marking the patch as needs work until it is ready for review. That way the patch will not be lost :)

Cheers,

Michael


---

Attachment

3rd version of the patch, tests pass now


---

Comment by tornaria created at 2009-03-01 04:17:11

In the 3rd patch I added a fix for issue with copying and caching which for some weird reason didn't show up before. 

All quadratic_form tests pass with this patch applied (NOT incremental, just get the 3rd one).


---

Comment by tornaria created at 2009-03-01 04:17:11

Changing assignee from tornaria to mabshoff.


---

Comment by tornaria created at 2009-03-01 04:17:11

Changing status from assigned to new.


---

Comment by tornaria created at 2009-03-01 04:21:55

Changing status from new to assigned.


---

Comment by tornaria created at 2009-03-01 04:21:55

Changing assignee from mabshoff to tornaria.


---

Comment by mabshoff created at 2009-03-02 04:00:08

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 04:00:25

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 04:00:25

Resolution: fixed


---

Attachment

This is a properly named version of Gonzalo's third patch
