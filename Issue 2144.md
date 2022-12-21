# Issue 2144: hex constants do not work as expected

Issue created by migration from Trac.

Original creator: rpw

Original creation time: 2008-02-12 07:35:29

Assignee: somebody

Keywords: preparser hex constants

Trying to use hex constants in SAGE as I usually do in Python, I ran into a small issue: the following should work, but does not:


```
sage: 0x23^0x42
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0)x23**Integer(0)x42
                 ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


I was told on #sage-devel that this is due to the preparser. A work around is to use `0rx23^0rx42` instead. However, according to william_stein, 0x23 should work as well and result in an Integer and 0x23r should be treated as an int.


---

Attachment


---

Comment by ncalexan created at 2008-02-15 03:42:22

I say apply, but there are no doctests!  Why is the preparser not considered important enough to be tested?


---

Comment by mabshoff created at 2008-02-15 04:58:37

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 04:58:37

Merged in Sage 2.10.2.alpha0


---

Attachment


---

Comment by was created at 2008-02-15 10:15:09

Changing status from closed to reopened.


---

Comment by was created at 2008-02-15 10:15:09

> Why is the preparser not considered important enough to be tested?

The preparse *is* important enough to be doctests.  I certainly don't
consider that to not be the case.  Any new code in Sage should get a negative review if there is any reasonable way to test that it fixes the claimed issue, but the patch doesn't actually test this fix explicitly. 

So shis should not have been closed without a doctest.  I've attached 
a patch that does that.


---

Comment by was created at 2008-02-15 10:15:09

Resolution changed from fixed to 


---

Comment by was created at 2008-02-15 10:15:09

Changing priority from minor to blocker.


---

Comment by mabshoff created at 2008-02-15 13:23:27

While 2144-hex-preparse.patch has been merged, trac-2144-doctest.patch needs review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 22:04:57

The added doctest looks good -> positive review for trac-2144-doctest.patch


---

Comment by mabshoff created at 2008-02-15 22:05:48

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 22:05:48

Merged trac-2144-doctest.patch in Sage 2.10.2.alpha1


---

Comment by was created at 2008-02-28 04:58:14

It turns out that:

  (1) this is a dupe of #37, and

  (2) it doesn't even work!  I stupidly didn't test with interesting inputs, and with them the patch by robertwb fails.  E.g.,

```
sage: 0x10
16
sage: 0xa
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0x)a
                ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


Fortunately, I have attached a patch to #37 that really fixes
the problem.
