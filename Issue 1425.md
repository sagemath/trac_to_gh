# Issue 1425: wrong automatic simplification of pow

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-12-08 10:07:59

Assignee: was

The following simplification is wrong in my opinion:

```
sage: pow(pow(z,2),1/3)
z^(2/3)
```

For example for z = -1, pow(pow(-1,2),1/3) gives 1, but pow(-1,2/3) should give -1/2+sqrt(3)/2*I
(it gives currently 1 in sage, which is another bug in my opinion):

```
sage: pow(-1,2/3)
1
```


Indeed pow(z,a/b) for a and b integers is defined to be pow(pow(z,1/b),a), where pow(z,1/b) is the
principal b-th root of z, i.e., in the argument domain (-pi/b, pi/b]. Thus the other simplification
pow(pow(z,1/b),a) -> pow(z, a/b) is valid, but pow(pow(z,a),1/b) -> pow(z,a/b) is not.
It suffices to consider the case a=b to understand this:

```
sage: pow(pow(z,2),1/2)
abs(z)
sage: pow(pow(z,3),1/3)
z
```



---

Comment by was created at 2007-12-10 05:31:10

This is likely deep in the core of Maxima, so a serious pain (= basically impossible) etc to fix in a way that would really work.  It could be reported to maxima, but could we even convince them that it is a bug?  (Hopefully).


```
(%i3) ((-1)^2)^(1/3);
(%o3)                                  1
(%i4) (-1)^(2/3);
(%o4)                                  1
```



---

Comment by was created at 2007-12-10 05:31:10

Changing priority from critical to major.


---

Comment by mhansen created at 2007-12-10 23:50:58

I sent an email to the maxima mailing list.


---

Comment by mhansen created at 2007-12-11 02:52:33

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-11 02:52:33


```
 (%i1) domain : complex$

 (%i2) (x^2)^(1/3);
 (%o2) (x^2)^(1/3)

 (%i3) ((-1)^2)^(1/3);
 (%o3) 1

 (%i4) (-1)^(2/3);
 (%o4) (-1)^(2/3)

 (%i5) rectform(%);
 (%o5) (sqrt(3)*%i)/2-1/2
```



---

Comment by mhansen created at 2007-12-11 02:52:33

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-11 03:34:30

Unfortunately, this causes another major problem:


```
(%i13) domain: complex$
(%i14) radcan( sqrt(x^2) - x );
(%o14)                                 0
(%i15) domain: real$
(%i16) radcan( sqrt(x^2) - x );
(%o16)                            abs(x) - x
```


which causes

```
sage: bool(sqrt(x^2) == x)
True
```



---

Attachment


---

Comment by cwitty created at 2007-12-15 02:47:13

It looks like this patch leaves maxima with its default "real" domain until the first call to simplify_radical, and then maxima is changed to use the "complex" domain.  That doesn't seem right; shouldn't there be a chunk of code somewhere to change to the "complex" domain on startup?


---

Comment by mhansen created at 2007-12-15 07:50:13

Oops, I forgot to commit sage/interfaces/r.py .  I've posted a patch with that change.


---

Attachment

I do *not* like 1425-2.patch.  We should *not* set complex domain for *all* maxima interfaces -- only for the one used by the calculus package.


---

Attachment


---

Comment by was created at 2007-12-15 13:42:22

NOTE!!   Apply only 1425.patch and trac-125-refeee.patch.

DO NOT apply 1425-2.patch.


---

Comment by mabshoff created at 2007-12-15 13:58:35

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 13:58:35

Merged in 2.9.rc0.
