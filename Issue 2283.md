# Issue 2283: the coercion code (in __mul__) should call __rmul__ when left or right is not coercible to a Sage element

Issue created by migration from https://trac.sagemath.org/ticket/2283

Original creator: was

Original creation time: 2008-02-23 22:32:25

Assignee: robertwb

In this example the last print statement goes boom, but should work fine.


```
class Foo:
   def __rmul__(self, left):
      return 'hello'

H = Foo()
print int(3)*H
print 3*H
```





---

Attachment


---

Comment by jason created at 2008-02-27 21:28:03

Currently, (before this patch), if a class did


```
_r_action = __rmul__
```


things would work since the coercion model looks for an _r_action function as a last resort.  This patch just makes this line unnecessary by having the coercion system also look for an __rmul__ function (which is standard python; see http://docs.python.org/ref/numeric-types.html)

Apparently this patch is controversial to at least one person, so it probably ought to be discussed.


---

Comment by jason created at 2008-02-27 21:30:03

disclaimer: I don't know much at all about the coercion system; the above statements are from observations made in running examples.


---

Attachment

credit goes to gfurnish for noticing and helping track down the segfault that the original patch introduced!

Apply coercion-rmul2.patch instead of coercion-rmul.patch


---

Comment by jason created at 2008-02-28 04:48:28

(and gfurnish also knew how to fix the error causing the segfault!)


---

Comment by jason created at 2008-02-28 04:56:05

The patches above apply to 2.10.2.


---

Comment by was created at 2008-02-28 05:18:12

Looks good to me. Thanks guys!


---

Comment by mabshoff created at 2008-02-28 06:14:01

Merged coercion-rmul2.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 06:14:01

Resolution: fixed
