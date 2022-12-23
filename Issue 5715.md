# Issue 5715: [with patch, needs review] show subdivisions for matrices over GF(2)

Issue created by migration from https://trac.sagemath.org/ticket/5715

Original creator: jhpalmieri

Original creation time: 2009-04-08 19:17:10

Assignee: jhpalmieri

Since `matrix_mod2_dense` defines its own `str` function, it overrides the function for general matrices, so for dense matrices over GF(2), subdivisions are not printed.  (See [this discussion](http://groups.google.com/group/sage-support/browse_frm/thread/a08df4717024f9c0).)

This patch deletes the `str` method for dense matrices over GF(2).


---

Attachment

This is a duplicate of #5714.


---

Comment by jhpalmieri created at 2009-04-08 19:24:40

Resolution: duplicate


---

Comment by was created at 2009-04-08 19:27:17

Needs work.  There is a *very good* reason that there is a str method for GF(2) -- it's for speed!  Check this out:

```
BEFORE YOUR PATCH:
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 0.41 s, sys: 0.01 s, total: 0.42 s
Wall time: 0.42 s
```


```
AFTER YOUR PATCH:
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 5.02 s, sys: 0.86 s, total: 5.88 s
Wall time: 5.89 s
```



---

Attachment

apply only this patch


---

Comment by robertwb created at 2009-04-09 07:23:44

I posted a new patch that handles subdivisions. I went ahead and sped up the str method while I was there too. 

Before

```
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 0.48 s, sys: 0.01 s, total: 0.49 s
Wall time: 0.50 s
```


After

```
sage: a = random_matrix(GF(2),1000)
sage: time b = a.str()
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 0.02 s
```



---

Comment by mabshoff created at 2009-04-09 09:59:45

Hmm, shouldn't this patch be reopened or maybe go to another ticket? We need to do one thing since this patch is currently closed as a dupe.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-09 10:40:29

Resolution changed from duplicate to 


---

Comment by robertwb created at 2009-04-09 10:40:29

Changing status from closed to reopened.


---

Comment by robertwb created at 2009-04-09 10:41:09

I just reopened this ticket, as it seems to have the most activity.


---

Comment by jhpalmieri created at 2009-04-13 00:15:16

Looks good, passes all tests when applied to 3.4.1.rc2.  Also fast, as robertwb pointed out above.

A question: how do you tell if a sparse matrix is too big to be converted to a dense one?  If we have a sparse mod 2 matrix, should we consider printing it by converting to a dense one and using this routine?  For a 1000x1000 random matrix, converting and using this one was about 5 times faster than just printing it.  (If this is a good idea, then it belongs in a different ticket, but I don't know if this is a good idea...)


---

Comment by mabshoff created at 2009-04-13 09:13:43

Merged 5715-mat2-subdiv.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 09:13:43

Resolution: fixed


---

Comment by robertwb created at 2009-04-14 02:12:03

How big is too big is an interesting question, but too big to convert > to big to print. Probably should be a separate ticket, but the optimizer in me sees an even easier way: create the zero matrix doing "[0 0 ... 0]" * nrows, then set the 1 entries. This wouldn't of course handle subdivisons though, but could be easily adapted to do so the same way as this code.
