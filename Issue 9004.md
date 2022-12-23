# Issue 9004: __cmp__ in sage/sets/set.py doesn't do what it's supposed to do.

Issue created by migration from https://trac.sagemath.org/ticket/9004

Original creator: fbissey

Original creation time: 2010-05-21 04:11:24

Assignee: AlexGhitza

According to the comments in the code:
-----
        Compare self and right.

        If right is not a Set compare types.  If right is also a Set,
        returns comparison on the underlying objects.
----
But that is not what is currently done. In the case where 
right is not a Set (more accurately a "Set_object" that's
possibly another issue) the following is evaluated:


```
cmp(type(right), type(Set_object))
```


The correct thing would be to compare type(right) with
the type "Set_object" [which is type(self)] not the type
*of* Set_object.

Patch to follow.


---

Attachment


---

Comment by mvngu created at 2010-05-21 10:51:50

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-05-21 10:52:46

Looks good to me.


---

Comment by mvngu created at 2010-05-21 10:52:46

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-03 15:47:23

This patch was still wrong, since it was backwards still.   See #9121 which is basically the same.


---

Comment by was created at 2010-06-03 15:47:23

Resolution: duplicate
