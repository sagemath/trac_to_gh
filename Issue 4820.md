# Issue 4820: Type inconsistency in rational points on elliptic curves

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-17 11:55:08

Assignee: was

Keywords: elliptic curves

Points on elliptic curves over Q which are not [0:1:0] have their last coordinate =1 but sometimes this is an int (not even an Integer) which breaks some code:


```
sage: E=EllipticCurve('37a1')
sage: [type(c) for c in E(0)]

[<type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>]
sage: [type(c) for c in E.gen(0)]

[<type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>]
sage: [type(c) for c in 2*E.gen(0)]

[<type 'sage.rings.rational.Rational'>,
 <type 'sage.rings.rational.Rational'>,
 <type 'int'>]
```

I am tracking this down and will post a patch soon.



---

Attachment


---

Comment by ncalexan created at 2009-01-21 22:11:35

Looks fine by me.  I checked that (0 : 1 : 0) over a non-standard ring had the correct types.


---

Comment by mabshoff created at 2009-01-23 10:26:58

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:26:58

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2009-01-23 10:26:58

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-23 10:28:46

Changing status from assigned to new.


---

Comment by mabshoff created at 2009-01-23 10:28:46

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2009-01-23 10:28:56

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 10:28:56

Merged in Sage 3.3.alpha1

Cheers,

Michael
