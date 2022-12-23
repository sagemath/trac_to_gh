# Issue 5820: bug in comparison of ring morphisms

Issue created by migration from https://trac.sagemath.org/ticket/5820

Original creator: AlexGhitza

Original creation time: 2009-04-19 02:54:39

Assignee: tbd

Keywords: morphism ring comparison loads dumps

As discussed at http://groups.google.com/group/sage-devel/browse_thread/thread/bc99d36058aff638 , the following is wrong:


```
sage: f = ZZ.hom(QQ)
sage: g = loads(dumps(f))
sage: f == g
False
```


(It should return True.)



---

Comment by AlexGhitza created at 2009-04-25 09:46:13

Changing assignee from tbd to AlexGhitza.


---

Comment by AlexGhitza created at 2009-04-25 09:46:13

Changing keywords from "morphism ring comparison loads dumps" to "ring coercion morphism comparison loads dumps".


---

Comment by AlexGhitza created at 2009-04-25 09:46:13

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-04-25 09:46:13

This is actually a problem with ring coercion morphisms, namely that they don't have a comparison method defined.

The attached patch does this and adds doctests (including `f == loads(dumps(f))`).


---

Attachment


---

Comment by roed created at 2009-04-29 18:04:02

Looks good to me.


---

Comment by mabshoff created at 2009-04-30 01:27:40

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 01:27:40

Resolution: fixed
