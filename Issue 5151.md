# Issue 5151: linear codes decoding algorithms in Sage

Issue created by migration from https://trac.sagemath.org/ticket/5151

Original creator: wdj

Original creation time: 2009-02-01 21:11:09

Assignee: rlm

The goal of this patch is to move some more of the algorithms in (the GAP package for error-correcting codes) Guava over to Sage. Currently Guava is included in Sage (in fact, Guava is the only GAP package included in Sage), but once the commands are implemented in Python (or Cython) it will be possible to remove Guava from Sage, while keeping Guava as an optional package. 

The patch adds a new file/module with 2 decoding methods implemented but does not import it into the namespace. Instead, methods from linear_code import them locally as needed.


---

Comment by wdj created at 2009-02-01 21:37:07

to be applied to 3.3.alpha3


---

Attachment


---

Comment by rlm created at 2009-02-04 23:03:28

Some suggestions:

 * The function `weight_order` doesn't get used anywhere, and should probably be removed from the patch. Also, you should remove the commented lines in `syndrome`.

 * The docs for `coset_leader` are identical to those for `syndrome` up to the examples. Perhaps this needs to be updated.

 * The patch file itself looks funny, since the

```
# HG changeset patch
# User David Joyner <wdjoyner@gmail.com>
# Date 1233523816 18000
# Node ID d5554b7ab8b14d7b369a200284355d135f319271
# Parent  d949d3b0e84312be26ede6df676eece1bac738f0
added decoder - wdj
```

   block shows up twice.


---

Comment by wdj created at 2009-02-04 23:48:04

to be applied to 3.3.alpha3. Ignore previous patch.


---

Attachment

Okay, I redid the patch following these instructions.

It will now not pass sage -t because now it gets lots of print statements "Warning: this should never happen" (from gap.py I think), followed by the correct answer. So the gap interface seems to be printing this message but the code I wrote is returning the correct answer. (After building guava "manually", sage -t -long has the same problem.)


---

Comment by rlm created at 2009-02-05 23:13:50

Apply after other patch


---

Attachment

I can't reproduce those errors, so positive review.


---

Comment by mabshoff created at 2009-02-06 23:04:35

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-07 01:38:05

Resolution: fixed


---

Comment by mabshoff created at 2009-02-07 01:38:05

Merged trac-5151-decoder2.patch and trac-5151-fix.patch in Sage 3.3.alpha6.

Cheers,

Michael
