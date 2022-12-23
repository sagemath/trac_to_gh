# Issue 684: NTL integers do not coerce to SAGE integers

Issue created by migration from https://trac.sagemath.org/ticket/684

Original creator: dmharvey

Original creation time: 2007-09-18 00:49:08

Assignee: was


```
sage: x = ntl.ZZ(5)
sage: x
5
sage: type(x)
<type 'sage.libs.ntl.ntl.ntl_ZZ'>
sage: Integer(x)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

/home/dmharvey/integer.pyx in integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
```




---

Comment by was created at 2007-09-18 00:54:32

Changing type from defect to enhancement.


---

Comment by was created at 2007-09-18 00:54:32

This isn't a bug, it's a lack of something that would be nice being implemented (because we never got to it).

It's easy to do this:


```
sage: Integer(repr(ntl.ZZ_random(1000)))
937
```


However, that uses base 10 strings.   It would be much better to get at the underlying
NTL pointer to some GMP data.  I have no clue how to do that. 

William


---

Comment by dmharvey created at 2007-09-28 04:03:55

Changing assignee from was to dmharvey.


---

Comment by dmharvey created at 2007-09-28 04:03:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-18 10:03:42

This seems to work now:

```
mabshoff@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.7, Release Date: 2007-10-15                       |
| Type notebook() for the GUI, and license() for information.        |
sage: x = ntl.ZZ(5)
sage: x
5
sage: type(x)
<type 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
sage: Integer(x)
5
```

Should it be closed?

Cheers,

Michael


---

Comment by was created at 2007-10-19 01:10:20

Yep, this fully works now, and is implemented in ntl_wrap.cpp.  Nice.


---

Comment by was created at 2007-10-19 01:10:20

Resolution: fixed
