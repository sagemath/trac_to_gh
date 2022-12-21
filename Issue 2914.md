# Issue 2914: integers are immutable but set_str breaks that -- having this function is a *major* bug.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-14 04:01:26

Assignee: mabshoff

This is *terrible*


```
sage: n = 10
sage: n.set_str('15')
sage: n
15
```


The set_str function must be made __ or removed.

Look at what evil can occur:

```
sage: a = matrix(ZZ,2,[1,2,3,4]); d = a.det(); d
-2
sage: d.set_str('10')
sage: a.det()
10
```



---

Comment by mabshoff created at 2008-04-14 04:13:18

Changing component from Cygwin to basic arithmetic.


---

Comment by mabshoff created at 2008-04-14 04:13:18

Changing assignee from mabshoff to somebody.


---

Attachment


---

Comment by ncalexan created at 2008-04-14 06:02:08

This looks good and should be applied.

In general I prefer single underscores to double -- strange things happen with double when inheritance comes in.  But in this situation, perhaps double is justified?

In the docstrings for the rational fixes, integer needs to be replaced by rational in a few places.


---

Comment by ncalexan created at 2008-04-14 06:03:25

The fact that this is not touched *anywhere* else in the Sage codebase (or that there's a mistake) suggests this could just be deleted.  Why not just nuke the functionality, or make it only available from Cython?


---

Comment by was created at 2008-04-14 14:47:31

I've attached a new patch that just nukes the functionality, as Nick suggested. 
This should be applied *instead* of the previously posted patch.

 -- William


---

Comment by was created at 2008-04-14 14:48:51

apply this instead of previous version


---

Attachment


---

Comment by ncalexan created at 2008-04-14 15:37:02

I think this is better.


---

Comment by mabshoff created at 2008-04-14 17:04:27

Merged sage-2914_nuke_em.patch in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-14 17:04:27

Resolution: fixed
