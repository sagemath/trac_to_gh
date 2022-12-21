# Issue 6004: [with patch, needs review] add odd_degree_model function to hyperelliptic curves

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-05-07 20:37:05

Assignee: was

Keywords: odd degree model hyperelliptic curves

Patch says it best.  Very simple but I need this all the time.


---

Comment by was created at 2009-05-07 20:55:13

Positive review pending patch 2 having "Return an odd degree model of self, or None if one does not exist over the field of definition. " changed to something that mentions that a ValueError is raised if no model exists.

William


---

Comment by was created at 2009-05-07 21:02:10

ok, genuine positive review.


---

Attachment


---

Comment by ncalexan created at 2009-05-07 22:52:22

Only apply `trac_6004-odd-degree-model-5.patch`.  All others could be deleted.


---

Comment by mabshoff created at 2009-05-12 20:41:05

Hmm, this needs a rebase:

```
mabshoff`@`sage:/scratch/mabshoff/sage-4.0.alpha0/devel/sage$ hg import trac_6004-odd-degree-model-5.patch 
applying trac_6004-odd-degree-model-5.patch
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py
Hunk #1 FAILED at 62
1 out of 2 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej
abort: patch failed to apply
```

Most likely culprit is another patch by Nick:

```
changeset:   12218:684af2b9657e
user:        Nick Alexander <ncalexander`@`gmail.com>
date:        Thu May 07 13:37:26 2009 -0700
summary:     [mq]: trac_6004-odd-degree-model.patch
```

Might this code already be in Sage via another patch?

Cheers,

Michael


---

Attachment


---

Comment by ncalexan created at 2009-05-12 21:05:49

Apply only second patch.  There were a few lines included in #6010 by accident.


---

Comment by mabshoff created at 2009-05-12 21:20:09

Merged trac_6004-odd-degree-model-5.2.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 21:20:09

Resolution: fixed
